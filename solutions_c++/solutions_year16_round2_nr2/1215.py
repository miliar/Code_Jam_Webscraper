/*
TASK: Close Match
LANG: C++
*/
#include <bits/stdc++.h>
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
long long x;
int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    freopen("B-small-attempt1.in","r",stdin);
    freopen("B-small-attempt1.out","w",stdout);
    int i,j,k;
    cin >> T;
    string s1,s2;
    char tmp1[5],tmp2[5];
    int tt=0;
    while(T--)
    {
        cin >> s1 >> s2;
        k=s1.size();
        int diff=11111,Mc1=0,Mc2=0;
        M=10;
        for(i=2;i<=k;i++)
            M*=10;
        for(i=0;i<M;i++)
        {
            bool ok=true;
            sprintf(tmp1,"%*0d",k,i);
            for(int a=0;a<k;a++)
                if(s1[a]!='?' && s1[a]!=tmp1[a])
                    ok=false;
            if(!ok)
                continue;
            for(j=0;j<M;j++)
            {
                sprintf(tmp2,"%*0d",k,j);
                bool ok=true;
                for(int a=0;a<k;a++)
                {
                    if(s2[a]!='?' && s2[a]!=tmp2[a])
                        ok=false;
                }
                if(ok)
                {
                    if(abs(i-j)<diff)
                    {
                        diff=abs(i-j);
                        Mc1=i;
                        Mc2=j;
                    }
                    else if(abs(i-j)==diff)
                    {
                        if(i<Mc1)
                        {
                            Mc1=i;
                            Mc2=j;
                        }
                        else if(i==Mc1 && j<Mc2)
                            j=Mc2;
                    }
                }
            }
        }
        tt++;
        printf("Case #%d: %*0d %*0d\n",tt,k,Mc1,k,Mc2);
    }
}
