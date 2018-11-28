#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <cstdlib>
#include <cmath>
typedef long long ll ;
//const int maxx =  ;
const int inf = 1<<30 ;
int high[3000] ;
int ans[55] ;
using namespace std;
int main()
{
    int cas = 1 , T;
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    cin >> T ;
    int n ;
    while(T--){
        cin >>  n;
        memset(high,0,sizeof(high)) ;
        memset(ans,0,sizeof(ans)) ;
        int h ;
        for(int i = 0 ; i < 2*n-1 ; ++i ){
            for(int  j = 0 ;j  < n ;++j){
                cin >> h;
                high[h]++;
            }
        }
        printf("Case #%d: ",cas++) ;
        for(int i = 1 , j = 0 ; i <= 2500 ; ++i){
            if(high[i]&1) {
                ans[j++] = i;
            }
        }
        cout << ans[0] ;
        for(int i = 1 ; i < n; ++i){
            cout << " " << ans[i]  ;
        }
        cout <<endl;
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
