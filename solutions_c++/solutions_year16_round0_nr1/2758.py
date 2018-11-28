#include <bits/stdc++.h>
using namespace std;
#define mp make_pair
#define pb push_back
#define f first
#define s second
#define D(x) cout << #x << " = " << (x) << endl;
#define all(x) (x).begin(),(x).end()
int n;
int cnt[10];
void process(long long x){
	while(x>0){
		cnt[x%10] = 1;
		x /= 10;
	}
}
bool check(){
	for(int i=0;i<10;i++)
		if(cnt[i]==0)
			return false;
	return true;
}

int main()
{
    freopen("/home/khaled/file.in","r",stdin);
    freopen("/home/khaled/file.out","w",stdout);
    int T,tc(1);
    cin >> T;
    while(T--){
		cin >> n;
		if(n==0){
			printf("Case #%d: INSOMNIA\n",tc++);
			continue;
		}
		memset(cnt,0,sizeof cnt);
		bool ok = 0;
		for(long long i=n;i<=100000LL*n;i+=n){
			process(i);
			if(check()){
				printf("Case #%d: %lld\n",tc++,i);
				ok = 1;
				break;
			}
		}
		if(!ok) printf("Case #%d: INSOMNIA\n",tc++);
    }
    return 0;
}



