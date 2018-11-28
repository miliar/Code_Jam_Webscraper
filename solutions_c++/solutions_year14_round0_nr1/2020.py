#include <bits/stdc++.h>
#define mp make_pair
using namespace std;
int v1[10][10],v2[10][10];
vector<int> t1,t2;
main() {
    freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);
    ios_base::sync_with_stdio(false);
    int t;
    cin>>t;
    for(int test=1;test<=t;test++){
        printf("Case #%d: ",test);
        int x,y;
        cin>>x;
        for(int i=1;i<=4;i++)
            for(int j=1;j<=4;j++)
            cin>>v1[i][j];
        cin>>y;
        for(int i=1;i<=4;i++)
            for(int j=1;j<=4;j++)
            cin>>v2[i][j];
        t1.clear(),t2.clear();
        for(int i=1;i<=4;i++){
            t1.push_back(v1[x][i]);
            t1.push_back(v2[y][i]);
            t2.push_back(v1[x][i]);
            t2.push_back(v2[y][i]);
        }
        sort(t1.begin(),t1.end());
        sort(t2.begin(),t2.end());
        t1.resize(unique(t1.begin(),t1.end())-t1.begin());
        if(t1.size()>7) printf("Volunteer cheated!\n");
        else if(t1.size()<7) printf("Bad magician!\n");
        else{
            for(int i=1;i<=4;i++)
                for(int j=1;j<=4;j++)
                if(v1[x][i]==v2[y][j]) printf("%d\n",v1[x][i]);

        }
    }
}
