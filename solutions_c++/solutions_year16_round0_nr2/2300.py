#include<stdio.h>
#include<string.h>
#include<vector>
#include<queue>
#include<set>
#include<string>
#include<map>

using namespace std;
#define INF 0x3f3f3f3f

char buff[1000];

int mymap[1 << 10];
map<string,int> ans;

int flip(int x,int i){
	int ret = x;
	for(int j = 0;j < i;++j){
		if((x >> j) & 1){
			ret |= (1 << (i - j - 1));
			ret ^= (1 << (i - j - 1));
		}else{	
			ret |= (1 << (i - j - 1));
		}
	}
	return ret;
}

void bfs(){
	queue<int> q;
	memset(mymap,-1,sizeof(mymap));
	mymap[0] = 0;
	q.push(0);
	while(!q.empty()){
		int x = q.front();
		q.pop();
		for(int i = 1;i <= 10;++i){
			int t = flip(x,i);
			if(mymap[t] == -1){
				mymap[t] = mymap[x] + 1;
				q.push(t);
			}
		}
	}
}

string gen_str(int x){
	string ret = "";
	for(int i = 0;i < 10;++i){
		if((x >> i) & 1)
			ret += "-";
		else
			ret += "+";
	}
	return ret;
}

void init(){
	memset(mymap,-1,sizeof(mymap));
	mymap[0] = 0;
	bfs();
	for(int i = 0;i < (1 << 10);++i){
		ans[gen_str(i)] = mymap[i];
	}
}

int solve(string s){
	while(s.length() < 10)
		s += "+";
	if(ans.find(s) == ans.end())
		printf("not found %s\n",s.c_str());
	return ans[s];
}

int greedy(string s){
	int n = s.length() - 1;
	int ret = 0;
	while(1){
		int left = 0;
		for(int i = 0;i < s.length();++i){
			if(s[i] == '+')
				++left;
			else
				break;
		}
		int done = 0;
		for(int i = s.length() - 1;i >= 0;--i){
			if(s[i] == '+')
				++done;
			else
				break;
		}
		if(done == s.length())
			break;
		if(left != 0){
			for(int i = 0;i < left;++i)
				s[i] = '-';
			++ret;
		}else{
			int l = 0,r = s.length() - 1 - done;
			while(l <= r){
				swap(s[l],s[r]);
				s[l] = '+' - s[l] + '-';
				if(l != r)
					s[r] = '+' - s[r] + '-';
				++l;
				--r;
			}
			++ret;
		}
	}
	return ret;
}

int main(){
//	init();
	int T;
	scanf("%d",&T);
	for(int cas = 1;cas <= T;++cas){
		scanf("%s",buff);
//		int t = solve(string(buff));
//		int t2 = greedy(string(buff));
//		if(t != t2){
//			printf("error: %s %d %d\n",buff,t,t2);
//			while(1);
//		}
		printf("Case #%d: %d\n",cas,greedy(string(buff)));
	}
	return 0;
}

