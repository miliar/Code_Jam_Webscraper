#include<iostream>
#include<vector>
#include<string> 

using namespace std;

int main() {
  int t;
  cin >> t;
  //cout << "t =" << t << endl;
  for (int i=0; i<t; i++) {
    int ans = 0;
    int  num = 0;
    int smax = 0;
    cin >> smax;
    //cout << "smax =" << smax << endl;
    string inp;
    cin >> inp;
    num=inp[0]-'0';
    for (int j=1; j<=smax;j++) {
      //cout <<ans << endl;
      if (num+ans < j) {
	ans = (j-num);
      }
      //cout << ans << endl;
      num+=(inp[j]-'0');
      if (num >= smax)
	break;
    }
    cout << "case #" << i+1 << ": " << ans <<endl;
  }
  return 0;
}
