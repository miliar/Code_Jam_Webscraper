/*
ID: kishwarshafin
PROG:
LANG: C++
*/
/*
Timus JI: 119454XP
*/
#include<iostream>
#include<vector>
#include<stack>
#include<string>
#include<queue>
#include<map>
#include<algorithm>
#include<sstream>
using namespace std;
#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<math.h>
#define MAX 100
#define INF 1<<23

#define I1(a) scanf("%d",&a)
#define I2(a,b) scanf("%d %d",&a,&b)
#define I3(a,b,c) scanf("%d %d %d",&a,&b,&c)
#define rep(i,s,e) for(i=s;i<e;i++)
#define repr(i,s,e) for(i=s;i>e;i--)


#define in(a) freopen(a,"r",stdin)
#define out(a) freopen(a,"w",stdout)
#define ll long long
ll BigMod(ll B,ll P,ll M){  ll R=1; while(P>0)  {if(P%2==1){R=(R*B)%M;}P/=2;B=(B*B)%M;} return R%M;}
#define ull unsigned long long
int N,M;
int lawn[110][110];
int rm[110];
int cm[110];
int current[110][110];
int main()
{
    #ifndef ONLINE_JUDGE
	in("in.txt");
	out("out.txt");
    #endif

    int t,caseno=1;
    cin>>t;
    while(t--)
    {
        scanf("%d %d",&N,&M);
        memset(rm,0,sizeof(rm));
        memset(cm,0,sizeof(cm));

        for(int i=0;i<N;i++)
        {
            for(int j=0;j<M;j++)
            {
                current[i][j]=100;
                scanf("%d",&lawn[i][j]);
                rm[i]=max(rm[i],lawn[i][j]);
                cm[j]=max(cm[j],lawn[i][j]);
            }
        }

        for(int i=0;i<N;i++)
        {
            for(int j=0;j<M;j++)
            {
                if(current[i][j]>rm[i])
                {
                    current[i][j]=rm[i];
                }
            }
        }


        for(int i=0;i<N;i++)
        {
            for(int j=0;j<M;j++)
            {
                if(current[i][j]>cm[j])
                {
                    current[i][j]=cm[j];
                }
            }
        }

        bool yes=1;
        for(int i=0;i<N;i++)
        {
            for(int j=0;j<M;j++)
            {
                if(current[i][j]!=lawn[i][j])
                    yes=0;
//                cout<<current[i][j]<<" ";
            }
//            cout<<endl;
        }
//        cout<<endl;
        printf("Case #%d: ",caseno++);

        if(yes)
            printf("YES\n");
        else printf("NO\n");
    }
	return 0;
}
