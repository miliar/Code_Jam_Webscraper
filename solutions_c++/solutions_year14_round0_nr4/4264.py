#include<iostream>
#include<algorithm>
using namespace std;

int main() {
	int nc;
	cin>>nc;
	for(int i=0;i<nc;i++){
		int n;
		cin>>n;
		long double ar1[n],ar2[n];
		for(int j=0;j<n;j++){
			cin>>ar1[j];
			}
		for(int j=0;j<n;j++){
			cin>>ar2[j];
			}
		sort(ar1,ar1+n); 
		sort(ar2,ar2+n);
		//DW starts here
		int score1=0,reject1=0;
		for(int j=n-1;(score1+reject1)<n;j--){
			if(ar1[j+reject1]>ar2[j]){
				score1++;
				}
			else{
				reject1++;			
				}
			}
		cout<<"Case #"<<i+1<<": "<<score1<<" ";
		//DW ends here
		//W starts here
		int score2=0,reject2=0;
		for(int j=n-1;(score2+reject2)<n;j--){
			if(ar2[j+reject2]>ar1[j]){
				score2++;
				}
			else{
				reject2++;
				}
			
			}
		cout<<reject2<<endl;
}


} 
