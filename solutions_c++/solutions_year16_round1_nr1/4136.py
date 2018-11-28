#include <iostream>
#include <cstdio>
using namespace std;

int main(){
	freopen("in.txt","r",stdin);
	long long T,N;
	cin>>T;
	for(int i=0;i<T;i++){
		string input,result;
		char tmp[2]="\0";
		cin>>input;
		tmp[0]=input[0];
		tmp[1]='\0';
		result = tmp;
		for(int i=1;i<input.length();i++){
			tmp[0]=input[i];
			tmp[1]='\0';
			if(tmp[0]>= result[0]){
				result = tmp + result;
			}else{
				result += tmp;
			}
		}
		cout<<"Case #"<<i+1<<": ";
		cout<<result<<endl;
	}
	return 0;
}