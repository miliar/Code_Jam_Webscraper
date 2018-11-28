#include <iostream>
#include <algorithm>

using namespace std;


int N;

int arr[26];



void solve(){
	
	int total = 0;
	
	char even = 0;
	char odd = 0;
	
	do{
		total = 0 ;
		for( int i = 0 ; i < N; i++ ){
			total = total + arr[i];	
		}
		if( total == 2){
			if(even){
				cout<<" "<<even ;
				even = odd = 0;
			}		

			cout << " ";	
			for( int i = 0 ; i < N; i++ ){
				if( arr[i] > 0){
					char party = 'A' + i;
					cout << party;
				}
			}
			total = 0;
		}
		else
		{
			
			int top1 = 0; int top1Index = -1;
			
			for( int i = 0 ; i < N; i++ ){
				if( arr[i] > top1){
					top1 = arr[i];
					top1Index = i;
				}
			}
			
			char party = 'A' + top1Index;
			//cout<<" "<< party;
			arr[top1Index] = arr[top1Index] -1;
			if(!even){
				even = party;
			}
			else if(!odd){
				odd = party;
			}
			
		}
		
		if(even&&odd){
			cout<<" "<<even <<odd;
			even = odd = 0;
		}
		
		
	} while(total > 0);
}

int main(){
	int T;
	cin >> T;
	
	for( int t = 1 ; t <= T ; t++)
	{
		cin >> N;
		for( int i = 0 ; i < N; i++ ){
			cin >> arr[i];	
		}
		cout <<"Case #"<<t<<":" ; solve() ; cout << "\n";
	}
	
	return 0;
}