#include<iostream>
#include<cstdio>
#include<cstring>
#include<string>
#include<vector>
#include<algorithm>
#include<map>
#include<set>
#include<stack>
#include<queue>
#include<cmath>

typedef long long ll;

using namespace std;

int main(){
    freopen("input.in","r",stdin);
    freopen("output.out","w", stdout);

    int t;
    cin >> t;
    int ntc = 1;
    int k;
    while( t-- ){
        int a,b;
        cin >> a;
        int first[20], second[20];
        for( int i = 1; i <= 4;i++ )
            for( int j = 0 ; j < 4;j++ ){
                cin >> k;
                first[k] = i;
            }
        cin >> b;
        for( int i = 1; i <= 4;i++ )
            for( int j = 0 ; j < 4;j++ ){
                cin >> k;
                second[k] = i;
            }

        int ans = 0, cant = 0;
        for( int i = 1; i <= 16;i++ ){
            if( first[i] == a && second[i] == b ){
                cant++;
                ans = i;
            }
        }
        printf("Case #%d: ", ntc);
        ntc++;
        if( cant == 0 )
            printf("Volunteer cheated!");
        if( cant == 1 )
            cout << ans;
        if( cant > 1 )
            cout << "Bad magician!";
        cout << endl;

    }

    return 0;
}
