#include <iostream>

using namespace std;

inline int cal(int max,string str){
	int sum=0,num=0;
	// cout<<"max : "<<max<<endl;K
	if(str[0] == '0'){
		sum++;
		num += 1;
	}
	num += str[0] - '0';

	for(int i=1;i<=max;i++){
		int curr = str[i]-'0';
		if(curr !=0 && num < i){
			int step = i-num;
			sum+=step;
			num+=step;
		}
		num += curr;

	}

	return sum;

}

int main(){
	int T;
	cin>>T;

	for(int i=0;i<T;i++){
		int max;
		string str;
		cin>>max>>str;

		int out = cal(max,str);
		cout<<"Case #"<<(i+1)<<": "<<out<<endl;
	}
}