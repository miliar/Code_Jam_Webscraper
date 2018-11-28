#include <iostream>

using namespace std;

int main(){
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    int T;
    cin >> T;
    for ( int x = 1; x <= T; x++ ){
        int n1,n2,a[4],b[4],c=0,ans=0;
        int rubish;
        cin >> n1;
        for ( int i = 0; i < 4; i++ ){
            for ( int j = 0; j < 4; j++ ){
                if ( i+1 == n1 ){
                     cin >> a[j];
                } else {
                 cin >> rubish;       
                }
            }
        }
        cin >> n2;
        for ( int i = 0; i < 4; i++ ){
            for ( int j = 0; j < 4; j++ ){
                if ( i+1 == n2 ){
                     cin >> b[j];
                } else {
                  cin >> rubish;       
                }
            }
        }
        for ( int i = 0; i < 4; i++ ){
            for ( int j = 0; j < 4; j++ ){
                if ( a[i] == b[j] ){
                   ans = a[i];
                   c++;
                }    
            }
        }
        cout << "Case #" << x << ": ";
        if ( c == 0 ){
           cout << "Volunteer cheated!" << endl;
        } else if ( c > 1 ){
          cout << "Bad magician!" << endl;
        } else {
          cout << ans << endl;       
        }
    }
    return 0;
}
