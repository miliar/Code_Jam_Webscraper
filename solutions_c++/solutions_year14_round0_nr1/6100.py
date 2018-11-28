#include <iostream>
#include <vector>
using namespace std;

int main(){
    int T;
    cin >> T;
    int ca = 0;
    while(T--){
        int n1,n2;
        int v1[5][5],v2[5][5];
        cin >> n1;
        for(int i=0;i<4;++i){
            for(int j=0;j<4;++j){
                cin >> v1[i][j];
            }
        }
        cin >> n2;
        for(int i=0;i<4;++i){
            for(int j=0;j<4;++j){
                cin >> v2[i][j];
            }
        }
        int ans = 0;
        int anscnt = 0;
        for(int i=0;i<4;i++){
            int choose = v1[n1-1][i];
            for(int j=0;j<4;++j){
                if(v2[n2-1][j]==choose){
                    ans = choose;
                    anscnt++;
                }
            }
        }
        cout << "Case #" << ++ca <<": ";
        if(anscnt == 1){
            cout << ans << endl;
        }
        else if(anscnt == 0){
            cout << "Volunteer cheated!" << endl;
        }
        else
        cout << "Bad magician!" << endl;
    }
}
