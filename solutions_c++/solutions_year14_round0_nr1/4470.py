#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int N = 4;

int main(void) {
    int T; cin >> T;
    for(int t =0; t < T; t++){
        vector<int> r1, r2;
        int A1; cin >> A1;
        for(int i=0; i < N; i++){
            for (int j=0; j < N; j++){
                int tmp; cin >> tmp;
                if (i == A1-1){ 
                    r1.push_back(tmp);
                }
            }
        }

        int A2; cin >> A2;
        for(int i=0; i < N; i++){
            for (int j=0; j < N; j++){
                int tmp; cin >> tmp;
                if (i == A2-1){ 
                    r2.push_back(tmp);
                }
            }
        }
        
        sort(r1.begin(), r1.end());
        sort(r2.begin(), r2.end());
        vector<int> result;
        set_intersection(r1.begin(), r1.end(), r2.begin(), r2.end(), 
                         back_inserter(result));
        
        cout << "Case #" << t+1 << ": ";
        switch(result.size()){
        case 0:
            cout << "Volunteer cheated!";
            break;
        case 1:
            cout << result.front();
            break;
        default:
            cout << "Bad magician!";
        }
        cout << endl;

#ifdef DEBUG
        cout << "#case: " << t << endl;
        cout << "A1:" << A1 << endl;
        for(auto it = r1.begin(); it != r1.end(); ++it){
            cout << *it << " ";
        }
        cout << endl;
        cout << "A2:" << A2 << endl;
        for(auto it = r2.begin(); it != r2.end(); ++it){
            cout << *it << " ";
        }
        cout << endl;
        cout << "result: ";
        for(auto it = result.begin(); it != result.end(); ++it){
            cout << *it << ", ";
        }
        cout << endl;
#endif //DEBUG

    }
}
