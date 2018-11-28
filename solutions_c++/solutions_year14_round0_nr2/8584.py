#include<iostream>
#include<vector>
#include<set>

#define FOR(i,a,b) for(int i=a; i<b; i++)

using std::cout;
using std::cin;
using std::vector;
using std::set;

int main(){
  
  cout.precision(18);
  int T;
  cin >> T;
  FOR(t,1,T+1) {
    double C,F,X;
    cin>>C;
    cin>>F;
    cin>>X;
    double price, price_prev;
    double cookies, cookies_prev;
    price_prev = 0;
    cookies_prev = 2.0;
    FOR(i,1,200000){
      price = price_prev+C/(2+(i-1)*F);
      cookies = cookies_prev+F;
      double eq = ((price*cookies - price_prev*cookies_prev)/(cookies-cookies_prev) - price_prev)
	  *(cookies_prev);
      if(X<eq) {
	double seconds = price_prev + X/cookies_prev;
	cout << "Case #" << t << ": " << seconds << "\n";
	break;
      }
      price_prev = price;
      cookies_prev = cookies;
    }
  }
  
  return 0;
}