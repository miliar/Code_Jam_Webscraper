#include <stdio.h>
#include <string.h>
char s[100][100];
int n,m;
int where[100];
int count[100];
int ind[100][100];
char list[1000][100];
int nlist;
int maxx = 0;
int nmaxx = 0;
int solve(){
	char tmp[100];
	int ans = 0;
	for(int g = 0 ; g < m ; g++ ){
		int ct = 0;
		nlist = 0;
		for(int k = 0 ; k < count[g] ; k++){
			char *mys = s[ind[g][k]] ;
			int lens = strlen(mys);
			for(int ki = 0 ; ki < lens ; ki++ ){
				for(int i = 0 ; i <= ki ; i++ ) tmp[i] = mys[i];
				tmp[ki+1] = 0;
				int chk = 1;
				for(int i = 0 ; i < nlist ; i++ ){
					if( strcmp(tmp,list[i]) == 0 ) {
						chk = 0;
						break;
					}
				}
				if( chk ){
					strcpy(list[nlist],tmp);
					nlist++;
					ct++;
				}
			}
		}
		ct++;
		ans+= ct;
	}
	return ans;
}

int rec(int k){
	if( k == n ){
		for(int i = 0 ;i  < m ; i++ ) count[i] = 0;
		for(int i = 0 ;i < n ; i++ ){
			ind[where[i]][ count[where[i]] ] = i;
			count[where[i]]++;
		}
		int chk = 0;
		for(int i = 0 ; i < m ; i++ ){
			if( count[i] == 0 ) chk = 1;
		}
		if( chk ) return 0;
		//for(int i = 0 ; i < n ; i++ ) printf("%d ",where[i]);
		int ans = solve();
		//printf("= %d\n",ans);
		//printf("\n");
		if( ans > maxx ) {
			maxx = ans;
			nmaxx = 1;
		}else if( ans == maxx ){
			nmaxx++;
		}
		return 0;
	}
	for(int i = 0 ; i < m ; i++ ){
		where[k] = i;
		rec(k+1);
	}
}
int main(){
	int t;
	scanf("%d",&t);
	for(int e = 0 ; e < t ; e++ ){
		nmaxx =0;
		maxx = 0;
		scanf("%d %d",&n,&m);
		for(int i = 0 ; i < m ; i++ ) count[i] = 0;
		for(int i = 0 ; i < n ; i++ ){
			scanf("%s",s[i]);	
		}
		rec(0);
		printf("Case #%d: %d %d\n",e+1,maxx,nmaxx);
	}
}
