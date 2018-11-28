#include <iostream>
using namespace std;

int search(int arr1[4], int arr2[4]){
		int i,j,ans,flag=0;
		for(i=0;i<4;i++){
			for(j=0;j<4;j++){
				if(arr1[i]==arr2[j]){
					flag++;
					ans=arr1[i];
				}
			}
		}
		if(flag==1) {return ans;}
		else if(flag>1) {return 0;}
		else {return -1;}
}

int main() {
	int t,k;
	cin>>t;
	for(k=1;k<=t;k++){
		int first,second,i,j,result,temp;
		int arr1[4],arr2[4];
		cin>>first;
		for(i=0;i<4;i++){
			for(j=0;j<4;j++){
				if(i+1==first){
					cin>>arr1[j];
				}
				else{
					cin>>temp;
				}
			}
		}


		cin>>second;
		for(i=0;i<4;i++){
			for(j=0;j<4;j++){
				if(i+1==second){
					cin>>arr2[j];
				}
				else{
					cin>>temp;
				}
			}
		}

		result = search(arr1,arr2);
		if(result==0){
			cout<<"Case #"<<k<<": Bad magician!\n";	
		}
		else if(result==-1){
			cout<<"Case #"<<k<<": Volunteer cheated!\n";	
		}
		else{
			cout<<"Case #"<<k<<": "<<result<<endl;	
		}
	}
	return 0;
}
