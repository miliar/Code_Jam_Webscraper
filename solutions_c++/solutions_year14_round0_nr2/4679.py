#include<iostream>
#include<vector>
using namespace std;

int main(){
    int T,i =1;	
	cin >> T;
	while(T-->0){
		double ret = 0,C,F,X,p =2.0;	
		cin >> C >> F >> X;
		double t1 = X/p;
		double t2 = ret + C/p + X/(p+F);
		while(t1>t2){
			ret += C/p;
			p+=F;	
			t1 = t2;
			t2 = ret + C/p + X/(p+F);
		}
		printf("Case #%d: %.8f\n",i++,t1);
		}
	return 0;
}
