#include<iostream>
#include<cmath>
#include<cstring>
#include<cstdio>
#include<algorithm>
#include<cstdlib>
#include<iomanip>
#include<vector>
#include<list>
#include<iterator>
#include<stack>
#include<queue>
using namespace std;

#include<fstream>
FILE *fin=freopen("a.in","r",stdin);
FILE *fout=freopen("a.out","w",stdout);

int T,t,n,i,j,k,p[21][2],m,ans,b[1<<17];
char s[6][6],ss[6][6],sss[6][6];

bool yes() {
	int x,y,z,zz,tt;
	for (x=0;x<n;x++) {
		tt=zz=0;
		for (y=0;y<n;y++)
		if (ss[x][y]=='1')
		tt++;
		for (y=0;y<n;y++) {
			for (z=0;z<n;z++)
			if (ss[x][z]!=ss[y][z])
			break;
			if (z==n)
			zz++;
			else {
				for (z=0;z<n;z++)
				if (ss[x][z]=='1' && ss[y][z]=='1')
				return 0;
			}
		}
		if (tt!=zz)
		return 0;
	}
	return 1;
}

int main() {
	b[0]=0;
	for (i=1;i<(1<<16);i++)
	b[i]=b[i/2]+i%2;
	cin>>T;
	for (t=1;t<=T;t++) {
		cin>>n;
		for (i=0;i<n;i++)
		scanf("%s",s[i]);
		m=0;
		for (i=0;i<n;i++)
		for (j=0;j<n;j++)
		if (s[i][j]=='0') {
			p[m][0]=i;
			p[m][1]=j;
			m++;
		}
		ans=999;
		for (i=0;i<(1<<m);i++) {
			memcpy(ss,s,sizeof(s));
			for (j=0;j<m;j++)
			if ((i&(1<<j))==(1<<j)) {
				ss[p[j][0]][p[j][1]]='1';
			}
			if (yes()) {
				ans=min(ans,b[i]);
			}
		}
		printf("Case #%d: %d\n",t,ans);
	}
    return 0;
}
