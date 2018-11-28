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

int main (int argc, char *argv[])
{
	int noc,n;
	char x[2000];
	scanf("%d",&noc);
	for (int cs=1;cs<=noc;cs++){
		scanf("%d%s",&n,x);
		int cnt=x[0]-'0';
		int ans=0;
		for (int i=1;i<=n;i++){
			if (x[i]!='0' && cnt<i){
				ans+=i-cnt;
				cnt+=x[i]-'0'+ans;
			}else{
				cnt+=x[i]-'0';
			}
		}
		cout<<"Case #"<<cs<<": "<<ans<<endl;
	}
	return 0;
}
