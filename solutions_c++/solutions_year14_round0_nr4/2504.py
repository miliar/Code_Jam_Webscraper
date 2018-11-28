#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <string>
#include <iomanip>
#include <deque>
using namespace std;

bool compare (double a, double b) {
  return (a > b);
}

int main(){
  ifstream input;
  ofstream output;

  string file;
  cin >> file;
  input.open(file);
  output.open("output.out");

  cout << fixed;
  output << fixed;

  int t, n; 
  input >> t;
  double maxv, maxi;
  double tmp;
  int temp, ans1, ans2, ans3;
  for (int k = 1; k <= t; k++){
    deque<double> a1;
    deque<double> a2;
    ans1 = 0;
    ans2 = 0;
    ans3 = 0;
    input >> n;
    for (int i = 0; i < n; i++){
      input >> tmp;
      a1.push_back(tmp);
    }
    for (int i = 0; i < n; i++){
	input >> tmp;
	a2.push_back(tmp);
    }
    sort(a1.begin(), a1.end(), compare);
    sort(a2.begin(), a2.end(), compare);
    maxv = a2[0];
    maxi = 0;
    for (int i = 0; i < n; i++)
      cout << a1[i] << " ";
    cout << endl;
    for (int i = 0; i < n; i++)
      cout << a2[i] << " ";
    cout << endl;


    for (int i = 0; i < n; i++){
      if (a1[i] > maxv){
	ans1++;
      } else {
	maxi++;
	maxv = a2[maxi];
      }
    }
    for (int i = 0; i < n; i++){
      cout << "\t" << a1[a1.size()-1] << " " << a2[a2.size()-1] << endl;

      if (a1[a1.size()-1] <  a2[a2.size()-1]){
	a2.pop_front();

      } else {
	a2.pop_back();
	ans3++;
      }
	a1.pop_back();
    }
    cout << "Case #" << k << ": " <<ans3<< " " << ans1 << endl;
    output << "Case #" << k << ": " << ans3<< " " << ans1 << endl;
  }
  return 0;
}


    

