#include <bits/stdc++.h>

using namespace std;

map<string,int> mp;

int bel1[10010],bel2[10010];

vector<int> a[110];

char str[10010];

int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);
    int T,cas=0;
    scanf("%d",&T);
    while(T--) {
        mp.clear();
        int n,num=0;
        scanf("%d",&n);
        gets(str);
        memset(bel1,0,sizeof(bel1));
        memset(bel2,0,sizeof(bel2));
        for(int i=1;i<=n;i++) {
            a[i].clear();
            gets(str);
            int l=strlen(str);
            string temp="";
            for(int j=0;j<l;j++) {
                if(str[j]==' ') {
                    if(mp.find(temp)==mp.end())
                        mp[temp]=++num;
                    a[i].push_back(mp[temp]);
                    temp="";
                }
                else
                    temp+=str[j];
            }
            if(mp.find(temp)==mp.end())
                mp[temp]=++num;
            a[i].push_back(mp[temp]);
        }
        printf("Case #%d: ",++cas);
        for(int i=0;i<a[1].size();i++)
            bel1[a[1][i]]++;
        for(int i=0;i<a[2].size();i++)
            bel2[a[2][i]]++;
        int tot=(1<<(n-2)),m=n-2,res=100000;
        for(int i=0;i<tot;i++) {
            for(int j=0;j<m;j++) {
                if(i&(1<<j)) {
                    for(int k=0;k<a[j+3].size();k++)
                        bel1[a[j+3][k]]++;
                }
                else {
                    for(int k=0;k<a[j+3].size();k++)
                        bel2[a[j+3][k]]++;
                }
            }
            int fuck=0;
            for(int j=1;j<=num;j++) {
                if(bel1[j]&&bel2[j])
                    fuck++;
            }
            res=min(res,fuck);
            for(int j=0;j<m;j++) {
                if(i&(1<<j)) {
                    for(int k=0;k<a[j+3].size();k++)
                        bel1[a[j+3][k]]--;
                }
                else {
                    for(int k=0;k<a[j+3].size();k++)
                        bel2[a[j+3][k]]--;
                }
            }
        }
        printf("%d\n",res);
    }
    return 0;
}
