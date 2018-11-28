#include <iostream>
#include <vector>
#include <deque>

using namespace std;

int ctoi(char c) {
  return c - '0';
}

int solve2(const vector<int> ds) {
  int max1 = *max_element(ds.begin(), ds.end());
  int min1 = max1;
  int sum;
  for(int i = 1; i <= max1; i++) {  
    sum = i;
    for(int j = 0 ; j < ds.size() ; j++) {  
      if(ds[j] > i) {  
	if(ds[j] % i == 0 )  
	  sum += (ds[j]/i-1) ;  
	else  
	  sum += (ds[j]/i) ;  
      }
    }
    min1 = min(min1,sum);
  }
  return min1;
}

// int solve(deque<int> &ds) {
//   int time = 0;
//   if (ds.size() == 0) {
//     return 0;
//   } else if (ds.size() % 2 == 1) {
//     ds.pop_front();
//     return 1 + solve(ds);
//   } else { //if (ds[ds.size() - 1] < ds.size()/2) {
//     deque<int> ds1 = ds;
//     deque<int> ds2 = ds;

//     if (ds1.size() % 2 == 0) {
//       ds1[ds1.size()/2 - 1] += 2*ds1[ds1.size()-1];
//     } else {
//       ds1[ds1.size()/2 - 1] += ds1[ds1.size()-1];
//       ds1[ds1.size()/2] += ds1[ds1.size()-1];
//     }
//     int t1 = time + ds1[ds1.size()-1];
//     ds1.pop_back();
//     t1 += solve(ds1);

//     int t2 = time + ds2.size()/2;
//     ds2.erase(ds2.begin(), ds2.begin() + ds2.size()/2);
//     t2 += solve(ds2);

//     return min(t1, t2);
//   }
// }

int main(int argc, char *argv[]) {
 
  int t;
  cin >> t;
  for (int i = 1; i <= t; i++) {
    int n;
    cin >> n;
    vector<int> ns;
    int max_d = 0;
    for (int j = 0; j < n; j++) {
      int d;
      cin >> d;
      ns.push_back(d);
      if (max_d < d) {
	max_d = d;
      }
    }

    // deque<int> ds(max_d, 0);
    // for (int d : ns) {
    //   ds[d-1]++;
    // }


    cout << "Case #" << i << ": " << solve2(ns) << endl;
  }
}
