#include <cstdio>
#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;

bool org[10][10], makeup[10][10], g[10][10];
int d[10][10], dn, nn;

int countbit(int x){
	int ret = 0;
	while (x){
		ret += x&1;
		x>>=1;
	}
	return ret;
}


bool s[100];
int x[100];

bool path( int i ){
	for (int j=1; j<=nn; j++)
	if ( !s[j] && g[i][j] ){
		s[j] = true;
		if ( !x[j] || path( x[j] ) ){
			x[j] = i;
			return true;
		}
	}
	return false;
}

bool canmatch(int n){
	nn = n;

	memset( x, 0, sizeof(x) );
	for (int i=1; i<=nn; i++){
		memset( s, 0, sizeof(s) );
		if ( !path( i ) ) return false;
	}
	return true;
}

int main()
{
	freopen("D-small-attempt0.in","r",stdin);
	freopen("small.out","w",stdout);
	
	int task; scanf("%d", &task);
	for (int cs=1; cs<=task; cs++){
		int n;
		scanf("%d", &n);
		dn = 0;
		for (int i=1; i<=n; i++)
		for (int j=1; j<=n; j++){
			char ch;
			do{
				scanf("%c", &ch);
			}while (!(ch=='1' || ch=='0'));
				
			org[i][j] = (ch=='1');
			if (!org[i][j]){
				d[i][j] = dn;
				dn++;
			}
		}

		int ret = 100;
		for (int mask=0; mask<(1<<dn); mask++){
			//cout<<"mask "<<mask<<endl;
			int current = countbit(mask);
			if (ret<=current) continue;

			for (int i=1; i<=n; i++)
			for (int j=1; j<=n; j++)
			if (org[i][j]){
				makeup[i][j] = true;
			}else{
				if (mask&(1<<d[i][j])){
					makeup[i][j] = true;
				}else{
					makeup[i][j] = false;
				}
			}

			for (int x=1; x<=n; x++){
			for (int y=1; y<=n; y++){
				//cout<<makeup[x][y];
				g[x][y] = makeup[x][y];
			}
			//cout<<endl;
			}

			if (canmatch(n)){
				//cout<<"go"<<endl;
				bool ok = true;
				
				for (int i=1; i<=n; i++){
					for (int j=1; j<=n; j++)
					if (!makeup[i][j]){
						for (int x=1; x<=n; x++)
						for (int y=1; y<=n; y++)
						if (x!=i && y!=j){
							int xx = x<i?x:x-1;
							int yy = y<j?y:y-1;
							g[xx][yy] = makeup[x][y];
						}

						if (canmatch(n-1)){
							ok = false;
							break;
						}
					}
					if (!ok) break;
				}

				if (ok){
					ret = current;
				}
			}
		}

		printf("Case #%d: %d\n", cs, ret);
	}	

	return 0;
}
