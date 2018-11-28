#include <iostream>
#include <cstdio>
using namespace std;

int main() {
	int t;
	cin>>t;
	int count=0;
	while(t--){
		double C,F,X,y=0;
		int n=0;
		count++;
		cin>>C>>F>>X;
			double ny,temp=0;
			y = temp + (X/(2+(n*F)));
			temp =  C/(2+(n*F));
			ny= temp + (X/(2+((n+1)*F)));
			while(ny<y){
				n++;
				y = temp + (X/(2+(n*F)));
				temp = temp + (C/(2+(n*F)));
				ny= temp + (X/(2+((n+1)*F)));
			}
			
		cout<<"case #"<<count<<": ";
			printf("%.7lf\n",y);
	}
	return 0;
}