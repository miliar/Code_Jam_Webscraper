#include <stdio.h>
#include <iostream>
#define FOR(i,a,b) for (int i=(a);i<(b);i++)
#define RFOR(i,a,b) for (int i=(b)-1;i>=(a);i--)
#define REP(i,n) for (int i=0;i<(n);i++)
#define RREP(i,n) for (int i=(n)-1;i>=0;i--)

using namespace std;
int n,N,total,c;
void solve(){
	cin >> n;
	REP(m,n){
		int a[10]={};
		cin >> N;
		
		for(int j=1;;j++){

			c=j*N;
		while(c != 0){
			a[c%10]=1;
			c = c/10;
			
		}
		         total=0;
			REP(i,10){
				total+=a[i];
				//cout << a[i]<< " " ;
			}
                        if(total==10) {
				cout << "Case #"<<m+1<<": "<<j*N<<endl;
				break;
			}
			if (N==0){
				cout <<"Case #"<<m+1<<": INSOMNIA"; 
	break;
			}}

	}

}


int main(){
	solve();
	return 0;
}


