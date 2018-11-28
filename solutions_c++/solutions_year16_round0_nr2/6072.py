#include <bits/stdc++.h>
#define optimizar_io ios_base::sync_with_stdio(0);cin.tie
using namespace std;

char act[102];

int T;
int N;
int pos;
int res;

int main(){
	optimizar_io(0);
	cin>>T;
	for(int caso =1 ; caso <= T; caso++){
		cin>>act;
		res = 0;
		for(N=0;act[N];N++);
		if(act[0]=='-')
			res++;
		pos = 0;
		while(act[pos]=='-')
			pos++;
		while(pos < N){
			if(act[pos]=='+'){
				while(act[pos]=='+')
					pos++;
			} else {
				while(act[pos]=='-')
					pos++;
				res += 2;
			}			
		}
		cout<<"Case #"<<caso<<": "<<res<<"\n";
	}
	return 0;
}