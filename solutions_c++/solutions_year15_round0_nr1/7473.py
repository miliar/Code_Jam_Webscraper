#include <iostream>
#include <cstdlib>
using namespace std;

int main() {
	int t;
	cin >> t;
	int j;
	for(j=1;j<=t;j++){
		int n;
		cin >> n;
		char st[n+1];
		cin >> st;
		int i;
		int sum,total,k;
		sum = st[0]-'0';
		total = 0;
		for(i=1;i<n+1;i++){
		
			if(sum<i&&st[i]-'0'!=0){
				total += i-sum;
				sum += i - sum;
			}
			sum += st[i]-'0';
		}
		cout <<"Case #"<<j<<":"<<" "<< total << endl;
	}
	return 0;
}
