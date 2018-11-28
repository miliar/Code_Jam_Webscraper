#include <iostream>
using namespace std;
#define N 4
int main() {
	int test=0;
	int test_case=1;
	cin>>test;
	
	while(test--){
		int row=0,new_row=0; 
		int found_count=0;
		int result=0;
		int A1[N] = {0}, A2[N] = {0};
		int x;
		
		
		cin>>row;
		for(int i=0;i<N;i++){
			for(int j=0;j<N;j++){
				if(i==row-1)
				cin>>A1[j];
				else
				cin>>x;
			}
		}
		
		cin>>new_row;
		for(int i=0;i<N;i++){
			for(int j=0;j<N;j++){
				if(i==new_row-1)
				cin>>A2[j];
				else
				cin>>x;
			}
		}
		for(int i=0;i<N;i++)
			for(int j=0;j<N;j++)
			{
				if(A1[i] == A2[j]) 
				{
					found_count++;
					if(1==found_count){
					result=A1[i];
					}
				}
		}
		switch(found_count){
			case 0:{
				cout<<"Case #"<<test_case<<": "<<"Volunteer cheated!"<<endl;
				break;
			}
			case 1:{
				cout<<"Case #"<<test_case<<": "<<result<<endl;
				break;
			}
			default:{
				cout<<"Case #"<<test_case<<": "<<"Bad magician!"<<endl;
				break;
			}
		}
		test_case++;
	}
	return 0;
}