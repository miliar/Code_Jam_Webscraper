#include <bits/stdc++.h>
using namespace std;
 
typedef pair<int,int> pii;
typedef long long ll;

void fastStream(){cin.tie(0);std::ios_base::sync_with_stdio(0);}


int main(){
    fastStream();
    int T;
    cin >> T;
    for(int t = 1; t <= T; t++){
        cout << "Case #" << t << ": ";
        string S;
        int K;
        cin >> S;
        cin >> K;
        vector<int> seq;
        for(int i = 0; i < (int)S.size(); i++){
            seq.push_back(S[i] == '+');
        }

        int flip = 0;
        for(int i = 0; i + K <= (int)S.size(); i++){
            if(seq[i] == 0){
                flip++;
                for(int j = 0; j < K; j++){
                    seq[i + j] ^= 1;
                }
            }
        }
        if(std::count(seq.begin(), seq.end(), 1) == (int)S.size()){
            cout << flip << endl;
        }
        else{
            cout << "IMPOSSIBLE" << endl;
        }
    }
  
    return 0;
}
