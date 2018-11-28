#include<iostream>
#include <string>
#include <fstream>
#include <vector>

using namespace std;

int main(){
	ifstream cin("input2.txt");
	ofstream cout("output2.txt");
	
	int T,n,a;
	int p;
	cin >> T;
	
	for(p = 1 ; p <= T ; p++){
		int result[3001];
		for(int i=0;i<=3000;i++){
			result[i]=0;
		}
		
		cin>>n;
		for(int i=0 ; i < (2*n-1) ; i++){
			for( int j=0;j<n;j++){
				cin>>a;
				result[a]++;
			}
		}
		
		cout<<"Case #"<< p <<": ";
		for( int i=0;i<=3000;i++){
			if(result[i]%2==1){
				cout<<i<<" ";
			}
 
		}
		cout<<endl;
	}
 
}
