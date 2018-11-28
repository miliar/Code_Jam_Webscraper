#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
    int n;
    cin >> n;
    for(int k = 0; k < n; k++){
        int a, b, temp;
        cin >> a;
        a--;
        int x[4];
        for(int i = 0; i < 4; i++){
            if(i == a) for(int j = 0; j < 4; j++) cin >> x[j];
            else for(int j = 0; j < 4; j++) cin >> temp;
        }

        cin >> b;
        b--;
        int y[4];
        for(int i = 0; i < 4; i++){
            if(i == b) for(int j = 0; j < 4; j++) cin >> y[j];
            else for(int j = 0; j < 4; j++) cin >> temp;
        }
        int ans;
        int match = 0;
        for(int i = 0; i < 4; i++){
            for(int j = 0; j < 4; j++){
                if(x[i] == y[j]){
                    match++;
                    ans = x[i];
                }
            }
        }
        cout << "Case #" << k+1 << ": ";
        if(match == 0) cout << "Volunteer cheated!";
        else if(match == 1) cout  << ans;
        else if(match > 1) cout << "Bad magician!";
        cout << endl;
    }
}
