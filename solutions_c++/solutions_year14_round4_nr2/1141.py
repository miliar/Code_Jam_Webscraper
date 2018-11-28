#include <cstdio>
#include <iostream>
#include <cstring>
#include <cctype>
#include <cmath>
#include <stack>
#include <string>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <queue>
using namespace std;
#define INF 0x3f3f3f3f
#define REP(i,n) for(int i=0; i<n; i++)
typedef long long int64;
typedef pair<int,int> pii;

int v[100];

int main() {
    int nt;

    scanf("%d",&nt);
    REP(ct,nt) {
        int n;
        vector<pii> ord;
        int imax=0,res=INF;

        scanf("%d",&n);
        REP(i,n) {
            scanf("%d",&v[i]);
            if (v[i]>v[imax]) imax=i;
        }

        REP(mb,(1<<n)) {
            vector<int> ve, vd;
            int acc=0;
            for (int i=imax-1;i>=0;i--)
                if (mb & (1<<i)) vd.push_back(v[i]);
                else ve.push_back(v[i]);

            for (int i=imax+1;i<n;i++)
                if (mb & (1<<i)) {
                    ve.push_back(v[i]);
                }
                else vd.push_back(v[i]);

            int qid=0;
            map<int,int> id;
            sort(ve.begin(),ve.end());
            sort(vd.begin(),vd.end());
            reverse(vd.begin(),vd.end());
            REP(i,ve.size())
                id[ve[i]]=qid++;
            id[v[imax]]=qid++;
            REP(i,vd.size())
                id[vd[i]]=qid++;

            REP(i,n)
                REP(j,i)
                    acc+=(id[v[j]]>id[v[i]]);

            res=min(res,acc);
        }
        printf("Case #%d: %d\n",ct+1,res);
    }

    return 0;
}


