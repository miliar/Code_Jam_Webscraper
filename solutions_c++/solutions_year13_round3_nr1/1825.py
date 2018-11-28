#include <cstdio>
#include <cstring>
#include <set>
using namespace std;

bool cons(char a){
	return (!(a=='a'||a=='e'||a=='i'||a=='u'||a=='o'));
}

int main(){
	int t, n;
	scanf(" %d ", &t);
	char word[1000005];
	for(int x = 1; x<=t;x++){
		set<int> pos;
		bool is[1000005];
		memset(is, 0, sizeof(is));
		scanf(" %s %d ", word, &n);
		int s=0, e=0, c=0, prev=0;
		if(cons(word[0])) c = 1;
		prev = cons(word[0]);
		if(c >= n) pos.insert(0);
		while(e < strlen(word)-1){
			if(!cons(word[e])){
				c = 0;
			}
			if(c < n){
				e++;
				if(cons(word[e])){
					if(prev) c++;
					else c=1;
				}
				else{
					c=0;
				}
			}
			else{
				if(cons(word[s])) c--;
				s++;
			}
			if(c >= n){
				pos.insert(e);
			}
//			printf("%d %d %d\n", x, s, e);
			prev = cons(word[e]);
		}

//		printf("HERE\n");
		set<int>::iterator it;
		it = pos.begin();

		long long ans = 0;
		for(int i = 0; i < strlen(word); i++){
			int val = i+n-1;
			it=pos.upper_bound(val-1);
			if(it != pos.end()){
				ans += (strlen(word)-(*it));
//				printf("HERE %d %d %d\n", i, *it, ans);
			}
		}
		printf("Case #%d: %lld\n", x, ans);
	}
	return 0;
}
