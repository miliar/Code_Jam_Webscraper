#include <iostream>
using namespace std;
int main(){
	int t;
	cin >> t;
	for(int q = 0; q < t;q++){
		int a,b,k,total=0;
		cin >> a >> b >> k;
		for (int i = 0; i < a; ++i)
		{
			for (int j = 0; j < b; ++j)
			{
				if((i&j)<k){
					total++;
				}
			}
		}
		cout << "Case #" << q+1 << ": " << total << endl;
	}
}