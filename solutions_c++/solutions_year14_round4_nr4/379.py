#include <bits/stdc++.h>



using namespace std;





#define fr(i,a,b) for(int i=a;i<b;++i)
typedef long long ll;
typedef pair<int,int> pii;
#define F first
#define S second
#define mp make_pair
const int oo = 0x3f3f3f3f;


char st[1010][1010];
int trie[4][101000][26];
int qt[4];
int v[10];
int mai,nv;
int t,n,m;
void limpa(int a, int b){
	fr(i,0,26) trie[a][b][i] = -1;
}


void add(int t, char s[]){
	int no = 0, qn = 0;
	while(s[qn] != '\0'){
		if(trie[t][no][s[qn]-'A'] == -1){
			limpa(t,qt[t]);
			trie[t][no][s[qn]-'A'] = qt[t];
			qt[t]++;
		}
		no = trie[t][no][s[qn]-'A'];
		qn++;
	}	
}


void bt(int q){
	if(q == m){
		fr(i,0,n) qt[i] = 1, limpa(i,0);
		fr(i,0,m){
			add(v[i],st[i]);
		}
		int qtn = 0;
		fr(i,0,n){
			if(qt[i] != 1){
				qtn += qt[i];
			}
		}
		if(qtn > mai){
			mai = qtn;
			nv = 1;
		}
		else if(qtn == mai){
			nv++;
		}
		return;
	}
	fr(i,0,n){
		v[q] = i;
		bt(q+1);
	}
}




int main(){
	scanf("%d",&t);
	fr(cas,1,t+1){
		scanf("%d %d",&m,&n);
		fr(i,0,m) scanf("%s",st[i]);
		mai = nv = 0;
		bt(0);
		printf("Case #%d: %d %d\n",cas,mai,nv);
	}
	return 0;
}






















