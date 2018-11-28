#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <iostream>

using namespace std;

inline void read(int &data) {
	bool inv=false;
	char ch = getchar();
	while (ch < '0' || ch > '9') {
		if (ch=='-')	inv=true;
		ch = getchar();
	}
	data = 0;
	do{
		data = data*10 + ch-'0';
		ch = getchar(); 
	}while (ch >= '0' && ch <= '9');
	if (inv)	data=-data;
}
typedef long long LL;
LL a[1000000];
int n;
int main (int argc, char *argv[])
{
	int noc;
	read(noc);
	for (int cs=1;cs<=noc;cs++){
		read(n);
		for (int i=1;i<=n;i++){
			scanf("%lld",&a[i]);
		}
		LL ans1=0,ans2=0,maxv=0;;
		for (int i=2;i<=n;i++){
			if (a[i]<a[i-1]){
				ans1+=a[i-1]-a[i];
				maxv=max(maxv,a[i-1]-a[i]);
			}
		}
		for (int i=2;i<=n;i++){
			if (a[i-1]<=maxv)	ans2+=a[i-1];
			else ans2+=maxv;
		}
		cout<<"Case #"<<cs<<": "<<ans1<<" "<<ans2<<endl;
	}
	return 0;
}
