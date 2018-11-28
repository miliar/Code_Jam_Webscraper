#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
//#define PI 3.14159265358979323846264338327950288419716939937510

using namespace std;

int main() {
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("aa.txt", "w", stdout);
	long long n;
	cin>>n;
	long long R,T;
	long double r,t;
	for (long long i=0; i<n; i++) {
		cin>>R>>T;
		r = (long double)R;
		t = (long double)T;
		long long res = 0;
		long long aa;
//		while (t*PI>=(aa=((R+1)*(R+1)*PI-R*R*PI))) {
		while (T>=(aa=((R+1)*(R+1)-R*R))) {
			T-=aa;
			R+=2;
			res++;
		}
		cout<<"Case #"<<i+1<<": "<<res<<'\n';
	}
	return 0;
}