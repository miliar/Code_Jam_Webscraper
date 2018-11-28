#include <iostream>
#include <string>
using namespace std;
void output(int i,int a){
	cout<<"Case #"<<i<<": "<<a<<endl;
}
int main(){
	int t;
	string n[101];
	cin>>t;
	for(int i=1;i<=t;i++){
		cin>>n[i];
	}
	for(int i=1;i<=t;i++){
		int tmp=0;
		int j=n[i].length();
		while(j--){
			if(n[i][j]=='-'){
				int k =j;
				while(k--)n[i][k]=n[i][k]=='-'?'+':'-';
				tmp++;
			}
		}
		output(i,tmp);
	}
	return 0;
}

