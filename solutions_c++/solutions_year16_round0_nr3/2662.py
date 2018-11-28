#include <bits/stdc++.h>
#define mem(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
const int maxn = 100005;
ofstream out("out.txt");
int N,J;
int num[20];
void get(int now){
	for(int i = (N - 1);i >= 0;i--){
		num[i] = now & 1;
		now = now >> 1;
	}
}
int check(ll wei){
	ll ret = 0;
	ll now = 1;
	for(int i = (N - 1);i >= 0;i--){
		ret += now * num[i];
		now = wei * now;
	}
	for(ll i = 2;i * i <= ret;i++)
		if(ret % i == 0)return 1;
	return 0;
}

int go(ll wei){
	ll ret = 0,now = 1;
	for(int i = (N - 1);i >= 0;i--){
		ret += now * num[i];
		now = wei * now;
	}
	for(ll i = 2;i * i <= ret;i++)
		if(ret % i == 0){
			return i;
		}
	return 0;
}

int main(){
	int T;
	scanf("%d",&T);
	for(int cas = 1;cas <= T;cas++){
		scanf("%d%d",&N,&J);
		int cnt = 0;
		out<<"Case #"<<cas<<": "<<endl;
		for(int i = (1 << (N - 1));i < (1 << N);i++){
			i = i | 1;
			get(i);
			int f = 1;
			for(int j = 2;j <= 10;j++){
				if(check(j) == 0){f = 0;break;}
			}
			if(f){
				vector<int> vec,ttt;
				for(int t = 0;t <= (N - 1);t++)vec.push_back(num[t]);
				int f = 1,ok = 0;
				for(int t = 2;t <= 10;t++){
					f = go(t);
					if(f)ttt.push_back(f);
					else {
						ok = 1;
					}
				}
				if(ok)continue;
				for(int t = 0;t < vec.size();t++)out<<vec[t];
				for(int t = 0;t < ttt.size();t++)out<<" "<<ttt[t];
				out<<endl;
				cnt++;
				if(cnt >= J)break;
			}
		}
	}

}
