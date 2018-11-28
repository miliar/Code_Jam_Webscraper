#include<bits/stdc++.h>
#define LL long long int
using namespace std;

template <class T> string toString(T n)
{
    stringstream ss;
    ss<<n;
    return ss.str();
}

set<int>s;

void f(LL n)
{
    while(n)    s.insert(n % 10), n /= 10;
    return;
}



int main()
{
#ifdef akid
    freopen("input","r",stdin);
    freopen("output","w",stdout);
#endif // akid

    int t,cas=1;
    scanf("%d",&t);
    while(t--)
    {
        LL n;
        scanf("%lld",&n);
        //  cout<<n<<endl;
        printf("Case #%d: ",cas++);
        if(n==0)
        {
            printf("INSOMNIA\n");
            continue;
        }
        LL m=1;
        bool ok=false;

        LL ans=n;
        //cout<<ans<<endl;

        for(int i=0; i<200; i++)
        {
            n=ans * m;
            //cout<<n<<endl;
//            string ss=toString(n);
//            for(int i=0; i<ss.size(); i++)
//            {
//                s.insert(ss[i]);
//            }
            f(n);
            if(s.size()==10)
            {

                ans=n;
                //  cout<<ans<<endl;
                ok=true;
                break;
            }
            m+=1LL;
        }
        //cout<<ans<<endl;
        ok?printf("%lld\n",ans):printf("INSOMNIA\n");
        s.clear();
    }
    return 0;
}
