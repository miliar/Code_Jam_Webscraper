#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <iostream>

using namespace std;

const int max_pre = 30000;
vector <int> p;
bool vis[max_pre];
int n;
int s[100];
int is_p[100];

void pre() {
    for(int i = 2; i < max_pre; i++) {
		if(!vis[i]) p.push_back(i);
		for(int j = 0; j < p.size() && p[j] <= (max_pre-1)/i; j++) {
            vis[p[j]*i] = true;
            if(i % p[j] == 0) break;
		}
    }
    //for(int i = 0; i < p.size(); i++) printf("%d ",p[i]);
}

bool che(int pr,int ji) {
	int t = 1, ret = 0;
    for(int i = 0; i < n; i++) {
		ret = (ret + t*s[i]) % pr;
		t = (t * ji) % pr;
    }
    return ret == 0;
}

bool check() {
	memset(is_p, 0, sizeof(is_p));
    for(int i = 0; i < p.size(); i++) {
		bool flag = true;
        for(int j = 2; j <= 10; j++)
			if(!is_p[j]) {is_p[j] = che(p[i], j)?p[i]:0; flag = false;}
        if(flag) return true;
    }
    return false;
}

void output() {
	for(int i = n-1; i >= 0; i--) printf("%d",s[i]);
	for(int i = 2; i <= 10; i++) printf(" %d",is_p[i]);
	puts("");

	//

	/*for(int i = 2; i <= 10; i++) {
		printf(" %d",is_p[i]);
		putchar('(');
		int t = 1, ret = 0;
		for(int j = 0; j < n; j++) {
			ret = ret + t*s[j];
			t = t*i;
		}
		printf("%d)",ret);
	}
	puts("");*/
}

void add_one() {
    s[1]++;
    for(int i = 1; i < n; i++) if(s[i] == 2) {
		s[i] = 0;
		s[i+1]++;
    }
    if(s[n]) {
    	puts("wrong");
    	while(1);
    }
}

int main()
{
	pre();
	freopen("C-large.in","r",stdin);
	freopen("C.out","w",stdout);
	int T, k;
	scanf("%d",&T);
    for(int cas = 1; cas <= T; cas++) {
		printf("Case #%d:\n",cas);
    	scanf("%d%d",&n,&k);
    	memset(s, 0, sizeof(s));
    	s[n-1] = s[0] = 1;
    	while(k) {
			if(check()) output(), k--;
			add_one();
    	}
    }
    return 0;
}
