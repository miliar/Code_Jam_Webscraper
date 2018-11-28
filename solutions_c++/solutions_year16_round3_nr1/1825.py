#include<bits/stdc++.h>
using namespace std;

int main(){
	int t;
	cin>>t;
	for(int q=1;q<=t;q++){
		int n,largest=0,sec=0,sum=0;
		cin>>n;
		int arr[n];
		for(int i=0;i<n;i++){
			cin>>arr[i];
			if(arr[i]>arr[largest]){
				sec=largest;
				largest=i;
			}
			else if(arr[i]>=arr[sec])
				sec=i;
			sum+=arr[i];
		}
		int c=n;
		//cout<<"H"<<largest<<" "<<sec<<endl;
		printf("Case #%d: ",q);
		while(sum!=0){
			int flag=0;
			for(int i=0;i<n;i++){
				if(i!=largest && arr[i]>(sum-2)/2){
					flag=1;
					break;
				}
			}
			if((flag==1) || (arr[largest]==1)){
				if(c==3 && arr[largest]==1 && arr[sec]==1){
					arr[largest]--;
					cout<<(char)(65+largest)<<" ";
					sum--;
				}
				else{
					arr[largest]--;
					arr[sec]--;
					cout<<(char)(65+largest)<<(char)(65+sec)<<" ";
					sum-=2;
				}
				if(arr[largest]==0)
					c--;
				if(arr[sec]==0)
					c--;
			}
			else{
				arr[largest]-=2;
				cout<<(char)(65+largest)<<(char)(65+largest)<<" ";
				if(arr[largest]==0)
					c--;
				sum-=2;
			}

			for(int i=0;i<n;i++){
				if(arr[i]>arr[largest]){
					sec=largest;
					largest=i;
				}
				else if(arr[i]>=arr[sec])
					sec=i;
			}
		}
		cout<<endl;
	}
	return 0;
}
