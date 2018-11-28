#include <iostream>
#include <vector>
#include <algorithm>
#include <functional>
#include <cstdio>
#include <map>
#include <string>
#include <set>
#include <string.h>
#include <iomanip>
using namespace std;
const int inf = 1e9;
int main(){
  freopen("input.txt", "r", stdin);
  int T;
  cin>>T;
  for(int times = 1; times <= T; times++){
    double c, f, x;
    cin>>c>>f>>x;
    double cookies = 0;
    double seconds = x / 2;
    vector<double> rates;
    int cnt = 0;
    for(double rate = 2; cnt < 100000; rate += f, cnt++){
      rates.push_back((double)(c / rate));
    }
    double rate = 2;
    double total = 0;
    for_each(rates.begin(), rates.end(),[&total,&rate, &f, &seconds, &x](double & sp){
	total += sp;
	rate += f;
	double rest = x / rate;
	if(rest + total < seconds)seconds = rest + total;
      });
    cout<<std::fixed;
    cout.precision(7);
    cout<<"Case #"<<times<<": "<<seconds<<endl;
  }
  return 0;
}
