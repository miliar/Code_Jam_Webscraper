#include<iostream>
#include<algorithm>
#include<cstring>
using namespace std;
long long p, q, t;
long long p2[41];
int main(){
  cin >> t;
  p2[0] = 1;
  for (int  i = 1; i <= 40; ++i) p2[i] = p2[i-1] * 2;
  for (int i = 1; i <= t; i++) {
    scanf("%lld/%lld\n", &p, &q); //cin >> p >> q;
    int j,k=0;
    for (j = 1; (j <= 40)&&(k==0); ++j) {
	    //cout << p2[j] << " " << p << " " << q << endl;
	    long long x = (p2[j]*p/q);
//	    cout << j << ":" << x << endl;
	    k=0;
//	    cout << j <<  ": x=" << x << " xq=" << x*q << " p2p="<< p2[j]*p << endl;
	    if (x*q == p2[j]*p){
//		    cout << "do: " << x << "/" << p2[j] << endl;
		    for (k = 0; k <=j; ++k) {
			    if (p*p2[k]>=q) break;
		    };
            }
    };
    if (j==41) 
      cout << "Case #" << i << ": impossible" << endl;
    else
      cout << "Case #" << i << ": " << k << endl;
  };
};
