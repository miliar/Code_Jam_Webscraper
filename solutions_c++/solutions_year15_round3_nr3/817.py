#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int N, C, D, V;

bool canMake(int amount, vector<int> &a) {
    if (amount == 0) return true;
    else if (amount < 0) return false;
    
    bool can = false;
    for (int i = 0; i < a.size(); i++) {
        vector<int> b;
        for (int j = 0; j < a.size(); j++)
            if (j != i)
                b.push_back(a[j]);
        if (canMake(amount - a[i], b)) {
            can = true;
            break;
        }
    }
    return can;
}

int main() {
    ifstream cin("/Users/byunghoon/Desktop/Programs/Programs/in.txt");
    ofstream cout("/Users/byunghoon/Desktop/Programs/Programs/out.txt");
    
    cin >> N;
    
    for (int i = 0; i < N; i++) {
        //cout << "Case #" << (i+1) << endl;
        cin >> C >> D >> V;
        
        int ans = 0;
        vector<int> a(D);
        
        //cout << "Make 1 - " << V << " using:" << endl;
        for (int j = 0; j < D; j++) {
            cin >> a[j];
            //cout << a[j] << "\t";
        }
        //cout << endl;
        
        for (int j = 1; j <= V; j++) {
            if (!canMake(j, a)) {
                ans++;
                //cout << "Add " << j << endl;
                a.push_back(j);
            }
        }
        
        cout << "Case #" << (i+1) << ": " << ans << endl;
        //cout << "FIN: " << ans << endl << endl;
    }
    
    return 0;
}