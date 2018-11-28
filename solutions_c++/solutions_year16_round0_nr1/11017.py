#include <iostream>
using namespace std;

int totalno(int n, int *c){

	while(n>0){
		 c[n%10]=1;
		 n/=10;
	}
	n = 0;
	for (int i = 0; i < 10; ++i)
	{
		if(c[i]==1) n++;
	}
	return n;
}

int main(){
	int t, i; cin >> t; 
	for(int j = 1; j <= t ; ++j){
		int c[10] = {0};
		int n; cin >> n;
		if(n==0){
			cout<<"Case #"<<j<<": "<<"INSOMNIA\n";
		}
		else{
				i = 1;
				unsigned long long l = n ;
				while(totalno(l,c)!=10 && l < 1844674407370955161){
					l = n*i;
					i++;
				}
				if(totalno(l,c)==10) cout<<"Case #"<<j<<": "<<l<<endl;
				else cout<<"zz Case #"<<j<<": "<<"INSOMNIA\n";
		}
			
	}

}

