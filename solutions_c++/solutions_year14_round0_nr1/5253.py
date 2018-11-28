#include <cstdio>
#include <cstring>
using namespace std;

FILE *in = fopen( "A-small-attempt3.in", "r" );
FILE *out = fopen( "A-small-attempt3.out", "w" );
int t,f,s,first[4][4],second[4][4],vis[17];
int cnt = 0;
void solve() {
    cnt ++;

    fscanf(in,"%d",&f);
    for(int i = 0;i < 4;i ++)
        for(int j = 0;j < 4;j ++)
            fscanf(in,"%d",&first[i][j]);
    fscanf(in,"%d",&s);
    for(int i = 0;i < 4;i ++)
        for(int j = 0;j < 4;j ++)
            fscanf(in,"%d",&second[i][j]);
    memset(vis,0,sizeof(vis));

    for(int i = 0;i < 4;i ++)
        vis[first[f - 1][i]] ++,vis[second[s - 1][i]] ++;

    int ans = 0,pos;
    for(int i = 1;i <= 16;i ++) {
        if(vis[i] == 2) ans ++,pos = i;
    }
    if(ans == 0)
        fprintf(out,"Case #%d: Volunteer cheated!\n",cnt);
    else if(ans >= 2)
        fprintf(out,"Case #%d: Bad magician!\n",cnt);
    else
        fprintf(out,"Case #%d: %d\n",cnt,pos);

   // for(int i = 1;i < 17;i ++)
       // printf("%d ",vis[i]);
}
int main() {
    fscanf(in,"%d",&t);
    while(t --) {
        solve();
    }
    fclose(in);
    fclose(out);
    return 0;
}
