#include<iostream>
using namespace std;

int main(){	
	int t,i,j;
	cin>>t;
	int ans[t];
	for(i=0;i<t;i++){
		int k,c,s;
		cin>>k>>c>>s;
		ans[i]=k;
	}
	for(i=0;i<t;i++){
		cout<<"Case #"<<i+1<<": ";
		for(j=1;j<=ans[i];j++){
				cout<<j<<"\t";
			}	
		cout<<endl;
	}
return 0;
}
