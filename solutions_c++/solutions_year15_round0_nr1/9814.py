#include<iostream>

using namespace std;

int main(){
	int t,k; 
	cin>>t;
	for(int z=0;z<t;z++){
		cin>>k;
		char inp[k+1];
		cin>>inp;
		int standing=0,reqd=0;
		for(int i=0;i<=k;i++){
			if(standing>=i||inp[i]=='0'){
				standing+=(((int)inp[i])-48);
				//cout<<standing<<" "<<reqd<<" "<<i<<endl;
				//cout<<"****  "<<standing<<endl;
				continue;	
			}
			else{
				//cout<<"** "<<standing<<" "<<reqd<<" "<<i<<endl;
				reqd+=(i-standing);
				standing+=reqd;
				standing+=(((int)inp[i])-48);
			}
		}
		cout<<"Case #"<<z+1<<": "<<reqd<<endl;
	}
	return 0;
}
