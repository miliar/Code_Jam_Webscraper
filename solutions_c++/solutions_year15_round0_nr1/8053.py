#include<bits/stdc++.h>
#define  FOR(i,x,n) for(int i=x;i<n;i++)
#define rFOR(i,x,n) for(int i=x;i>n;i--)
#define  LFOR(i,x,n) for(long long i=x;i<n;i++)
#define rLFOR(i,x,n) for(long long i=x;i>n;i--)
#define b_e(x) x.begin(),x.end()
#define rb_re(x) x.rbegin(),x.rend()
#define p_b push_back
#define m_p make_pair
#define SZ size()
#define srt insert
#define CL clear()
#define DE delete
#define S string
#define SS stringstream
#define g_l(x)  getline(cin,x)
#define CIN(x)  scanf("%d",&x)
#define CIN2(x,y) scanf("%d%d",&x,&y)
#define CLN(x)  scanf("%I64d",&x)
#define CLN2(x,y)  scanf("%I64d %I64d",&x,&y)
#define CSN(x)  scanf("100000s",&x)
#define CIUT(x) printf("%d",x)
#define CLUT(x) printf("%I64d",x)
typedef long long LL;

using namespace std;

int main()
{
    freopen("output.txt","w",stdout);
    long long x,y,c,d=0,f=0;
    string in;
    cin >> x;
    while(x--){
        c=d=0;
        cin >> y; cin >> in;
        FOR(i,0,in.SZ){
            if(in[i]!='0'){
            if(i>c){
                d+=(i-c);
                c+=(i-c);
            }
            c+=(in[i]-'0');
            }
        }
        cout << "Case #" << ++f << ": " << d << endl;
    }
    return 0;
}
