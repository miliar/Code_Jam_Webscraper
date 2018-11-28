#include <iostream>
using namespace std;

int num10, list[10];

int main(void) {
	int x, y;
	cin >> x;
	for(int i=0;i<x;i++){
		cin >> y;
		cout << "Case #" << i+1 << ": ";
		if(y == 0){
			cout << "INSOMNIA" << endl;
			continue;
		}
		for(int j=0;j<10;j++) list[j] = 1;
		num10 = 10;

		int yy = y;
		while(num10){
			int yyy = yy;
			while(yyy){
				if(list[yyy%10]){
					list[yyy%10] = 0;
					num10--;
				}
				yyy/=10;
			}
			if(num10==0) break;
			yy += y;
		}
		cout << yy << endl;
	}
	return 0;
}


