#include<iostream>
using namespace std;
int main(){
	int T, r1, r2;
	int arr1[4][4], arr2[4][4];
	int i,j,temp,n,temp1;
	cin>>T;
	for(n=1; n<=T; n++){
		temp=0;
		cin>>r1;
		for(i=0; i<4; i++){
			for(j=0; j<4; j++){
				cin>>arr1[i][j];
			}
		}
		cin>>r2;
		for(i=0; i<4; i++){
			for(j=0; j<4; j++){
				cin>>arr2[i][j];
			}
		}
		for(i=0; i<4; i++){
			for(j=0; j<4; j++){
				if(arr1[r1-1][i]==arr2[r2-1][j]){
					if(temp==0)
						temp1=arr1[r1-1][i];
					temp++;
				}
			}
		}
		if(temp==1)
			cout<<"Case #"<<n<<": "<<temp1<<endl;
		else if(temp>1)
			cout<<"Case #"<<n<<": Bad magician!"<<endl;
		else
			cout<<"Case #"<<n<<": Volunteer cheated!"<<endl;
	}
	return 0;
}
