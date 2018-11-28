#include <cstdlib>
#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;

int main(){
    freopen("t.in","r",stdin);
    freopen("t.out","w",stdout);
    int n;
    cin >> n;
    for (int test=1; test<=n; test++){
        int row;
        cin >> row;
        int num1[4];
        int num2[4];
        int count1 = 0;
        int count2 = 0;
        for (int i=0; i<4; i++)
            for (int j=0; j<4; j++){
                int temp;
                cin >> temp;
                if (i == row-1){
                    num1[count1] = temp;
                    count1++;
                }
            }
        int col;
        cin >> col;
        for (int i=0; i<4; i++){
            for (int j=0; j<4; j++){
                int temp;
                cin >> temp;
                if (i == col-1){
                    num2[count2] = temp;
                    count2++;
                }
            }
        }
        int ans = 0;
        bool has_answer = false;
        bool dup = false;
        for (int i=0; i<4; i++){
            for (int j=0; j<4; j++){
                if (num1[i] == num2[j]){
                    if (has_answer) dup = true;
                    has_answer = true;
                    ans = num1[i];
                }
            }
        }
        cout << "Case #" << test << ": ";
        if (!has_answer){
            cout << "Volunteer cheated!" << endl;
        } else if (dup){
            cout << "Bad magician!" << endl;
        } else {
            cout << ans << endl;
        }
    }
}
