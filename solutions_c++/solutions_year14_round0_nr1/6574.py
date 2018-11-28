#include<iostream>
#include<fstream>
using namespace std;
int main()
{ifstream cin("a.in");
	ofstream cout("a.txt");
	int t,a[4][4],r1,r2,b[4][4],i=0,j,k=0,m,x;
	cin>>t;
	m=t;
	while(t--){k=0;
		cin>>r1;
		for(i=0;i<4;i++){
			for(j=0;j<4;j++)
			cin>>a[i][j];
		}
		cin>>r2;
        for(i=0;i<4;i++){
			for(j=0;j<4;j++)
			cin>>b[i][j];
		}
		
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++){
		//	cout<<a[r1][i]<<"   "<<b[r2][j];
			if(a[r1-1][i]==b[r2-1][j]){
			k++;
			x=a[r1-1][i];
		}
	}}if(k==1){
cout<<"Case #"<<m-t<<": "<<x<<endl;
	}
	else if(k==0)
cout<<"Case #"<<m-t<<": "<<"Volunteer cheated!"<<endl;
else
cout<<"Case #"<<m-t<<": "<<"Bad magician!"<<endl;
}return 0;}

