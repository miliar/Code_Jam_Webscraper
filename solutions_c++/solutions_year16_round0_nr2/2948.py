#include <cstdio>
#include <string>
#include <iostream>

using namespace std;

int main () {
	int n;
	scanf("%d",&n);
	string x;
	for (int i=0;i<n;i++) {
		cin >> x;
		int ch=1;
		int cnt=0;
		while (ch) {
			ch=0;
			for (int i=x.length()-1;i>=0;i--) {
				if (ch) {
					if (x[i]=='+') x[i]='-';
					else x[i]='+';
				} else {
					if (x[i]=='-') {
						x[i]='+';
						ch=1;
					}
				}
			}
			cnt++;
		}
		printf("Case #%d: %d\n",i+1,cnt-1);
	}

	return 0;
}
