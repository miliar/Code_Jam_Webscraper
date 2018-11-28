#include<cstdio>
#include<iostream>
#include<cstring>
#include<string>
#include<algorithm>
#include<map>
#include<set>
#include<vector>
#include<queue>
#include<cmath>
using namespace std;
typedef long long LL;
#define mod 1000000007
#define DEBUG 0
#define N 2010
#define M 30

int T;
char s[N];
int f[M],d[M];
bool ans;

void dfs(int x){
	switch(x){
		case 0:
		for(int i=0;;i++){
			if(f['Z'-'A']>=i&&f['E'-'A']>=i&&f['R'-'A']>=i&&f['O'-'A']>=i){
				f['Z'-'A']-=i;
				f['E'-'A']-=i;
				f['R'-'A']-=i;
				f['O'-'A']-=i;
				d[x]=i;
				dfs(x+1);
				if(ans) return;
				f['Z'-'A']+=i;
				f['E'-'A']+=i;
				f['R'-'A']+=i;
				f['O'-'A']+=i;
			}else break;
		}
		break;
		case 1:
		for(int i=0;;i++){
			if(f['O'-'A']>=i&&f['N'-'A']>=i&&f['E'-'A']>=i){
				f['O'-'A']-=i;
				f['N'-'A']-=i;
				f['E'-'A']-=i;
				d[x]=i;
				dfs(x+1);
				if(ans) return;
				f['O'-'A']+=i;
				f['N'-'A']+=i;
				f['E'-'A']+=i;
			}else break;
		}
		break;
		case 2:
		for(int i=0;;i++){
			if(f['T'-'A']>=i&&f['W'-'A']>=i&&f['O'-'A']>=i){
				f['T'-'A']-=i;
				f['W'-'A']-=i;
				f['O'-'A']-=i;
				d[x]=i;
				dfs(x+1);
				if(ans) return;
				f['T'-'A']+=i;
				f['W'-'A']+=i;
				f['O'-'A']+=i;
			}else break;
		}
		break;
		case 3:
		for(int i=0;;i++){
			if(f['T'-'A']>=i&&f['H'-'A']>=i&&f['R'-'A']>=i&&f['E'-'A']>=i*2){
				f['T'-'A']-=i;
				f['H'-'A']-=i;
				f['R'-'A']-=i;
				f['E'-'A']-=i*2;
				d[x]=i;
				dfs(x+1);
				if(ans) return;
				f['T'-'A']+=i;
				f['H'-'A']+=i;
				f['R'-'A']+=i;
				f['E'-'A']+=i*2;
			}else break;
		}
		break;
		case 4:
		for(int i=0;;i++){
			if(f['F'-'A']>=i&&f['O'-'A']>=i&&f['U'-'A']>=i&&f['R'-'A']>=i){
				f['F'-'A']-=i;
				f['O'-'A']-=i;
				f['U'-'A']-=i;
				f['R'-'A']-=i;
				d[x]=i;
				dfs(x+1);
				if(ans) return;
				f['F'-'A']+=i;
				f['O'-'A']+=i;
				f['U'-'A']+=i;
				f['R'-'A']+=i;
			}else break;
		}
		break;
		case 5:
		for(int i=0;;i++){
			if(f['F'-'A']>=i&&f['I'-'A']>=i&&f['V'-'A']>=i&&f['E'-'A']>=i){
				f['F'-'A']-=i;
				f['I'-'A']-=i;
				f['V'-'A']-=i;
				f['E'-'A']-=i;
				d[x]=i;
				dfs(x+1);
				if(ans) return;
				f['F'-'A']+=i;
				f['I'-'A']+=i;
				f['V'-'A']+=i;
				f['E'-'A']+=i;
			}else break;
		}
		break;
		case 6:
		for(int i=0;;i++){
			if(f['S'-'A']>=i&&f['I'-'A']>=i&&f['X'-'A']>=i){
				f['S'-'A']-=i;
				f['I'-'A']-=i;
				f['X'-'A']-=i;
				d[x]=i;
				dfs(x+1);
				if(ans) return;
				f['S'-'A']+=i;
				f['I'-'A']+=i;
				f['X'-'A']+=i;
			}else break;
		}
		break;
		case 7:
		for(int i=0;;i++){
			if(f['S'-'A']>=i&&f['E'-'A']>=i*2&&f['V'-'A']>=i&&f['N'-'A']>=i){
				f['S'-'A']-=i;
				f['E'-'A']-=i*2;
				f['V'-'A']-=i;
				f['N'-'A']-=i;
				d[x]=i;
				dfs(x+1);
				if(ans) return;
				f['S'-'A']+=i;
				f['E'-'A']+=i*2;
				f['V'-'A']+=i;
				f['N'-'A']+=i;
			}else break;
		}
		break;
		case 8:
		for(int i=0;;i++){
			if(f['E'-'A']>=i&&f['I'-'A']>=i&&f['G'-'A']>=i&&f['H'-'A']>=i&&f['T'-'A']>=i){
				f['E'-'A']-=i;
				f['I'-'A']-=i;
				f['G'-'A']-=i;
				f['H'-'A']-=i;
				f['T'-'A']-=i;
				d[x]=i;
				dfs(x+1);
				if(ans) return;
				f['E'-'A']+=i;
				f['I'-'A']+=i;
				f['G'-'A']+=i;
				f['H'-'A']+=i;
				f['T'-'A']+=i;
			}else break;
		}
		break;
		case 9:
		int y=f['I'-'A'];
		if(f['N'-'A']==y*2&&f['E'-'A']==y){
			ans=true;
			d[x]=y;
			for(int i=0;i<26;i++){
				if(i!=('E'-'A')&&i!=('I'-'A')&&i!=('N'-'A')){
					if(f[i]){
						ans=false;
						break;
					}
				}
			}
		}
		break;
	}
}

int main(){
	if(!DEBUG){
		freopen("in.in","r",stdin);
		freopen("out.out","w",stdout);
	}
    scanf("%d",&T);
    for(int t=1;t<=T;t++){
    	scanf("%s",s);
    	int n=strlen(s);
    	for(int i=0;i<M;i++){
			f[i]=0;
    		d[i]=0;
    	}
    	for(int i=0;i<n;i++){
	    	f[s[i]-'A']++;
	    }
	    ans=false;
	    dfs(0);
        printf("Case #%d: ",t);
        for(int i=0;i<10;i++){
        	while(d[i]--) printf("%d",i);
        }
        printf("\n");
    }
    return 0;
}
