#include <iostream>
#include <fstream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

char num;
int T, D, P, i, j, t = 0;

void print(vector<int> &vi) {
    for (int b = 0; b < vi.size(); b++)
        cout << vi[b] << " ";
    cout << endl;
}

int getMin(vector<int> vi) {
    if (vi.size() == 0) return 0;
    
    sort(vi.begin(), vi.end(), greater<int>());
    vector<int> vi1, vi2;
    
    for (int a = 0; a < vi.size(); a++) {
        if (vi[a] - 1 > 0)
            vi1.push_back(vi[a]-1);
    }
    print(vi);
    
    int ans2 = 2000000000;
    if (vi[0] > 3) {
        for (int a = 1; a < vi.size(); a++)
            vi2.push_back(vi[a]);
        if (vi[0] == 9) {
            vi2.push_back(6);
            vi2.push_back(3);
        } else {
            vi2.push_back(vi[0] / 2);
            vi2.push_back(vi[0] - (vi[0] / 2));
        }
        ans2 = getMin(vi2);
    }
    
    return min(getMin(vi1), ans2) + 1;
}

int main() {
    ifstream cin("/Users/byunghoon/Desktop/Programs/Programs/in.txt");
    ofstream cout("/Users/byunghoon/Desktop/Programs/Programs/out.txt");
    
    cin >> T;
    
    for (i = 0; i < T; i++) {
        vector<int> v;
        cin >> D;
        for (j = 0; j < D; j++) {
            cin >> P;
            v.push_back(P);
        }
        
        cout << "Case #" << i+1 << ": " << getMin(v) << endl;
    }
    
    return 0;
}