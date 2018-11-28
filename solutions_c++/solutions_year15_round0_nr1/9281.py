#include<iostream>
#include<string>
#include<vector>
#include<algorithm>

using namespace std;


int main(){
  int T,Smax,tmp;
  char tmpc;
  cin >> T;
  for (int i = 0; i < T; i++){
    cin >> Smax;
    vector<int> Si;
    int nb_applaud = 0;
    int res=0;
    for (int j = 0; j <= Smax; j++){
      cin >> tmpc;
//      cout << tmpc << "\n";
      tmp = tmpc - '0';
//      cout << tmp << "\n";
//      if (i == 2) {
//        cout << "nb_applaud = " << nb_applaud << "\n";
//        cout << "j = " << j << "\n";
//      }      
      if (nb_applaud < j){
	res++;
	nb_applaud++;
//	if (i == 2) {cout << "1 spectator added\n";}
      }
      nb_applaud += tmp;
    }
    cout << "case #" << i+1 << ": " << res << "\n";
  }
  return 0;
}
