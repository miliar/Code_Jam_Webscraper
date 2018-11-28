#include <iostream>
#include <string>
using namespace std;

int main() {
	// your code goes here
	int T;
	cin>>T;
	int Smax[T]={0};
	string S[T];int SS[T][7]={0};
	int count[T]={0};
	
	for(int i=0; i<T; i++){
		cin>>Smax[i];
		cin>>S[i];
	}
	
	//cout<<S[2][0]<<endl;
	
	for(int i=0; i<T; i++){
		for(int j=0; j<=Smax[i]; j++){
			SS[i][j]=0;
			for(int k=0; k<j; k++){
				SS[i][j]+=S[i][k]-'0';
			}
			//cout<<SS[i][j]<<endl;
		}
	}
	
	
	
	for(int i=0; i<T; i++){
		for(int j=1; j<=Smax[i]; j++){
			if ((S[i][j]!='0') && (SS[i][j] < j )) {
				count[i]+=j-SS[i][j];
				int temp=j-SS[i][j];
				
				for(int k=j+1; k<=Smax[i]; k++){
					SS[i][k]+=temp;
				}
			}
		}
	}
	
	for(int i=0; i<T; i++){
		cout<<"Case #"<<i+1<<": "<<count[i]<<endl;
	}
	
	return 0;
}