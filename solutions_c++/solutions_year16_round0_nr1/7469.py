#include "iostream"
#include <string> 


using namespace std;

int getMax(int N){
	if(N==0){return -1;}
	string out="0000000000";
	for(int j=0;j<1000;j++)
	{
	int NN=(j+1)*N;
	char buffer [33];
	itoa(NN,buffer,10);
	string str = string(buffer);

	for(int i=0;i<str.length();i++){
		int selected=str.at(i)-48;
		out.at(selected)='1';
		if(out=="1111111111")return NN;
	}
	}

	return -1;
}
int main(){
	int T;
	cin>>T;
	if(T<0||T>200){return 0;}

	for(int i=1;i<=T;i++){
		int N;
		cin>>N;
		int r=getMax(N);
		if(r!=-1){
		cout<<"Case #"<<i<<": "<<r<< endl;	;
		}else{
		cout<<"Case #"<<i<<": "<<"INSOMNIA"<< endl;	;
		}
	}
	return 0;
}