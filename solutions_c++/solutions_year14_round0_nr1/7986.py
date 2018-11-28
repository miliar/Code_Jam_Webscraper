#include<iostream>

using namespace std;

int main(){
	int t;
	cin>>t;
	int n;
	int count;
	int **arr = new int*[4];
	for(int i=0;i<4;i++){
		arr[i] = new int[4];
	}
	int tt=1;
	int first;
	int *a = new int[4];
	while(tt<=t){
	//	cout<<"Entering whlie:"<<tt<<endl;
		count=0;
		cin>>n;
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				cin>>arr[i][j];
			}
		}
	//	cout<<"for 1 over\n";
		for(int i=0;i<4;i++){
			a[i] = arr[n-1][i];
		}
	//	cout<<"small for loop over\n";
		cin>>n;
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				cin>>arr[i][j];
			}
		}
	//	cout<<"for2 over\n";
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				if(arr[n-1][i]==a[j]){
					first = a[j];
					count++;
				}
			}
		}
	//	cout<<"for 3 over\n";
		if(count==1){
			cout<<"Case #"<<tt<<": "<<first<<endl;
		}
		else if(count==0){
			cout<<"Case #"<<tt<<": Volunteer cheated!\n";
		}
		else{
			cout<<"Case #"<<tt<<": Bad magician!\n";
		}
		tt++;
	}
	delete(a);
	for(int i=0;i<4;i++){
		delete(arr[i]);
	}
	delete(arr);
	return 0;
}
