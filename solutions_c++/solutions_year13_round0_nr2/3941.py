#include<cstdio>
#include<iostream>
#include<vector>
#include<cstdlib>
using namespace std;
#define N 110
int a[N][N];
typedef struct {
    int i,j,val;
}pt;
int ht[N][2];
pt p[10010];
void radixSort(pt *p, int cnt) {
    vector<vector< pt > > temp;
    for(int i=0;i<=100;i++) temp.push_back(vector<pt>());
    for(int i=0;i<cnt;i++) temp[p[i].val].push_back(p[i]);
    vector<vector< pt > >::iterator it;
    int j=0;
    for (it = temp.begin(); it != temp.end(); it++) {
        vector<pt>::iterator it1 = (*it).begin();
        for(it1 = (*it).begin(); it1 != (*it).end(); it1++) {
            p[j++]=*it1;
        }
    }
}
int main() {
    int tc,n,m;
    scanf("%d ",&tc);
    for(int t=0;t<tc;t++) {
        scanf(" %d %d ", &n, &m);
        int cnt=0;
        for(int i=0;i<n;i++) 
            for(int j=0;j<m;j++) {
                scanf("%d",&a[i][j]);
                pt p1 = {i,j,a[i][j]};
                p[cnt++]=p1;
            }
        radixSort(p,cnt);
        memset(ht,0,sizeof(ht[0][0])*N*2);
        int i;
        for(i=0;i<cnt;i++) {
            int currRow=p[i].i, currCol=p[i].j, currHt=p[i].val;
            if (ht[currRow][0]==currHt) continue;
            else if (ht[currCol][1]==currHt) continue;
            else {
                int j=0;
                for(j=0;j<m;j++) {
                    if(a[currRow][j]==currHt) continue;
                    else if(a[currRow][j] < currHt) continue;
                    else break;
                }
                if (j==m) ht[currRow][0]=currHt;
                for(j=0;j<n;j++) {
                    if(a[j][currCol]==currHt) continue;
                    if(a[j][currCol]<currHt) continue;
                    else break;
                }
                if(j==n) ht[currCol][1]=currHt;
                if(ht[currRow][0] != currHt && ht[currCol][1] != currHt) break;
            }
        }
        
        if(i==cnt) printf("Case #%d: YES\n",t+1);
        else printf("Case #%d: NO\n",t+1);
    }

    return 0;
}
