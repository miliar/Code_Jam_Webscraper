#include <iostream>
#include <vector>
using namespace std;

int main(){
    int T; cin>> T;
    int CC = 0;
    while(T--) {
        int K; cin>> K;
        CC+=1;
        string val; cin>> val;
        vector<int> t;
        for(auto i: val) t.push_back(i-'0');
        int need = 0;
        int prefix_sum = t[0];
        for(int i=1; i<t.size(); ++i) {
            if (t[i]==0 || i<= prefix_sum) {
                prefix_sum += t[i];
            }
            else {
                need += i - prefix_sum;
                prefix_sum += need + t[i];
            }
        }
        cout << "Case #"<< CC << ": "<< need << endl;
    }
}
