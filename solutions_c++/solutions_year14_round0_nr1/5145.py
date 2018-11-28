#include <iostream>

/* run this program using the console pauser or add your own getch, system("pause") or input loop */
using namespace std;
int main() 
	{
	int t,i,j,r1,r2;
	int arr1[5][5],arr2[5][5];
	cin>>t;
	int u=1;
	while(t--){
	
		int comm,count=0,p;
	cin>>r1;
	for(i=1;i<=4;i++)
	{
		for(j=1;j<=4;j++)
		cin>>arr1[i][j];
	}
	cin>>r2;
	for(i=1;i<=4;i++){
		for(j=1;j<=4;j++)
		cin>>arr2[i][j];
	}
	for(j=1;j<=4;j++){
		p=arr1[r1][j];
		for(int k=1;k<=4;k++){
			if(arr2[r2][k]==p){
			count++;
			comm=arr2[r2][k];
			break;
		}
			
		}
	}
	if(count==1)
	cout<<"Case #"<<u<<": "<<comm<<"\n";
	else if(count==0)
	cout<<"Case #"<<u<<": "<<"Volunteer cheated!"<<"\n";
	else
	cout<<"Case #"<<u<<": "<<"Bad magician!"<<"\n";
	u++;
}
	return 0;
}