#include<iostream>
using namespace std;
void f(){
	int ans,x;
	int ok[16];
	for(int i=0;i<16;i++)ok[i]=0;
	for(int k=0;k<2;k++){
		cin>>ans;
		for(int i=1;i<=4;i++){
			for(int j=1;j<=4;j++){
				cin>>x;
				ok[x-1]+=(ans==i);
			}
		}
	}
	int iledw=0,dw;
	for(int i=0;i<16;i++){
		if(ok[i]==2){iledw++;dw=i;}	
	}
	if(iledw>1){cout<<"Bad magician!\n";return;}
	if(iledw==0){cout<<"Volunteer cheated!\n";return;}
	cout<<dw+1<<"\n";
}
main(){
	int t;
	cin>>t;
	for(int i=0;i<t;i++){
		cout<<"Case #"<<i+1<<": ";
		f();
	}
}
