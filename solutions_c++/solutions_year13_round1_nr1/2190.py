#include <iostream>
#include <cmath>
using namespace std;
#define ll long long

int main(){
	#ifndef ONLINE_JUDGE
   freopen("input.txt", "rt", stdin);
   freopen("output.txt", "wt", stdout);
	#endif
	ll n, r, t, ch = 0, temp;
	scanf("%lld", &n);
	for(int i = 0; i< n; i++){
			scanf("%lld %lld", &r , &t);
			while(t > 0){
				temp = pow((r + 1), 2)- r*r;
				if(t >= temp){
					ch++;
					r += 2;
					t -= temp;
				}
				else{
					break;
				}
			}
			cout << "Case #" << i+1 << ": " << ch << endl;
			ch = 0;
		}		
}