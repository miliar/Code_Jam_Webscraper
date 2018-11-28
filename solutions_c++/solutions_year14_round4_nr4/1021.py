#include <iostream>
#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include <map>
using namespace std;
int T , N , M , C = 1;
map<int,int> MAP;
string s[10];
char G[101];
struct XD{
	XD( int x , int y ):cnt(x),data(y),bottom(nullptr),right(nullptr){}
	XD *bottom , *right;
	int cnt , data;
};
XD *head[11];
int cnt , off;
bool vst[11];
void Insert( char *p , XD *fa ,XD *ptr ){
	if ( *p == 0) return;
	if ( ptr == nullptr ){
		cnt++;
		ptr = new XD( 1 , *p );
		fa->bottom = ptr;
		Insert( p+1 , ptr , ptr->bottom );	
	}
	else{
		if ( ptr->data == *p ){
			ptr->cnt++;
			if ( ptr->cnt == 1 ) cnt++;
			Insert( p+1 , ptr , ptr->bottom );	
		}
		else{
			XD *pre = ptr;
			ptr = pre -> right;
			while ( ptr != nullptr && ptr->data != *p )
				pre = ptr , ptr = ptr -> right;
			if ( ptr == nullptr ){
				ptr = new XD( 1 , *p );
				cnt++;
				pre->right = ptr;
				Insert( p+1 , ptr , ptr->bottom );
			}
			else{
				ptr->cnt++;
				if ( ptr->cnt==1 ) cnt++;
				Insert( p+1 , ptr , ptr->bottom );	
			}
		}
	}
	
}
void Delete( char *p , XD *ptr ){
	if ( *p == 0 ) return;
	while ( ptr->data != *p ) ptr = ptr->right;
	ptr->cnt--;
	if ( ptr->cnt == 0 )
		cnt--;
	Delete( p+1 , ptr->bottom );	
}
void Brutal( int cur ){
	if ( cur > M ){


		MAP[cnt+off]++;
		return;
	}
	for ( int i = 1 ; i <= N ; i++ ){
		bool ori = vst[i];
		if ( !ori ) vst[i] = true , off++;
		Insert( (char*)s[cur].c_str() , head[i] , head[i]->bottom );	
		Brutal( cur+1 );
		Delete(  (char*)s[cur].c_str() , head[i]->bottom );
		if ( !ori ) vst[i] = false , off--;
	}

	
}
int main(){
	freopen("D-small-attempt0.in","r",stdin);
	freopen("outputD.txt","w",stdout);
	scanf("%d",&T);
	while ( T-- ){
		MAP.clear();
		cnt = off = 0;
		memset( vst , 0 , sizeof( vst ) );
		scanf("%d%d",&M,&N);
		for ( int i = 1 ; i <= N ; i++ )
			head[i] = new XD(0,0);
		for ( int i = 1 ; i <= M ; i++ ){
			cin>>G;
			s[i] = string( G );
		}
		Brutal( 1 );
		int a1 , a2;
		map<int,int>::iterator it=MAP.begin();
		while ( it != MAP.end() )
			a1 = it->first , a2 = it->second , ++it;
		printf("Case #%d: %d %d\n",C++,a1,a2);
	}


	return 0;
}
