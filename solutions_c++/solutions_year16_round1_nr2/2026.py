#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
using namespace std;



int main(){
    int T;
    cin >> T;
    int CN = 0;
    while(T--){
        ++CN;
        int n;
        cin >> n;
        set<int> input;
        for(int i =0; i<2*n-1; i++){
            for(int j = 0; j<n; j++){
                int x;
                cin >> x;
                if(input.count(x)){
                    input.erase(x);
                }
                else{
                    input.insert(x);
                }
            }
        }
        cout << "Case #" << CN << ":";
        for(int x : input){
            cout << " " << x;
        }
        cout << endl;
    }
}
