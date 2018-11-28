#include <bits/stdc++.h>
#define mem(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
const int maxn = 100005;

ofstream out("out.txt");
int K,C,S;

int main(){
	int T;
	scanf("%d",&T);
	for(int cas = 1;cas <= T;cas++){
		scanf("%d%d%d",&K,&C,&S);
		C--;
		string all = "";
		for(int i = 0;i < K;i++)all += "1";
		for(int i = 0;i < (1 << K);i++){
			string s = "";
			string ss = "";
			string ans = "";
			int temp = i;
			for(int j = 0;j < K;j++){
				char c = '0';
				c += (temp & 1);
				s += c;
				temp = temp >> 1;
			}
			reverse(s.begin(),s.end());
			ss = s;
			temp = C;
			while(temp--){
				for(int i = 0;i < ss.length();i++){
					if(ss[i] == '1')ans += all;
					else ans += s;
				}
				ss = ans;
			}
			out<<ans<<endl;
		}
	}
}
