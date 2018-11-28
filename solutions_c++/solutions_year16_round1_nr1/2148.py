#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <string.h>
#include <stdio.h>
#include <math.h>
#include <queue>
#include <stack>
#include <map>
#include <ctime>
#include <set>
using namespace std;
const int N=1234;

char s[N];
vector <int> pos[30];
bool mark[N];
int main () {
    freopen("in","r",stdin);
    freopen("out.txt","w",stdout);
    int T;
    scanf("%d",&T);
    for (int cas=1;cas<=T;cas++) {
        scanf("%s",s+1);
        int n=strlen(s+1);
        memset(mark,false,sizeof mark);
        for (int i=0;i<30;i++) pos[i].clear();
        for (int i=n;i>=1;i--) {
            pos[s[i]-'A'].push_back(i);
        }
        string ret="";
        int last=n+1;
        for (int i=25;i>=0;i--) {
            if (pos[i].size()==0) continue;
            for (int j=0;j<pos[i].size();j++) {
                int u=pos[i][j];
                if (u>=last) continue;
                ret+=(char)('A'+i);
                last=u;
                mark[last]=true;
            }
        }
        for (int i=1;i<=n;i++) {
            if (mark[i]) continue;
            ret+=s[i];
        }
        printf("Case #%d: %s\n",cas,ret.c_str());
    }

    return 0;
}
