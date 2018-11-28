#include <bits/stdc++.h>
using namespace std;

int main()
{
	int test;
	int i,j,num1,num2;
	int arr1[4][4];
	int arr2[4][4];
	cin>>test;
	int t;
	for(t=1;t<=test;t++){
		cin>>num1;
		memset(arr1,0,sizeof(arr1));
		memset(arr2,0,sizeof(arr2));
		for(i=0;i<4;i++){
			for(j=0;j<4;j++)
				cin>>arr1[i][j];
		}
		cin>>num2;
		for(i=0;i<4;i++){
			for(j=0;j<4;j++)
				cin>>arr2[i][j];
		}
		int count=0;
		int result = 0;
		for(i=0;i<4;i++)
			for(j=0;j<4;j++)
				if(arr1[num1-1][i]==arr2[num2-1][j]){
					count++;
					result=arr1[num1-1][i];
				}
		if(count==0)
			cout<<"Case #"<<t<<": "<<"Volunteer cheated!"<<endl;
		else if(count>1)
			cout<<"Case #"<<t<<": "<<"Bad magician!"<<endl;
		else if(count==1)
			cout<<"Case #"<<t<<": "<<result<<endl;					
	}
	return 0;
}
