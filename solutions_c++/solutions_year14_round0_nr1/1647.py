#include <iostream>
#include <algorithm>
#include <memory.h>
#include <stdio.h>
#include <vector>
#include <string>
#include <vector>
#include <set>

using namespace std;
#define pb push_back
int vis[20];

int main(){
    freopen("A.in", "r", stdin );
    freopen("Aout.txt", "w", stdout );
    int tcase;
    cin>>tcase;
    int no = 0;
    int r1, r2, a;
    while(tcase--){
        memset(vis, 0, sizeof(vis));
        cin>>r1;
        for(int i = 1; i <= 4; ++i){
            for(int j = 1; j <= 4; ++j){
                cin>>a;
                if( i == r1 ) vis[ a ]++;
            }
        }
        cin>>r2;
        for(int i = 1; i <= 4; ++i)
        for(int j = 1; j <= 4; ++j){
            cin>>a;
            if( i == r2) vis[a]++;
        }

        int cont = 0, ans =  -1;
        for(int i = 1; i <= 16; ++i)
        if( vis[i] == 2 ){
            ++cont; ans = i;
        }
        printf("Case #%d: ", ++no );
        if( cont == 1 ){
            printf("%d\n", ans);
        }else if( cont == 0 ){
            printf("Volunteer cheated!\n");
        }else{
            printf("Bad magician!\n");
        }
    }
    return 0;
}
