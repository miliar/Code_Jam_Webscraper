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
int dig_s(int n)
{
	int i=0;
	int x=0;
	while(n>0)
	{
		i=n%10;
		x=x*10 + i;
		n=n/10;
	}
return x;
	
}
//prec
int dp[1000005];

int func()
{

dp[0]=0; 
int i;
f(i,1,11)
{
	dp[i] = dp[i-1] + 1;
}
f(i,11,1000001)
{
int temp = dig_s(i);

if(temp != i && dp[temp]!=-1 && i%10!=0)
	dp[i]= min(dp[i-1] + 1, dp[temp] + 1);
else
	dp[i] = dp[i-1] + 1;

}
}

int main()
{
    int t,i; int n;
    cin>>t;
    fill(dp,dp+1000002,-1);
    func();
    i=1;
    while(t--)
    {
    	int cnt = 0;
    	cin>>n;
    	//cout<<dig_s(n)<<endl;
    	cout<<"Case #"<<i<<": "<<dp[n]<<endl;
    	i++;

    }


    return 0;
}

