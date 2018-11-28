#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <iomanip>
using namespace std;
int main(){
	freopen("D-large.in","r",stdin);
    freopen("D-large.out","w",stdout);
	int testCase,N,dwin,win;
	double naomi[1000];
	double ken[1000];
	cin>>testCase;
	for(int i=1;i<=testCase;i++){
		cin>>N;
		for(int j=0;j<N;j++){
			cin>>naomi[j];
		}
		for(int j=0;j<N;j++){
			cin>>ken[j];
		}
		sort(naomi,naomi+N);
		sort(ken,ken+N);
		int n=0;
		int k=0;
		dwin = 0;
		while(k<N){
			while(naomi[n]<ken[k]&&n<N){
				n++;
			}
			if(n<N){
				dwin++;
				k++;
				n++;
			}else{
				break;
			}
		}
		n=k=0;
		win = 0;
		while(n<N){
			while(ken[k]<naomi[n]&&k<N){
				k++;
			}
			if(k<N){
				win++;
				n++;
				k++;
			}else{
				break;
			}
		}
		cout<<"Case #"<<i<<": "<<dwin<<" "<<(N-win)<<endl;
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}