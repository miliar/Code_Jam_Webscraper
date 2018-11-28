#include <iostream>
#include <fstream>
#include <map>
#include <iomanip> 

using namespace std;

int main(){
	freopen("p2.in","r",stdin);
	freopen("p2.out","w",stdout);
	
	int t;
	cin >> t;
	int tc = 1;
	while(t--){
		double c,f,x;
		cin >> c >> f >> x;
		double rate = 2;
		double ans = 10e30;
		double time = 0;
		while(true){
			if(ans > time + x/rate){
				ans = time + x/rate;
			}else{
				cout << setprecision(7) << fixed << "Case #" << tc++ << ": " <<  ans << endl;
				break;
			}
			time += c/rate;
			rate += f; 
		}
		
	}
}

