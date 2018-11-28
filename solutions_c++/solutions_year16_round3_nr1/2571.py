#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>
using namespace std;

int sum = 0;

bool compare(pair<int,int> a, pair<int,int> b){
    return (b.first) < (a.first);
}

int main(){
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t = 0;
    cin >> t;
    for(int i=0; i<t; i++){
        int n = 0;
        cin >> n;
        vector<pair<int,int>> parties(n);
        sum = 0;
        for(int j=0; j<n; j++){
            int x = 0;
            cin >> x;
            parties[j] = {x, j};
            sum += x;
        }
        cout << "Case #" << i+1 << ":";
        while(sum > 0){
            sort(parties.begin(), parties.end(), compare);
            cout << " " << (char)(parties[0].second+65);
            sum--;
            int counter = 0;
            for(int j=0; j<n; j++){
                if(parties[j].first == parties[0].first) counter++;
                else break;
            }
            if(counter%2 == 0){
                cout << (char)(parties[1].second+65);
                parties[1].first--;
                sum--;
            }
            parties[0].first--;
        }
        cout << endl;
    }
    return 0;
}
