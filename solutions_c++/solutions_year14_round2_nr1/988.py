/*
TASK: The Repeater
LANG: C++
*/
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<map>
#include<set>
#include<list>
#include<queue>
#include<iostream>
#include<sstream>
#include<string>
#include<vector>
#include<stack>
#include<bitset>
using namespace std;
#define X first
#define Y second
#define EPS 1e-9
#define ALL(x) (x).begin(),(x).end()
#define mp(x,y) make_pair((x),(y))
#define pb(x) push_back((x))
#define FOR(i,st,ed) for(int (i)=(st);(i)<(ed);(i)++)
typedef pair<int,int> PII;
typedef vector<int> vi;
typedef vector<pair<int,int> > vii;
typedef long long LL;

int N,M,T;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("xxx.out","w",stdout);
    int i,j,k;
	scanf("%d",&T);
	int tt=0;
    while(T--)
    {
        vector<pair<char,int> > v[127];
        scanf("%d",&N);
        char ch,s[127];
        int x,y,z;
        for(i=0;i<N;i++)
        {
            scanf("%s",s);
            k=strlen(s);
            ch=s[0];    x=0;
            for(j=0;j<=k;j++)
            {
                if(ch==s[j])
                {
                    x++;
                }
                else
                {
                    v[i].pb(mp(ch,x));
                    x=1;    ch=s[j];
                }
            }
        }
        tt++;
        printf("Case #%d: ",tt);
        string ss[127];
        for(i=0;i<N;i++)
        {
            for(j=0;j<v[i].size();j++)
                ss[i]+=v[i][j].X;
 //           cout << ss[i] << endl;
        }
        bool ok=true;
        for(i=1;i<N;i++)
            if(ss[i-1]!=ss[i])
                ok=false;
        if(!ok) printf("Fegla Won\n");
        else
        {
            int Mc=0;
            for(i=0;i<v[0].size();i++)
            {
                vi temp;
                for(j=0;j<N;j++)
                {
                    temp.pb(v[j][i].Y);
                }
                sort(ALL(temp));
                if(N%2==0)
                {
                    M=temp[N/2];
                    for(j=0;j<N;j++)
                        Mc+=(abs(M-temp[j]));
                }
                else
                {
                    x=temp[N/2];    y=temp[N/2]+1;
                    if((x+y)%2==0)
                    {
                        M=(x+y)/2;
                        for(j=0;j<N;j++)
                            Mc+=(abs(M-temp[j]));
                    }
                    else
                    {
                        int p=0,q=0;
                        M=(x+y)/2;
                        for(j=0;j<N;j++)
                            p+=(abs(M-temp[j]));
                        M++;
                        for(j=0;j<N;j++)
                            q+=(abs(M-temp[j]));
                        Mc+=min(p,q);
                    }
                }
            }
            printf("%d\n",Mc);
        }
    }
}
