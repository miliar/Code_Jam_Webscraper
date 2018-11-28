#include <bits/stdc++.h>
using namespace std;
typedef long long LL;
const int N = 105;
const int MOD = 10000007;

struct Trie  {    
    Trie *next[26];    
    Trie *fail;   
    bool end;
}*root;    
Trie *que[N],s[N];    
int tot;
char alpha[N] , target[N];
double cnt[26];
int k , l , n;
Trie *NewNode()  {    
    Trie *tmp=&s[tot ++];  
    for (int i = 0 ; i < 26 ; i ++)
    	tmp->next[i] = NULL;
    tmp -> end = false;
    tmp -> fail = NULL; 
    return tmp;    
}    
void Insert(Trie *root,char *s,int len)  {    
    Trie *p=root;    
    for(int i=0; i<len; i++){    
        if(p->next[s[i]-'A']==NULL) p->next[s[i]-'A']=NewNode();    
        p=p->next[s[i]-'A'];    
    }    
    p -> end = true;
}    
void Bulid_fail(Trie *root)  {    
    int head=0,tail=0;    
    que[tail++]=root;    
    root->fail=NULL;    
    while(head<tail){    
        Trie *tmp=que[head++];    
        for(int i=0; i<26; i++){    
            if(tmp->next[i]){    
                if(tmp==root) tmp->next[i]->fail=root;    
                else{    
                    Trie *p=tmp->fail;    
                    while(p!=NULL){    
                        if(p->next[i]){    
                            tmp->next[i]->fail=p->next[i];    
                            break;    
                        }    
                        p=p->fail;    
                    }    
                    if(p==NULL) tmp->next[i]->fail=root;    
                }    
                if(tmp->next[i]->fail->end) tmp->next[i]->end|=tmp->next[i]->fail->end;  
                que[tail++]=tmp->next[i];    
            }    
            else if(tmp==root) tmp->next[i]=root;    
            else tmp->next[i]=tmp->fail->next[i];    
        }    
    }    
}    
double dp[N][N][N];
int main () {
	freopen ("input.txt" , "r" , stdin);
	freopen ("output.txt" , "w" , stdout);
	int t , cas = 0;scanf ("%d" , &t);
	while (t --) {
		tot = 0;
		root = NewNode ();
		scanf ("%d %d %d %s %s" , &k , &l , &n , alpha , target);
		memset (cnt , 0 , sizeof (cnt));
		for (int i = 0 ; i < k ; i ++)
			cnt[alpha[i] - 'A'] ++;
	
		int can = 1;
		for (int i = 0 ; i < l ; i ++) {
			if (cnt[target[i] - 'A'] == 0)
				can = 0;
		}
		if (!can) {
			printf ("Case #%d: %.10f\n" , ++ cas , 0);
			continue;
		}

	
		for (int i = 0 ; i < 26 ; i ++) {

	
			cnt[i] = cnt[i] / (k * 1.0);
		}
		Insert (root , target , l);
		Bulid_fail (root);
		memset (dp , 0 , sizeof (dp));
		dp[0][0][0] = 1.0;
		for (int i = 0 ; i < n ; i ++) {
			for (int j = 0 ; j < tot ; j ++) {
				for (int k = 0 ; k <= i ; k ++) {
					if (dp[i][j][k] < 1e-6) continue;
					for (int r = 0 ; r < 26 ; r ++) {
						int c = k;
						int pre = j , nxt = s[pre].next[r] - s;
						if (s[nxt].end) c ++;
						// cout << pre << " " << nxt << " " << cnt[r] << endl;
						dp[i + 1][nxt][c] += dp[i][j][k] * cnt[r];
					}
				}
			}
		} 
		double ans = 0.0;
		for (int i = 0 ; i < tot ; i ++) {
			for (int j = 1 ; j <= n ; j ++) {
				ans += dp[n][i][j] * j;
			}
		}

		int fail = 0;
		for (int i = 1 ; i < l ; i ++) {
			int ok = 1;
			for (int j = 0 ; j < i ; j ++) {
				if (target[j] != target[l - i + j])
					ok = 0;
			}
			if (ok) fail = i;
		}
		double mx = 0;

		if (n >= l) {
			mx = 1 + (n - l) / (l - fail);
		}
		printf ("Case #%d: %.10f\n" , ++ cas , mx - ans);
	}
	return 0;
}