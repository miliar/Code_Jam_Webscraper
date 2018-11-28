#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <math.h>
using namespace std;

bool isPolindrom (const __int64 num) {
	__int64 newx = 0;
	__int64 x = num;
	while (x>0){
		newx = newx*10 + x%10;
		x = x/10;
	}
	return (num == newx);
}
int main() {
	//int count = 0;
	vector<__int64> P;
	for (int i = 1 ; i <= 1000*1000*10; ++i) {
		if (isPolindrom(i)) {
			//count ++;
			__int64 k = __int64(i)*__int64(i);
			if (isPolindrom(k)){
				P.push_back(k);
				//cout<<k<<endl;
			}
		}
	}
	//cout << count << " " << P.size();;
	int T;

	cin >> T;
	
	for (int i = 1; i<= T; ++i) {
		__int64 A, B;
		cin >> A >> B;
		int count = 0; 
		for (int i = 0; i<P.size(); ++i) {
			if ((P[i]>=A)&&(P[i]<=B)){
				count ++;
			}
		}
		cout << "Case #" << i <<": "<< count << endl;
	}
	return 0;
}