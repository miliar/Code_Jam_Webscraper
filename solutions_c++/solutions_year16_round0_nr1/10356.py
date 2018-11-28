#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cstdlib>

using namespace std;

int main(){

	int t, n, seen = 0;
	bool dig[11];
	cin>>t;
	for(int test = 1;test<=t;test++){
		memset(dig, 0, sizeof(dig));
		seen = 0;
		cin>>n;
		if(n==0){
			cout<<"Case #"<<test<<": INSOMNIA"<<endl;
		}else{
			int i=1;
			while(seen < 10){
				int cur = n*i;
				while(cur){
					int d = cur %10;
					if(!dig[d]){
						dig[d] = true;
						seen++;
					}
					cur /=10;
				}
				if(seen == 10){
					break;
				}
				i++;
			}
			cout<<"Case #"<<test<<": "<<n*i<<endl;

		}
	}


return 0;
}