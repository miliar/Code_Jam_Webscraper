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
    int t,i,j=1,d,p;
    cin>>t;
    int a[1005];
    int max_cake = -1;
    while(t--)
    {
        cin>>d;
        f(i,0,d)
        {
            cin>>a[i];
            max_cake = max1(max_cake,a[i]);
        }
        int ans = max_cake; // answer can't be greater than this

        // cout<<max_cake<<endl;
        // we will check the minimum for each possible type of division, 
        f(i,1,max_cake+1) // varying from no divisions to one to all //1-indexing to avoid zero
        {
            int j;
            int min= 0;
            int temp = 0;
            f(j,0,d)
            {
                if(a[j]>i) // check if dividable
                {
                    min += (a[j]/i);
                    if(a[j]% i == 0)
                        min --;
                    temp = max1(temp,i);
                    //cout<<temp<<endl;
                }
                else
                    {
                        temp = max1(temp,a[j]); //not dividable
                        //cout<<temp<<endl;
                    }
            }
            min += temp;
            if(min < ans)
                ans = min;


        }




            cout<<"Case #"<<j<<": "<<ans<<endl;
            j++;



    }

    return 0;
}

