#include<iostream>

using namespace std;


int main(){

	int t,f,s;
	cin>>t;
	int k=1;
	while(k<=t){
		cin>>f;
		int a[4][4];
		int count[17]={0};
		for(int i=0;i<4;++i){
			for(int j=0;j<4;++j){

				cin>>a[i][j];
				if(i+1==f) { count[a[i][j]]++;}
			}

		}
		cin>>s;
		
		int cnt=0,no=-1;
		int temp;
		for(int i=0;i<4;++i){
			for(int j=0;j<4;++j){
			cin>>temp;
			if(i+1==s)
			if(count[temp]>0) { ++cnt;no=temp;}

			}
		}
		
		cout<<"Case #"<<k<<": ";
		if(cnt==1) cout<<no<<endl;
		else if(cnt==0) cout<<"Volunteer cheated!"<<endl;
		else cout<<"Bad magician!"<<endl;

		++k;

	}



}
