#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>

using namespace std;

vector<double> nao, ken;

int main(void){
    
    freopen("D-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    
    int cas, c=0, n, war, deceit_war;
    double wei;
    
    scanf("%d", &cas);
    while( cas-- ){
        scanf("%d", &n);
        nao.clear();    ken.clear();
        for(int i=0; i<n; ++i){
            scanf("%lf", &wei);
            nao.push_back(wei);
        }
        for(int i=0; i<n; ++i){
            scanf("%lf", &wei);
            ken.push_back(wei);
        }
        sort(nao.begin(), nao.end());
        sort(ken.begin(), ken.end());
        
        war = n;
        for(int i=0,j=0; i<n&&j<n; ++i) for(j; j<n; ++j){
            if( nao[i] > ken[j] )   continue;
            --war;  ++j;    break;
        }
        
        deceit_war = 0;
        for(int i=n-1,j=n-1; i>=0&&j>=0; --i) for(j; j>=0; --j){
            if( nao[i] < ken[j] )   continue;
            ++deceit_war;   --j;    break;
        }
        
        printf("Case #%d: %d %d\n", ++c, deceit_war, war);
        
    }
    
    return 0;
}
