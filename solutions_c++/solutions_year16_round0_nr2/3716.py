#include<iostream>

using namespace std;
const int MN=20;
int mark[MN];


int main(){
	int T;
	cin>>T;
	for(int i=0;i<T;i++){
		string x;
		cin>>x;
		int con=0;
		if(x[0]=='-'){
			con++;
		}
		for(int i=0;i<x.size()-1;i++){
			if(x[i]=='+'&&x[i+1]=='-'){
				con+=2;
			}
		}
		cerr<<x<<endl;
		cout<<"Case #"<<i+1<<": "<<con<<endl;
	}
}

			
		
