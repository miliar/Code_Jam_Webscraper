#include<iostream>
using namespace std;
int main(){

	long int tt;
	long int t,r,rb,rw,area;
	long int count = 1, ans;
	long double bp;
	cin >> tt;
	while(tt){
		cin >> r >> t;
		rw = r; rb = r+1;
		bp = t;
		ans = 0;
		while(bp > 0){
			area = (rb*rb) - (rw*rw);
			bp = bp - area;
			rb = rb+2;
			rw = rw+2;
			if(bp >= 0)
				ans++;
		}

		cout << "Case #"<<count <<": " << ans <<endl;
		tt--;count++;
	}



	return 0;
}
