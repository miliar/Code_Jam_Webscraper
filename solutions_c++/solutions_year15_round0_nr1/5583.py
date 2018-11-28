#include <iostream>
#include <cstdio>
#include <string>

using namespace std;

int main(){
	int T;
	cin >> T;
	for(int kase=1;kase<=T;kase++){
		int smax;
		cin>>smax;

		string shyes;
		cin >> shyes;
		int needed = 0;
		int acum = 0;
		for (int i=0;i<smax+1;++i){
			if(acum < i){
				needed+= i-acum;
				acum=i;
			}
			acum += shyes[i] - '0';
		}
		printf("Case #%d: %d\n",kase,needed);
	}
	return 0;
}