#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

int main(){
    int T;
    cin >> T;
    for(int t = 1; t <= T; t++){
        int max_v;
        string str;
        cin >> max_v >> str;
        int ans = 0;
        int total = 0;
        for(int i = 0; i <= max_v; i++){
            int num = str[i] - '0';
            for(int j = 0; j < num; j++){
                while(i > total){
                    ans++;
                    total++;
                }
                total++;
            }
        }
        cout << "Case #" << t << ": " << ans << endl;
    }
    return 0;
}


