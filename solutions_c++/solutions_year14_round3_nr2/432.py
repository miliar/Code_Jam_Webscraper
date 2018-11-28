#include <iostream>
#include <math.h>
#include <algorithm>
#include <string>
#include <cstdio>

#define SC(x) scanf("%d", &x);
#define File freopen("input.txt","r",stdin); freopen("output.txt","w",stdout);

using namespace std;
const long long inf =2147483647;
const int md=1e9+7;
const double eps=1e-6;

int n,m,i,j,k,ttt,tt;
long long ans;
string s[500];
struct _c{
	int bgn,end,mid,ent;
	char next,pred;
} c[100500];
bool fl,f[500];
char tmp;

int fact(int k){
	long long res=1;
	for (int i=2; i<=k; i++)
		res=(res*i)%md;
	return res;
}

int main(){
	File;
	SC(ttt);
	for (tt=1; tt<=ttt; tt++){
		printf("Case #%d:",tt);
		scanf("%d",&n);
		for (char ch='a'; ch<='z'; ch++){
			c[ch].bgn=0;
			c[ch].end=0;
			c[ch].mid=0;
			c[ch].ent=0;
			c[ch].next=0;
			c[ch].pred=0;
			f[ch]=0;
		}
		for (i=1; i<=n; i++){
			cin>>s[i];
			m=0;
			for (j=1; j<s[i].size(); j++)
				if (s[i][j]!=s[i][m]){
					s[i][++m]=s[i][j];
				}
			if (m==0){
				c[s[i][0]].ent++;
			} else {
				c[s[i][0]].bgn++;
				c[s[i][m]].end++;
				c[s[i][0]].next=s[i][m];
				c[s[i][m]].pred=s[i][0];
				for (j=1; j<m; j++)
					c[s[i][j]].mid++;
			}
		}
		fl=1;
		for (char ch='a'; ch<='z'; ch++){
			if (c[ch].mid>1 || (c[ch].mid==1 && (c[ch].bgn || c[ch].end || c[ch].ent))){
				fl=0;
				break;
			}
			if (c[ch].bgn>1 || c[ch].end>1){
				fl=0;
				break;
			}
		}
		if (!fl){
			printf(" 0\n");
			continue;
		}
		m=0;
		ans=1;
		for (char ch='a'; ch<='z'; ch++){
			if (c[ch].end!=0) continue;
			if (c[ch].bgn!=0 || c[ch].bgn==0 && c[ch].ent>0) m++;
			tmp=ch;
			while (!f[tmp]){
				f[tmp]=1;
				if (c[tmp].bgn!=0)
					tmp=c[tmp].next;
				else break;
			}
		}
		for (char ch='a'; ch<='z'; ch++){
			ans=(ans*fact(c[ch].ent))%md;
			if (f[ch]) continue;
			if (c[ch].bgn || c[ch].end){
				fl=0;
				break;
			}
			//if (c[ch].ent) m++;
		}
		if (!fl){
			printf(" 0\n");
			continue;
		}
		ans=(ans*fact(m))%md;
		printf(" %lld",ans);
		printf("\n");
	}
	return 0;
}
