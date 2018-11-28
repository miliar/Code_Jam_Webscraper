#include<iostream>
using namespace std;
int main()
{
    int T,n,p;
    freopen("2.in","r",stdin);
    freopen("2.out","w",stdout);
    cin>>T;
    for (int TT=1;TT<=T;++TT)
    {
        int ans1,ans2;
        cin>>n>>p;
        int x=1<<n;
        for (int i=x-1;i>=0;--i)
        {
            int r=x-i,cnt=0;
            while (r>0)
            {

                r>>=1;
                ++cnt;
            }
            --cnt;
            if (x>>cnt<=p) {ans2=i;break;}
        }
        for (int i=x-1;i>=0;--i)
        {
            int r=i+1,cnt=0;
            while (r>0)
            {

                r>>=1;
                ++cnt;
            }
            --cnt;
            if (x-(x>>cnt)+1<=p) {ans1=i;break;}
        }
        printf("Case #%d: %d %d\n",TT,ans1,ans2);
    }
}
