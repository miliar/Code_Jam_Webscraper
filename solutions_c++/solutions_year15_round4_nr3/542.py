#include<stdio.h>
#include<iostream>
#include<algorithm>
#include<vector>
#include<math.h>
#include<string.h>
#include<string>
#include<vector>
#include<map>
#include<set>
#include<iostream>

using namespace std;

typedef long long ll;

map<string,int> ma;

char c[1000005];
int n;

set<int> ve[205];

int f[200005];

set<int> s1,s2;

int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);
    int T,I=1,i,j;
    scanf("%d",&T);
    while(T--)
    {
        ma.clear();
        cin>>n;
        int id=0;
        for(i=0;i<n;i++) ve[i].clear();
        memset(f,0,sizeof(f));
        cin.getline(c,1000005,'\n');
        for(i=0;i<n;i++)
        {
            cin.getline(c,1000005,'\n');
            string tt;
            int nn=strlen(c);
            for(j=0;j<=nn;j++)
            {
                if(j<nn&&c[j]!=' ') tt=tt+c[j];
                else
                {
                    if(ma.find(tt)==ma.end()) ma[tt]=id,++id;
                    int cur=ma[tt];
                    f[cur]=f[cur]|(1<<i);
                    //cout<<tt<<" "<<i<<" "<<cur<<" "<<f[cur]<<endl;
                    tt.clear();
                }
            }
        }
        //for(i=0;i<id;i++) cout<<f[i]<<" !\n";cout<<endl;
        printf("Case #%d: ",I++);
        int nn=0,rr=100000;
        for(nn=0;nn<1<<(n-2);nn++)
        {
            int rt=0;
            int nnt=nn*4+1;
            for(i=0;i<id;i++)
            {
                if((nnt&f[i])&&((nnt&f[i])!=f[i])) ++rt;
                if(rt>=rr) break;
            }
            rr=min(rr,rt);
        }
        printf("%d\n",rr);
    }
    return 0;
}
