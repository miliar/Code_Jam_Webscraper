#include <bits/stdc++.h>
using namespace std;

int  main() {
	int t;
	scanf("%d", &t);

	for(int k=1; k<=t; k++) {
		string s;
		cin>>s;
		int l = s.length();
		int ind=INT_MAX;

		for(int i=l-1; i>=0; i--) {
			if(s[i]=='-') {
				ind=i;
				break;
			}
		}
		if(ind==INT_MAX) {
			printf("Case #%d: 0\n", k);
			continue;
		}
		ind--;
		if(ind<0) {
			printf("Case #%d: 1\n", k);
			continue;
		}
		while(s[ind]=='-' && ind>=0) {
			ind--;
		}
		if(ind<0) {
			printf("Case #%d: 1\n", k);
			continue;
		}
		int flag=0,f=0,c=1;

		while(1) {
			//cout<<"c -> "<<c<<"ind -> "<<ind<<endl;
			f=0;
			while(s[ind]=='+') {
				if(f==0) {
					c++;
					f=1;
				}
				ind--;
				if(ind<0) {
					flag=1;
					break;
				}
			}
			if(flag==1)	break;
			f=0;
			while(s[ind]=='-') {
				if(f==0) {
					c++;
					f=1;
				}
				ind--;
				if(ind<0) {
					flag=1;
					break;
				}
			}
			if(flag==1)	break;
		}
		printf("Case #%d: %d\n", k,c);
	}
	return 0;
}
