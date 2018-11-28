#include<iostream>
using namespace std;
int main() {
	int cases, row, temp,val;
	cin>>cases;
	for(int i=0;i<cases;i++) {
		int a[4],b[4];
		int count=0;
		cin>>row;
		for(int j=0;j<(row-1)*4;j++) {
			cin>>temp;
		}
		for(int j=0;j<4;j++) {cin>>a[j];}
		for(int j=0;j<(4-row)*4;j++) {
			cin>>temp;
		}
		cin>>row;
		for(int j=0;j<(row-1)*4;j++) {
			cin>>temp;
		}
		for(int j=0;j<4;j++) {cin>>b[j];}
		for(int j=0;j<(4-row)*4;j++) {
			cin>>temp;
		}
		for(int k=0;k<4;k++) {
			for(int l=0;l<4;l++) {
				if(a[k]==b[l]) {count++;val=b[l];break;}
			}
		}
		if(count==0) cout<<"Case #"<<i+1<<": "<<"Volunteer cheated!"<<endl;
		else if(count==1) cout<<"Case #"<<i+1<<": "<<val<<endl;
		else cout<<"Case #"<<i+1<<": "<<"Bad magician!"<<endl;
	}
}