#include <iostream>
using namespace std;

int main(){
	int t;cin>>t;
	for(int w=0;w<t;w++){
		int first[4],sec[4];
		int a;cin>>a;
		int g[4][4];
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				cin>>g[i][j];
			}
		}
		/*
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				cout<<g[i][j]<<" ";
			}
			cout<<endl;
		}
		cout<<endl;
		*/
		for(int i=0;i<4;i++)first[i]=g[a-1][i];
		int b;cin>>b;
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				cin>>g[i][j];
			}
		}
		/*
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				cout<<g[i][j]<<" ";
			}
			cout<<endl;
		}
		cout<<endl;
		*/
		for(int i=0;i<4;i++)sec[i]=g[b-1][i];
		int c=0,ans;
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				if(first[i]==sec[j]){
					c++;
					ans=first[i];
				}
			}
		}
		if(c==0){
			cout<<"Case #"<<w+1<<": Volunteer cheated!"<<endl;
		}
		else if(c==1){
			cout<<"Case #"<<w+1<<": "<<ans<<endl;
		}
		else{
			cout<<"Case #"<<w+1<<": Bad magician!"<<endl;
		}
	}
}
