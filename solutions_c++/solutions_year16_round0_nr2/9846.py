#include<iostream>
#include<cstring>
using namespace std;
int f[11][1<<11];
int limit;
bool flag;
void dfs(int x,int len,int now){
	if (now==limit){
		if (x==((1<<len)-1))
			flag=true;
	}
	if (flag) return;
	if (now>=limit) return;
	//cout << "testing... " << x << " " << now << endl;
	for (int i=1;i<=len;i++){
		int y=0;
		for (int j=0;j<i;j++)
			y|=(!((x&(1<<(i-j-1)))>0))<<j;
			// 0000 000
			//    i   j
			// 0000
		for (int j=i;j<len;j++)
			y|=(x&(1<<j));
		dfs(y,len,now+1);
	}
}
int test(int x,int i,int len){
	int y=0;
	for (int j=0;j<i;j++)
		y|=(!((x&(1<<(i-j-1)))>0))<<j;
		// 0000 000
		//    i   j
		// 0000
	for (int j=i;j<len;j++)
		y|=(x&(1<<j));
	return y;
}
int main(){
//	while (true){
//		int x,i,len;
//		cin >> x >> i >> len;
//		cout << test(x,i,len) << endl;
//	}
	memset(f,0x3f,sizeof(f));
	int t;
	cin >> t;
	for (int tt=0;tt<t;tt++){
		flag=false;
		string s;
		cin >> s;
		int x=0;
		for (int i=s.length()-1;i>=0;i--){
			x<<=1;
			x+=(s[i]=='+'?1:0);
		}
		for (limit=0;limit<=s.length();limit++){
			dfs(x,s.length(),0);
			if (flag){
				cout << "Case #" << tt+1 << ": " << limit << endl;
				break;
			}
		}
	}
	return 0;
}

