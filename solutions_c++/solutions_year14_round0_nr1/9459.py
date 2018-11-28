#include<iostream>
using namespace std;

int match(int a[],int b[],int l){
	int p,i,j;int count=0;
	for(i=0;i<4;i++){
			for (j=0;j<4;j++)
			if (a[i]==b[j]){
				count++;
				p = a[i];
			} 
	}
	if (count>1) cout<<"Case #"<<l<<": "<<"Bad magician!"<<"\n";
	if(count==0) cout<<"Case #"<<l<<": "<<"Volunteer cheated!"<<"\n";
	if (count==1) cout<<"Case #"<<l<<": "<<p<<"\n";
		
}









int main(){
	int t,b[4][4];
	int a[4][4];
	int x,y,i,j,ans;
	cin>>t;
	int l=0;
	while(t--){
		cin>>x;x--;
		for(i=0;i<4;i++){
			for (j=0;j<4;j++)
			cin>>a[i][j];
		}
		cin>>y;y--;
		for(i=0;i<4;i++){
			for (j=0;j<4;j++)
			cin>>b[i][j];
		}
		l++;
		ans = match(a[x],b[y],l);
		
	}
}


