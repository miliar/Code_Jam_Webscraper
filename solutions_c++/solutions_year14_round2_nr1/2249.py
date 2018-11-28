#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <climits>
#include <vector>
#include <iterator>
#include <set>
#include <bitset>
#include <ctime>
#include <iomanip>
#include <map>

using namespace std;

vector<pair<char, int> > breakintoparts(string x);
 
int main() {
    int t;
    cin>>t;
 
    for(int i = 0; i < t; i++) {
            cout<<"Case #"<<i+1<<": ";
            int N;
            int ans = 0;
            cin>>N;
            vector<vector<pair<char, int> > > toBeFixed;
            for(int j = 0; j < N; j++) {
                    string x;
                    cin>>x;
                    toBeFixed.push_back(breakintoparts(x));
            }
            for(int j = 1; j < N; j++) {
                    if(toBeFixed[j].size() != toBeFixed[0].size()) {
                         goto Fegla;
                    }
                    for(int k = 0; k < toBeFixed[j].size(); k++) {
                            if(toBeFixed[j][k].first != toBeFixed[0][k].first) goto Fegla;
 
                    }
            }
 
            for(int j = 0; j < toBeFixed[0].size(); j++) {
                    int sum = 0;
 
                    for(int k = 0; k < N; k++) sum += toBeFixed[k][j].second;
 
                    sum = sum / N  + (2*(sum % N) > N);
 
                    int minimal = 0;
 
                    for(int k = 0; k < N; k++) minimal += abs(toBeFixed[k][j].second - sum);
 
                    ans += minimal;
 
            }
 
            cout << ans << endl;
 
            continue;
 
            Fegla:
            cout << "Fegla Won" << endl;
    }
    return 0;
}
 
vector<pair<char, int> > breakintoparts(string x) {
     vector< pair<char, int> > result;
     int counter = 1;
     for(int k = 0; k < x.size(); k++) {
          if(k < x.size()-1 && x[k] == x[k+1]) {
               counter++;
          }
          else {
               result.push_back(make_pair(x[k], counter)); 
               counter = 1;
          }            
     }             
     return result;
}