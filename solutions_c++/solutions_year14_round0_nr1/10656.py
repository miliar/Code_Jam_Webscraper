#include <iostream>
#include <fstream>

using namespace std;
int t;
int ars[4][4],ar[4][4];
int k = 0,a,b,ans;
int main(){
cin >> t;
for(int i = 0; i < t; i++){
k = 0;
cin >> a;
for(int j = 0;j < 4; j++)
for(int c = 0; c < 4; c++)
cin >> ars[j][c];
cin >> b;
for(int j = 0;j < 4; j++)
for(int c = 0; c < 4; c++)
cin >> ar[j][c];
 for(int c = 0; c < 4; c++){
            for(int j = 0; j < 4; j++){
                if(ars[a-1][c] == ar[b-1][j]){
                    ans = ar[b-1][j];
                    k++;
                }
            }
        }
        cout << "Case #" << i + 1 << ": ";
        if(k==0)
            cout << "Volunteer cheated!\n";
        else if(k==1)
            cout << ans << "\n";
        else cout << "Bad magician!\n";
}
return 0;
}