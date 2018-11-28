#include<bits/stdc++.h>
#include <algorithm>
#include <string>
#include <vector>

int max_limit = 2500;
using namespace std;
void rank_file(std::vector<int> v){
     vector<int> v1;
     for(int i = 0; i < max_limit; i++)
        if (v[i] == 1) v1.push_back(i);

     sort(v1.begin(), v1.end());
     int x = v1.size() - 1;
     for(int i = 0; i < x; i++)
        cout << v1[i] << " ";
     cout << v1[x];
}
int main(){
    int T, N, x, y;
    cin >> T;
    int i = 0;
    while (i < T){
        i++;
        cin >> N;
        vector<int> v(max_limit, 0);
        y = (2*N*N) - N;
        for(int i = 0; i < y; i++){
            cin >> x;
            v[x] = v[x] ^ 1;
        }
        cout << "Case #" << i << ": ";
        rank_file(v);
        cout << endl;
    }
    return 0;
}
