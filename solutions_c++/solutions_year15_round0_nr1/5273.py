#include <iostream>
#include <string>
using namespace std;
string a;
int main(){
	freopen("f.txt","r",stdin);
	freopen("fout.txt","w",stdout);
	int t,smax,s = 0,c = 0,x = 1;
	cin >> t;
	while(t--){
		cin >> smax;
		s = 0,c = 0;
		cin >> a;
		for(int i = 0; i <= smax; i++){
			
			
			if(s < i){
				c += i - s;
				s += i - s;
			}
			s += a[i] - '0';
		}
		cout << "Case #" << x << ": " << c << '\n';
		x++;
	}


	return 0;
}