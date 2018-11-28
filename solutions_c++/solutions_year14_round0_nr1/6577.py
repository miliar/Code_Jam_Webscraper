#include <iostream>
#include <array>
#include <vector>
#include <algorithm>

using namespace std;

using Cards = array<array<int,4>,4>;

string solve(Cards a, int an, Cards b, int bn){
    vector<int> v;
    for(int i=0;i<4;i++){
        v.push_back(a[an][i]);
    }
    auto f = [&](int n){return find(v.begin(),v.end(),n) != v.end();};
    int c = count_if(b[bn].begin(),b[bn].end(),f);
    if(c > 1){
        return "Bad magician!";
    }else if(c == 1){
        int ans = *(find_if(b[bn].begin(),b[bn].end(),f));
        return to_string(ans);
    }
    return "Volunteer cheated!";
}

int main(){
    int T;
    cin >> T;
    for(int t=1;t<=T;t++){
        int an,bn;
        Cards a,b;
        cin >> an;
        for(int i=0;i<4;i++){
            for(int j=0;j<4;j++){
                cin >> a[i][j];
            }
        }
        cin >> bn;
        for(int i=0;i<4;i++){
            for(int j=0;j<4;j++){
                cin >> b[i][j];
            }
        }
        cout << "Case #" << t << ": " << solve(a,an-1,b,bn-1) << endl;
    }
}
