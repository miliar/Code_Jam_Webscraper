#include<stdio.h>
#include<algorithm>
#include<set>
#include<string>
#include<iostream>
#include<unordered_map>

using namespace std;

#define maxn 10005
#define inf (1<<29)

int words,servers;
int maxnoduri = 0,nrmax = 1;
int x[maxn],apare[maxn];
string s[maxn];
unordered_map<string,int>M[maxn];

void back ( int niv ){
	if ( niv == words+1 ){
		
		for ( int i = 1 ; i <= servers ; ++i ){
			apare[i] = 0;
		}
		for ( int i = 1 ; i <= words ; ++i ){
			apare[x[i]] = 1;
		}
		for ( int i = 1 ; i <= servers ; ++i ){
			if ( !apare[i] )	return ;
		}
		
		for ( int i = 1 ; i <= servers ; ++i )	M[i].clear();
		
		int nodes = 0;
		for ( int i = 1 ; i <= words ; ++i ){
			
			string pref = "";
			if ( !M[x[i]][pref] ){
				++nodes; M[x[i]][pref] = 1;
			}
			for ( int j = 0 ; j < (int)s[i].size() ; ++j ){
				pref += s[i][j];
				if ( !M[x[i]][pref] ){
					++nodes; M[x[i]][pref] = 1;
				}
			}
		}
		
		if ( nodes > maxnoduri ){
			maxnoduri = nodes;
			nrmax = 1;
		}
		else{
			if ( nodes == maxnoduri )	++nrmax;
		}
		
		return ;
	}
	
	for ( int i = 1 ; i <= servers ; ++i ){
		x[niv] = i;
		back(niv+1);
		x[niv] = 0;
	}
}

int main () {
	
	freopen("codejam.in","r",stdin);
	freopen("codejam.out","w",stdout);
	
	int tests;
	scanf("%d",&tests);
	
	for ( int ii = 1 ; ii <= tests ; ++ii ){
		
		scanf("%d %d",&words,&servers);
		for ( int i = 1 ; i <= words ; ++i ){
			cin >> s[i];
		}
		
		back(1);
		
		printf("Case #%d: %d %d\n",ii,maxnoduri,nrmax);
		maxnoduri = 0,nrmax = 1;
		fprintf(stderr,"%d\n",ii);
	}
	
	return 0;
}
