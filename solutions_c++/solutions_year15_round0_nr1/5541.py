#include <algorithm>
#include <cstdio>
#include <iostream>

using namespace std;

const int MAXN=1024;

int T,S;
int ar[MAXN];

int main(){
	
	scanf("%d",&T);
	
	for( int Case=1 ; Case<=T ; Case++ ){
		
		int res=0,cur=0;
		char ch;
		
		scanf("%d",&S);
		
		for( int i=0 ; i<=S ; i++ ){
			scanf(" %c",&ch);
			ar[i]=ch-'0';
		}
		
		cur=ar[0];
		for( int i=1 ; i<=S ; i++ ){
			if( ar[i] && i>cur ){
				res+=i-cur;
				cur+=i-cur;
			}
			cur+=ar[i];
		}
		
		printf("Case #%d: %d\n",Case,res);
	}
	
	return 0;
}