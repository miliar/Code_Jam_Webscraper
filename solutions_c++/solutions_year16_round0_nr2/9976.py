#include<iostream>
using namespace std;
string rever(string aa,int pos){
	string b=aa;
	for(int i=0;i<=pos;i++){
		if(b[i]=='-')
			b[i]='+';
		else {

			b[i]='-';
		}
	}
	return b;
}

int main(){
	int test;
	string a;
	cin>>test;
	for(int i=1;i<=test;i++){
		cin>>a;
		int cnt=0;
		int siz=a.size();
		for(int j=siz-1;j>=0;j--)
		if(a[j]=='-'){
				cnt++;
			a=rever(a,j);
		//cout<<cnt<<"  "<<a<<" "<<endl;
		}
		cout<<"Case #"<<i<<": "<<cnt<<endl;
	}
}

