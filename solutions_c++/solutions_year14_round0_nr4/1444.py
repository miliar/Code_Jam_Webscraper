#include<iostream>
#include<vector>
#include<set>
#include<algorithm>
#include<math.h>
#include<stdio.h>
#define ll long long

bool desc_sort(double i, double j)
{
  return(i>j);
}

using namespace std;

int main()
{
  int T;
  cin >> T;
  for(int tc=1; tc <= T; ++tc){
    int N;
    cin >> N;
    set<double> Naomi, Ken;
    for(int i = 0; i < N; ++i){
      double t;
      cin >> t;
      Naomi.insert(t);
    }
    for(int i = 0; i < N; ++i){
      double t;
      cin >> t;
      Ken.insert(t);
    }
    set<double> Ken_temp(Ken.begin(), Ken.end());
   
    set<double>::iterator k ;
    int wPoints=0, dPoints=0;
    for(set<double>::iterator n = Naomi.begin(); n != Naomi.end(); ++n){
      //cout << "lol" << endl;
      if(*n < *(Ken_temp.begin())){
	//Ken_temp.pop_back();
	k = Ken_temp.end();
	--k;
	Ken_temp.erase(k);
      }
      else{
	k = Ken_temp.upper_bound(*n);
	k--;   // highest element lesser than *n
	Ken_temp.erase(k);
	++dPoints;
      }
    }
    
    for(set<double>::reverse_iterator n = Naomi.rbegin(); n != Naomi.rend(); ++n){
      set<double>::iterator k = Ken.upper_bound(*n);
      if(k == Ken.end()){
	++wPoints;
	Ken.erase(Ken.begin());
      }
      else{
	Ken.erase(k);
      }
      //cout << "lol" << endl;
    }
    cout << "Case #" << tc << ": " << dPoints << " " << wPoints << endl;
  }
  return 0;
}
