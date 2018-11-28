#include <iostream>
#include <cstring>

using namespace std;

int main(){
	int t, big, len, need;
	int *num;
	string aud;
	cin>>t;
	for(int ord = 1; ord <= t; ord++){
		cin>>big;
		cin>>aud;
		need = 0;
		len = aud.size();
		num = new int[big];
		num[0] = aud[0] - 48;
		for(int i = 1; i < len; i++){
			if(num[i - 1] >= i + 1) num[i] = num[i - 1] + aud[i] - 48;
			else{
				num[i] = i + aud[i] - 48;
				need += i - num[i - 1];
			} 
		}
		cout<<"Case #"<<ord<<": "<<need<<endl;
	}
	return 0;
} 
