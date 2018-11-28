#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<iostream>
#include<algorithm>
#include<cassert>

using namespace std;
const int maxn = 1e6;
int cnt[11] = {0};

bool ok(){
	for (int i = 0; i < 10; ++i)
	if (cnt[i] == 0)return 0;
	return 1;
}

bool add(long long n){
	while (n > 0){
		int tmp = n%10;
		cnt[tmp] = 1;
		if (ok())return 1;
		n /= 10;
	}
	return 0;
}


void work(int n){
	if (n == 0){
		printf("INSOMNIA\n");
		return;
	}

	long long cur = 0;
	memset(cnt,0,sizeof(cnt));
	for (int i = 1;;++i){
		cur+= n;
		//cout<<cur<<endl;
		if (add(cur)){
			cout<<cur<<'\n';
			return;
		}
	}
	
}
 
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int T;
	int n;
	scanf("%d",&T);
	for (int i = 1; i <= T; ++i){
		scanf("%d",&n);
		printf("Case #%d: ",i);
		work(n);
	} 
	

	return 0;
}

