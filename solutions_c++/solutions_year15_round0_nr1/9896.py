/*
ID: hanifbo1
PROG: ride
LANG: C++
*/
#include<bits/stdc++.h>

using namespace std;

#define DD          double
#define INF         1000000000000000000000
#define llu            unsigned long long
#define eps         0.000001
#define FastIO      ios_base::sync_with_stdio(0); cin.tie(0)
#define READ(f)     freopen(f,"r",stdin)
#define WRITE(f)    freopen(f,"w",stdout)
#define sc          scanf
#define pf          printf
#define mem(a,val)  memset(a,val,sizeof(a))
#define rep(s,n)    for(long i=s; i<=n;i++)
#define pb          push_back
#define ll          long long
#define pi          (2*acos(0.0))
#define mx          35000
#define ssc         sscanf
#define FOR(i,n)    for(int i=1;i<=n;i++)
#define FORL(i,n)   for(int i=0;i<n;i++)
#define PQ          priority_queue
#define sr(v)       sort(v.begin(),v.end())
#define mod         1000000007
#define sz          size()
#define Case(x)     (pf("Case %ld",x);)
#define radian(x)   ((pi/180.0)*x)
#define degree(x)   ((180.0/pi)*x)
#define inputI      ({ long tt2; sc("%ld",&tt2); tt2;})
#define inputD      ({DD a; sc("%lf",&a); a;})
#define inputLL     ({ ll a; sc("%lld",&a); a; })
#define VI          vector<int>
//#define inp2        ({long a,b})


struct info{


    int number,shyness;
};

int main()
{

    //READ("in.txt");
    WRITE("out.txt");
    //ofstream fout ("ride.out");
    //ifstream fin ("ride.in");

    int t,ks = 1;

    sc("%d",&t);

    //cout<<t<<endl;
    while(t--){
        //cout<<"yes "<<t<<endl;
        int n;

        sc("%d",&n);

        //char ch[10000];

        //sc("%s",ch);
        //cout<<n<<endl;
        int people =0;

        getchar();
        int ans = 0;

        for(int i = 0; i<=n;i++){

            //cout<<"yes "<<i<<endl;
            char c;

            sc("%c",&c);

            //cout<<c;
            int id = i;
            int value = c-'0';

            if(i == 0){

                people = c - '0';
                continue;
            }

            else if(i>people){

                ans += i-people;
                people += i-people;
            }

            people += c-'0';
        }
        //cout<<endl;

        pf("Case #%d: %d\n",ks++,ans);
    }


    return 0;
}


