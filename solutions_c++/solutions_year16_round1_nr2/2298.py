#include<iostream>
#include<deque>
#include<algorithm>
#include<cmath>
using namespace std;
int main (){
	int x;
	cin>>x;
	int n;
	int array[2501];
	int num;
	for(int i=1;i<=x;i++){
		cin>>n;
		
		for(int j=1;j<=2500;j++){
			array[j]=0;
		}
		for(int j=0;j<2*n-1;j++){
			for(int k=1;k<=n;k++){
				cin>>num;
				array[num]++;
			}
		}
		
		cout<<"Case #"<<i<<": ";
		for(int j=1;j<=2500;j++){
			if(array[j]%2==1){
				cout<<j;
				n--;
				if(n==0){
					cout<<endl;
				}else{
					cout<<" ";
				}
			}
		}
		
	}
}
