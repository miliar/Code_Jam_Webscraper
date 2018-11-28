#include <iostream>
#include<map>
#include<cstdio>
using namespace std;

int main() {
	int t,i,j,n1,n2,a,l=1,p,q;
	cin>>t;
	while(t--) {
		p = 0;
		q = 0;
		int z[4][4];
		map<int,int>mp1;
		cin>>n1;
		for(i=0;i<4;i++)
		for(j=0;j<4;j++)
		cin>>z[i][j];
		cin>>n2;
		for(i=1;i<n2;i++)
		for(j=0;j<4;j++)
		cin>>a;
		for(i=0;i<4;i++) {
			cin>>a;
			mp1[a]++;
		}
		for(i=n2+1;i<=4;i++)
		for(j=0;j<4;j++)
		cin>>a;
		for(i=0;i<4;i++) {
			if(mp1[z[n1-1][i]]==1) {
			p = z[n1-1][i];
			q++;
			}
		}
		if(q==1) {
			printf("Case #%d: %d\n",l,p);
		}
		else if(q==0) {
			printf("Case #%d: Volunteer cheated!\n",l);
		}
		else
		printf("Case #%d: Bad magician!\n",l);
		l++;
		}
	return 0;
}