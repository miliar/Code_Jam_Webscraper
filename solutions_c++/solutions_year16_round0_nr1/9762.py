#include<bits/stdc++.h>
using namespace std;
#define ll long long int
#define scanl(a) scanf("%lld",&a)
#define scanii(a,b) scanf("%d%d",&a,&b)
#define scaniii(a,b,c) scanf("%d%d%d",&a,&b,&c)
#define scanll(a,b) scanf("%lld%lld",&a,&b)
#define scanlll(a,b,c) scanf("%lld%lld%lld",&a,&b,&c)
#define scani(a) scanf("%d",&a)
#define clr(a) memset(a,0,sizeof(a))
#define clr_(a) memset(a,-1,sizeof(a))
#define pb(a) push_back(a)
#define siz 1001
#define pii pair<int,int>
#define sqr(a) a*a
#define eps 1e-9
#define inf 1e9
#define pi acos(-1.0)
int fx[]={0,0,-1,1,-1,1,1,-1};
int fy[]={1,-1,0,0,1,1,-1,-1};
map<string,int>mp;
set<int>st;
int main()
{
   // freopen("out.txt","w",stdout);
    int t;
    scani(t);
    for(int test=1;test<=t;test++)
    {
        int n;
        scani((n));
        int temp=n;
        if(n==0)printf("Case #%d: INSOMNIA\n",test);
        else
        {
            int i=2;
             //  cout<<temp<<" = ";
            while(1)
            {
                //temp=n;
                int r=temp;
                while(temp>=1)
                {
                    int x=temp%10;
                    temp/=10;
                    st.insert(x);
                //    cout<<x<<" ";

                }
              //  cout<<endl;
                   if(st.size()==10)
            {
                printf("Case #%d: %d\n",test,r);
                break;
            }
                temp=n*i;
                i++;
            }


        }
           st.clear();
    }
    return 0;
}

