#include <cstdio>
#include <algorithm>
const int MAXN=105;
struct node{
	char c;
	int cnt;
};
bool cmp(node n1,node n2){
	return n1.cnt<n2.cnt;
}
int main(){
	int T;
	node s[MAXN][MAXN];
	scanf("%d",&T);
	for(int caseNumber=1;caseNumber<=T;++caseNumber){
		int n,cnt,len,len0,sum=0;
		char c,c0;
		bool flag=true;
		scanf("%d",&n);
		for(int i=0;i<n;++i){
			for(;!(('a'<=c)&&(c<='z'));scanf("%c",&c));
			c0=0;
			len=0;
			for(;('a'<=c)&&(c<='z');){
				c0=c;
				cnt=1;
				s[len][i].c=c;
				for(scanf("%c",&c);c0==c;scanf("%c",&c)) ++cnt;
				s[len][i].cnt=cnt;
				++len;
			}
			if(i){
				if(len!=len0){
					flag=false;
					break;
				}
			}else len0=len;
		}
		if(flag){
			for(int i=0;i<len;++i){
				for(int j=1;j<n;++j)
					if(s[i][j].c!=s[i][0].c){
						flag=false;
						break;
					}
				if(flag){
					int tmp;
					std::sort(&(s[i][0]),&(s[i][n]),cmp);
					if(n%2) tmp=s[i][n>>1].cnt;
					else tmp=(s[i][(n>>1)-1].cnt+s[i][n>>1].cnt)>>1;
					for(int j=0;j<n;++j) sum+=abs(tmp-s[i][j].cnt);
				}
			}
		}
		printf("Case #%d: ",caseNumber);
		if(flag) printf("%d",sum);
		else printf("Fegla Won");
		printf("\n");
	}
}
