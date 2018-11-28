#include <iostream>
#include <cstring>

using namespace std;

int main(){
	int n;
	cin >> n;
	for(int j = 1; j <= n; j ++){
		int m;
		cin >> m;
		int num[m + 1];
		string str;
		cin >> str;
		for(int i = 0; i <= m; i ++){
			num[i] = str[i] - 48;
		}
		int ext = 0;
		int sumOfAud = 0;
		for(int i = 0; i <= m; i ++){
			
			if(i > sumOfAud){
				ext += i - sumOfAud;
				sumOfAud += i - sumOfAud;
			}
			sumOfAud += num[i];	
			
		}
		cout<<"Case #"<<j<<": "<<ext<<endl;
	}
	return 0;
}
