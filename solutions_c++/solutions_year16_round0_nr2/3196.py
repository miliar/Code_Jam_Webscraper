#include <bits/stdc++.h>
#define mem(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
const int maxn = 100005;

ofstream out("out.txt");
string s;
int ori[105];
int sta[1 << 20];
int num[20];
int len = 0;
int get1(){
	int ret= 0;
	for(int i = 0;i < len;i++){
		ret = ret * 2 + ori[i];
	}
	return ret;
}
int get2(){
	int ret= 0;
	for(int i = 0;i < len;i++){
		ret = ret * 2 + num[i];
	}
	return ret;
}
queue<int> que;
void bfs(){
	while(!que.empty()){
		int temp = que.front();
		int gaga = temp;
		que.pop();
		for(int i = len - 1;i >= 0;i--){
			ori[i] = gaga & 1;
			gaga = gaga >> 1;
		}
		for(int i = 0;i < len;i++){
			for(int j = i,t = 0;j >= 0;j--,t++)num[j] = ori[t] ^ 1;
			for(int j = i + 1;j < len;j++)num[j] = ori[j];
			int now = get2();
			if(sta[now] > sta[temp] + 1){
				que.push(now);
				sta[now] = sta[temp] + 1;
			}
		}
	}
}
int main(){
	int T;
	scanf("%d",&T);
	for(int cas = 1;cas <= T;cas++){
		cin>>s;
		len = s.length();
		mem(sta,0x3f);
		for(int i = 0;i < len;i++)
			ori[i] = (s[i] == '+') ? 1 : 0;
		int now = get1();
		sta[now] = 0;
		que.push(now);
		bfs();
		int zong = (1 << len) - 1;
		out<<"Case #"<<cas<<": "<<sta[(1 << len) - 1]<<endl;
	}

}
