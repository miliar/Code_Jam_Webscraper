#include <iostream>
#include <stdio.h>
using namespace std;

int main(){
	int n;
	cin >> n;
	for(int i=0;i<n;i++){
		double c,f,x;
		cin >> c >> f >> x;
		double v = 2.0f;
		double t = 0.0f;
		while(true){
			if(t+x/(v+f)+c/v<t+x/v){
				t+=c/v;
				v+=f;
				continue;
			}
			else{
				t+=x/v;
				break;
			}
		}
		printf("Case #%d: %.7f\n",i+1,t);
		//cout << "Case #" << i+1 << ": " << t;
	}
	return 0;
}