#include <stdio.h>
#include <vector>
#include <algorithm>
#include <string.h>
using namespace std;

int table2[150],table1[150];

void solve(){

    int n,m,count = 0,c;
    vector <pair<int,pair<int,int> > > v;
    scanf("%d %d",&n,&m);
    for (int i=0;i<n;i++)
        for (int j=0;j<m;j++){
            scanf("%d",&c);
            v.push_back(make_pair(c,make_pair(i,j)));
        }
    sort(v.begin(),v.end());

    int i = v.size() - 1;
    int j = v.size() - 1;
     while ( j >= 0 ) {
        while ( j >= 0 && v[j].first == v[i].first ) 
        {
            int x = v[j].second.first;
            int y = v[j].second.second;

            if ( table1[x] && table2[y] )
            {
                printf("NO\n");
                return;
            }
            j--;
        }
        for (int k=i;k>j;k--)
        {
            int x = v[k].second.first;
            int y = v[k].second.second;
            table1[x] = 1;
            table2[y] = 1;
        }
        i = j;
    }
    printf("YES\n");


}


int main(){
    int t;
    scanf("%d",&t);
    for (int i=1;i<=t;i++)
    {
        memset(table1,0x00,150*sizeof(int));
        memset(table2,0x00,150*sizeof(int));
        printf("Case #%d: ",i);
        solve();
    }
    return 0;
}
