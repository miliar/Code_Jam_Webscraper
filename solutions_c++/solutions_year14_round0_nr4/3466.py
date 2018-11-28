#include <iostream>
#include <string>
#include <set>
#include <queue>
#include <algorithm>

using namespace std;

const int MAX_WEIGHT = 1;

int main(int argc, char** argv) {
  int ntc;
  cin>>ntc;
  for(int tc=1;tc<=ntc;++tc) {
    int t;
    cin>>t;
    vector<double> k1;
    set<double> n1;
    vector<double> n2;
    set<double> k2;
    for(int i=0;i<t;++i) {
      double b;
      cin>>b;
      n1.insert(b);
      n2.push_back(b);
    }
    sort(n2.rbegin(), n2.rend());
    for(int i=0;i<t;++i) {
      double b;
      cin>>b;
      k1.push_back(b);
      k2.insert(b);
    }
    sort(k1.begin(), k1.end());

    // Play war
    int war=0;
    for(int i=0;i<t;++i) {
      double n = n2[i];
      // Find best
      double closest = MAX_WEIGHT;
      double smallest = MAX_WEIGHT;
      for(auto j = k2.begin(); j!= k2.end(); ++j) {
        if(*j < smallest) {
          smallest = *j;
        }
        if(*j < closest && *j > n) {
          closest = *j;
        }
      }
      if(closest!=MAX_WEIGHT && closest > n) {
        k2.erase(closest);
      } else {
        k2.erase(smallest);
        war++;
      }
    }

    // Play D-war
    int dwar = 0;
    for(int i=0;i<t;++i) {
      double k = k1[i];
      // Find best
      double closest = MAX_WEIGHT;
      double smallest = MAX_WEIGHT;
      for(auto j = n1.begin(); j!= n1.end(); ++j) {
        if(*j < smallest) {
          smallest = *j;
        }
        if(*j < closest && *j > k) {
          closest = *j;
        }
      }
      if(closest!=MAX_WEIGHT && closest > k) {
        n1.erase(closest);
        dwar++;
      } else {
        n1.erase(smallest);
      }
    }

    cout<<"Case #"<<tc<<": "<<dwar<<" "<<war<<endl;
  }
}
