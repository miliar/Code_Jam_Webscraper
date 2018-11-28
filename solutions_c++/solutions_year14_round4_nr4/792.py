#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

#define fr(a,b,c) for(int a = b; a < c; a++)
#define rep(a,b) fr(a,0,b)
#define pb push_back
#define db if(1)
#define ln puts("")

struct trie{
	trie * a[26];
	
	trie(){
		rep(i,26) a[i] = NULL;
	}
	
	int count(){
		int res = 1;
		
		rep(i,26){
			if(a[i] != NULL){
				res += a[i]->count();
			}
		}
		
		return res;
	}
	
	void add(char * s){
		if(s[0] == 0) return;
		
		int pos = s[0] - 'A';
		
		if(a[pos] == NULL){
			a[pos] = new trie();
		}
		
		a[pos]->add(s+1);
	}
	
	void copy(trie * b){
		rep(i,26){
			if(b->a[i] != NULL){
				a[i] = new trie();				
				a[i]->copy(b->a[i]);
			}
		}
	}
};

int n,m;

char s[21][21];

bool read(){
	if(scanf("%d%d", &m, &n) == EOF) return false;
	
	rep(i,m) scanf("%s", s[i]);
	
	return true;
}

struct ret{
	int size;
	int cont;
};

trie cur[11];

ret bt(int pos){
	/*printf("%d\n", pos);
	rep(i,n){
		printf("%d ", cur[i].count());
	}
	ln;
	//*/
	if(pos == m) {		
		ret res;
		res.size = -1;
		res.cont = 0;
		
		int cont = 0;
		
		rep(i,n){
			int k = cur[i].count();
			if(k == 1){
				return res;
			}
			cont += k;
		}
		
		res.size = cont;
		res.cont = 1;
		
		return res;
	}	
	
	ret res;
	res.size = -1;
	res.cont = 0;
	
	rep(i,n){
		trie old;
		old.copy(&cur[i]);		
		cur[i].add(s[pos]);
		ret x = bt(pos+1);
		if(x.size > res.size){
			res = x;
		}
		else if(x.size == res.size){
			res.cont += x.cont;
		}
		cur[i] = old;
	}
	
	//printf("%d %d %d %d = %d %d\n", server, pos, size, cur.count(), res.size, res.cont);
	
	return res;
}

int cn = 1;

void process(){
	printf("Case #%d: ", cn++);

	rep(i,n){
		cur[i] = trie();
	}
	
	ret res = bt(0);
	
	printf("%d %d\n", res.size, res.cont);
}

int main(){
/*
	trie x;
	printf("%d\n", x.count());
	char buf[10];
	buf[0] = 'A';
	buf[1] = 0;
	x.add(buf);
	printf("%d\n", x.count());
	x.add(buf);
	printf("%d\n", x.count());
	buf[1] = 'B';
	buf[2] = 0;
	x.add(buf);
	printf("%d\n", x.count());
	trie y;
	y.copy(&x);
	printf("%d\n", y.count());
	return 0;
//*/

	
	int t;
	scanf("%d", &t);
	
	while(t-- && read()) process();
	
	return 0;
}


