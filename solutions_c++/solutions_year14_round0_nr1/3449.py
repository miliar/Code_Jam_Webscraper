#include <iostream>

using namespace std;

int var1[4];
int var2[4];
int ans1, ans2;
int tmp;

int main(){
    int t;
    freopen("output.txt", "w", stdout);
    freopen("input.txt", "r", stdin);
    cin >> t;
    t++;
    for ( int test = 1; test < t; test++ ){
        
        cin >> ans1;
        
        for ( int i = 1; i < 5; i++ )
            if ( i == ans1 )
                for ( int j = 0; j < 4; j++ )
                    cin >> var1[j];
            else
                for ( int j = 0; j < 4; j++ )
                    cin >> tmp;
        
        cin >> ans2;
        
        for ( int i = 1; i < 5; i++ )
            if ( i == ans2 )
                for ( int j = 0; j < 4; j++ )
                    cin >> var2[j];
            else
                for ( int j = 0; j < 4; j++ )
                    cin >> tmp;
        
        int cnt = 0;
        int ans = -1;
        
        for ( int i = 0; i < 4; i++ ){
            bool f = false;
            for ( int j = 0; j < 4; j++ )
                if ( var1[i] == var2[j] )
                    f = true;
            if (f){
                cnt++;
                ans = var1[i];
            }
        }
        
        if ( cnt == 1 )
            cout << "Case #" << test << ": " << ans << endl;
        if ( cnt > 1 )
            cout << "Case #" << test << ": Bad magician!" << endl;
        if ( cnt == 0 )
            cout << "Case #" << test << ": Volunteer cheated!" << endl;
    }
    return 0;
}
