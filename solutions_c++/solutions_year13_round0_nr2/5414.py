#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;

int main() {
    int T,N,M,arr[105][105],check;
    bool cek,cek1,cek2,hasil;
    vector<int> values;
    vector< pair<int, int> > pos;
    scanf("%d",&T);
    for(int z=1;z<=T;z++) {
        aa :
        if(z>T) break;
        values.clear();
        hasil=true;
        scanf("%d%d",&N,&M);
        for(int a=0;a<N;a++)
            for(int b=0;b<M;b++) {
                scanf("%d",&arr[a][b]);
                cek=true;
                for(int c=0;c<values.size();c++) if(arr[a][b]==values[c]) cek=false;
                if(cek) values.push_back(arr[a][b]);
            }
        sort(values.begin(),values.end());
        for(int x=0;x<values.size();x++) {
            check=values[x];
            for(int a=0;a<N;a++) {
                for(int b=0;b<M;b++) {
                    if(arr[a][b]==check) {
                        pos.push_back(make_pair(a,b));
                        cek1=true;
                        cek2=true;
                        for(int c=0;c<N;c++) if(arr[c][b]!=arr[a][b]) cek1=false;
                        for(int c=0;c<M;c++) if(arr[a][c]!=arr[a][b]) cek2=false;
                        hasil=cek1||cek2;
                        if(!hasil) {
                            printf("Case #%d: NO\n",z);
                            z++;
                            goto aa;
                        }
                    }
                }   
            }
            for(int a=0;a<pos.size();a++) arr[pos[a].first][pos[a].second]=values[x+1];
            pos.clear();
        }
        if(hasil) printf("Case #%d: YES\n",z);
    }
    return 0;
}
