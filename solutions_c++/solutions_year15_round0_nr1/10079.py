#include <iostream>
#include <string>
using namespace std;

int main(){
	int n;
	cin >> n;
	
	int len;
	string seats;
	
	for(int i=0;i<n;i++){
		cin >> len >> seats;
		int num = 0, need = 0;
		for(int j=0;j<=len;j++){
			if(num<j && seats[j]!='0'){
				need = need+j-num;
				num = num+need+seats[j]-'0';
			}else{
				num = num+seats[j]-'0';
			}
		}
		cout << "Case #" << i+1 << ": " << need << endl;
	}
	

	return 0;
}
