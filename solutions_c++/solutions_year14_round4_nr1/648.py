#include<stdio.h>
#include<queue>
#include<set>
#include<algorithm>
using namespace std;
priority_queue<int> pq;
int tab[20000];
int main(){
	int t;
	scanf("%d",&t);
	for(int e = 0 ; e< t ;e++ ){
		int n,m;
		scanf("%d %d",&n,&m);
		for(int i = 0 ;i < n ;i++ ) scanf("%d",&tab[i]);
		sort(tab,tab+n);
		int nbox = 1;
		for( ; ; nbox++ ){
			for( ; pq.size() > 0 ; pq.pop() );
			int chk = 1;
			for(int i = 0 ; i < nbox ; i++ ) pq.push(m);
			for(int i = n-1 ; i>=0 ; i-- ){
				if( pq.size() == 0 ) { chk = 0 ; break; }
				int left = pq.top();
				if( left < tab[i] ){
					chk = 0 ;
					break;
				}
				pq.pop();
				if( left == m ) pq.push(left-tab[i]);
			}
			if( chk ){
				printf("Case #%d: %d\n",e+1,nbox);
				break;
			}
		}
	}
}
