#include <iostream>

using namespace std;

int main(){
    freopen("/Users/zhengnanlee/Desktop/a.txt", "r", stdin);
    freopen("/Users/zhengnanlee/Desktop/b.txt", "w", stdout);
    int t;
    cin>>t;
    
    for (int k = 1; k <= t; k++) {
        int m,n;
        int a[4][4], b[4][4];
        cin>>n;
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                cin>>a[i][j];
            }
        }
        cin>>m;
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                cin>>b[i][j];
            }
        }
        int flag = 0;
        int pos = -1;
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                if(a[n-1][i] == b[m-1][j]){
                    flag++;
                    pos = i;
                }
            }
        }
        cout << "Case #" << k << ": ";
        if(flag == 0) cout << "Volunteer cheated!" << endl;
        else if(flag == 1) cout << a[n-1][pos] << endl;
        else cout << "Bad magician!" << endl;
    }
}