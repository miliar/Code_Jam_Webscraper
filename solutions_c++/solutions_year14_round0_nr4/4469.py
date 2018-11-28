#include<iostream>
#include<algorithm>
using namespace std;

int main(){
	int tc,n;
	double naomi[1000], ken[1000];
	cin>>tc;
	for(int i=1;i<=tc;i++){
		cin>>n;	
		for(int j=0;j<n;j++){
			cin>>naomi[j];
		}
		for(int j=0;j<n;j++){
			cin>>ken[j];
		}
		
		int deceit = 0;
		int honest = 0;
		
		sort(naomi, naomi+n);
		sort(ken, ken+n);
		
		int idxNaomi = 0;
		int idxKen = 0;
			
		//calculate deceit
		while(idxNaomi < n && idxKen < n){
			if(naomi[idxNaomi] > ken[idxKen]){
				deceit++;
				idxKen++;
				idxNaomi++;
			} else if(naomi[idxNaomi] < ken[idxKen]){
				idxNaomi++;
			} //else tidak mungkin, pasti beda
		}
		
		//calculate honest
		idxNaomi = 0;
		idxKen = 0;
		while(idxNaomi < n && idxKen < n){
			if(ken[idxKen] > naomi[idxNaomi]){
				honest++;
				idxNaomi++;
				idxKen++;
			} else if(naomi[idxNaomi] > ken[idxKen]){
				idxKen++;
			} //else tidak mungkin, pasti beda
		}
		
		honest = n - honest;
		
		cout<<"Case #"<<i<<": "<<deceit<<" "<<honest<<endl;
	}
	return 0;
}