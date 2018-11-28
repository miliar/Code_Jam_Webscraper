#include<iostream>
using namespace std;

int main()
{
	int ans[102];
	int numcases;
	cin >> numcases;
	for(int k = 0; k < numcases; k++){
		int smax;
		cin >> smax;
		string str;
		cin >> str;
		
		int total = 0;
		int need = 0;
		for(int i = 0; i <= smax; i++){
			if(str[i] == '0'){
				continue;
			}
			int temp = str[i] - '0';
			if(i == 0){
				total = temp;
				continue;
			}
			if(total >= i){
				total += temp;
			} else{
				int diff = i - total;
				need += diff;
				total += diff;;
				total += temp;
			}
		}
		ans[k] = need;
	}
	for(int k = 0; k < numcases; k++){
		cout << "Case #" << k+1 << ": "<< ans[k]<<endl;
	}

}
