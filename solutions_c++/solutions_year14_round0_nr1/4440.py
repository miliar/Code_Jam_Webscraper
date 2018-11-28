#include<iostream>

using namespace std;

int main(){
	int  a[4][4], b[4][4],t,i,j,n,m,c=1;
	int ans;
	cin>>t;
	while(t--){
		int k=-1;
		cin>>n;
		for(i=0;i<4;i++){
			for(j=0;j<4;j++)
			cin>>a[i][j];
		}
		cin>>m;
		for(i=0;i<4;i++){
			for(j=0;j<4;j++)
			cin>>b[i][j];
		}
		n--;m--;
		for(i=0;i<4;i++){
			for(j=0;j<4;j++){
				if (a[n][i]==b[m][j]){
					k++;
					if(k==0)
					ans=a[n][i];
				}
				
			}
			
		}
		if (k>0)
		cout<<"Case #"<<c++<<": Bad magician!"<<endl;
		else if (k==0)
		cout<<"Case #"<<c++<<": "<<ans<<endl;
		else if(k==-1)
		cout<<"Case #"<<c++<<": Volunteer cheated!"<<endl;
		
	}
	return 0;
}
