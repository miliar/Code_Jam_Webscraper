#include<bits/stdc++.h>

#define llu unsigned long long
#define ll long long
#define pi 3.141592
#define nl printf("\n")
#define f(i,l1,l2) for(i=l1;i<l2;i++)
#define gc getchar_unlocked
#define vi vector<int>
#define vit vi::iterator
#define all(c) c.begin(), c.end() 
#define pb push_back
using namespace std;

/*void fin(int &x)       //does not compile in codeblocks but does in online judges
{                        //use if input too large ( only for integers )
int i=0;x=0;
register int c=gc();
while(c<48||c>57)
c=gc();
while(c>47&&c<58)
{
x=(x<<1)+(x<<3) + c-48;
i++;
c=gc();
}
}*/

int max1( int a, int b)
{
    if(a > b)
        return a;
    else
        return b;
}

int main()
{
    int t,i,n,j=1;
    cin>>t;
    while(t--)
    {

    	cin>>n;
    	int a[n+5];
    	f(i,0,n)
    	{
    		cin>>a[i];
    	}
    	int diff = -1;
    	f(i,0,n-1)
    	{
    		int temp = fabs(a[i]-a[i+1]);
    		//cout<<a[i]<<" "<<a[i+1]<<endl;
    		if(a[i]>a[i+1])
    		diff = max1(temp,diff);
    	}
    	//cout<<diff<<endl;
    	// 1
    	int ans = 0;
    	int prev=0;
    	f(i,0,n)
    	{
    		if(a[i]<prev)
    			ans += prev-a[i];
    		prev = a[i];
    	}
    	//2
    	int ans2=0;

    	f(i,0,n-1)
    	{
    		if(a[i]<diff)
    			ans2 += a[i];
    		else
    			ans2 += diff;
    	}
    	if(ans2 == -1)
    		ans2 = 0;


    	cout<<"Case #"<<j<<": "<<ans<<" "<<ans2<<endl;
                j++;
    }


    return 0;
}

