#include<iostream>
using namespace std;
int main(){
	int t,n,j;
	cin>>t>>n>>j;
	string base="1000000000000001";
	string s[10]={base,"3","2","5","2","7","2","3","2","11"};
	int odd[7]={1,3,5,7,9,11,13},even[7]={2,4,6,8,10,12,14};
	cout<<"Case #1:\n";
	for(int k=0;k<10;k++){
		if(k==9) cout<<s[k]<<endl;	
		else cout<<s[k]<<" ";
	}
	for(int i=0;i<7;i++){
		for(int j=0;j<7;j++){
			s[0]=base;
			s[0][15-odd[i]]='1';
			s[0][15-even[j]]='1';
			for(int k=0;k<10;k++){
				if(k==9) cout<<s[k]<<endl;	
				else cout<<s[k]<<" ";
			}
		}
	}
	return 0;
}

