#include <iostream>
using namespace std;
typedef long long int lli;

int main(){
	int t;
	cin >> t;
	lli n;
	int ok = 0x3ff;
	for(int i=1;i<=t;i++){
		cin >> n;
		cout << "Case #"<<i<<": ";
		if(n == 0){
			cout << "INSOMNIA" << endl;
			continue;
		}
		int status = 0;
		int num = 0, count = 0;
		while(status != ok){
			num+=n;
			int temp = num;
			while(temp){
				int bit = temp%10;
				status = status|(1<<bit);
				temp/=10;
			}
			count++;
		}
		cout << num  << endl;
	}
	return 0;
}
