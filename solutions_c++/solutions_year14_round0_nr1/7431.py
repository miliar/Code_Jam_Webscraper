#include <stdio.h>
#include <iostream>
#include <sstream>
#include <string.h>
#include <string>
#include <math.h>
#include <algorithm>
using namespace std;

const int maxn=205;

int num[20];

void solve() {
}

int main() {
	int T,kase=0,l,temp;
	cin>>T;
	while (T--) {
		memset(num,0,sizeof(num));
		cin>>l;
		l--;
		for (int i=0;i<4;i++)
			for (int j=0;j<4;j++) {
				cin>>temp;
				if (i==l) num[temp]++;
			}
		cin>>l;
		l--;
		for (int i=0;i<4;i++)
			for (int j=0;j<4;j++) {
				cin>>temp;
				if (i==l) num[temp]++;
			}
		int ans=0;
		bool bad=false;
		for (int i=1;i<=16;i++)
			if (num[i]==2) {
				if (ans==0) ans=i;
				else bad=true;
			}
		cout<<"Case #"<<++kase<<": ";
		if (bad) cout<<"Bad magician!"<<endl;
		else if (ans==0) cout<<"Volunteer cheated!"<<endl;
		else cout<<ans<<endl;
	}
	return 0;
}
