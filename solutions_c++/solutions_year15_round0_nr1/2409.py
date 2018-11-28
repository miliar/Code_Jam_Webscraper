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

int main()
{
    int t,i,j=1,n;
    cin>>n;
    while(n--)
    {
        cin>>t;
        cin.ignore();

            char a[1005];
            gets(a);
            int s= 0;
            int ans = 0;
            f(i,0,t+1)
            {
                s += a[i]-48;
                if(i+1>s)
                {
                    ans += i+1-s;
                    s = i+1;

                }
            }
            

            cout<<"Case #"<<j<<": "<<ans<<endl;
            j++;



    }

    return 0;
}

