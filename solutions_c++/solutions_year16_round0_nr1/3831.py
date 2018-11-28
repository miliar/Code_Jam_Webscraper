#include <iostream>
#include <cmath>
using namespace std;
int main(){
	int T;
	cin >> T;
	long long n,cef;
	int found;
	bool a[10];
	for(int t = 1;t <= T;t ++){
		for(int i = 0;i < 10;i ++){
			a[i] = false;
		}
		cin >> n;
		cout << "Case #" << t << ": ";
		if(n == 0){
			cout << "INSOMNIA" << endl;
			continue;
		}
		cef = 1;
		found = 0;
		while(true){
			for(int q = n * cef;q > 0;q /= 10){
				int w = q % 10;
				if(!a[w]){
					a[w] = true;
					found ++;
				}
				if(found == 10) break;
			}
			if(found == 10) break;
			cef ++;
		}
		cout << n * cef << endl;
	}
	
	
	return 0;
}
