#include<bits/stdc++.h>
#define pic pair<int, char>
#define mk make_pair
#define ll long long
using namespace std;

string s, cad;
int caso = 0;

pic mul( pic a , pic b ){
	int a1 = a.first , b1 = b.first;
	char a2 = a.second , b2  =b.second;
	int flag = a1^b1;
	if( a2 == '1' ){
		if( b2 == '1') return mk( flag , '1' );	
		if( b2 == 'i') return mk( flag , 'i' );
		if( b2 == 'j') return mk( flag , 'j' );
		if( b2 == 'k') return mk( flag , 'k' );
	}
	if( a2 == 'i' ){
		if( b2 == '1') return mk( flag , 'i' );	
		if( b2 == 'i') return mk( flag^1 , '1' );
		if( b2 == 'j') return mk( flag , 'k' );
		if( b2 == 'k') return mk( flag^1 , 'j' );
	}
	if( a2 == 'j' ){
		if( b2 == '1') return mk( flag , 'j' );	
		if( b2 == 'i') return mk( flag ^1, 'k' );
		if( b2 == 'j') return mk( flag^1 , '1' );
		if( b2 == 'k') return mk( flag , 'i' );
	}
	if( a2 == 'k' ){
		if( b2 == '1') return mk( flag , 'k' );	
		if( b2 == 'i') return mk( flag , 'j' );
		if( b2 == 'j') return mk( flag ^1, 'i' );
		if( b2 == 'k') return mk( flag ^1, '1' );
	}
	
}

void doit(){
	int L;
	ll x;
	cin>>L>>x;
	cin>>s;
	cad ="";
	string aux ="";
	ll xaux = x%4;
	for( int i =0 ; i<xaux ; ++i ) aux+=s;
	pic ans = mk( 0 ,'1');
	int len = aux.size();
	for( int i=0 ; i<len ; ++i ){
		ans = mul( ans , mk( 0 , aux[ i ] ) );
	}
	if( ans != mk( 1 , '1') ){
		printf("Case #%d: NO\n" , ++caso );
		return;
	}
	ll total = L*x;
	x = min( 4LL, x );
	for( int i =0 ; i<x ; ++i ) cad+=s;
	int sz = L*x;
	ans = mk( 0 , '1');
	ll izq = -1 , der = -1;
	for( int i=0 ; i<sz ; ++i ){
		ans = mul( ans , mk( 0 , cad[ i ] ) );
		if( ans == mk( 0 , 'i') && izq==-1 ) izq = i; 
	}
	ans = mk( 0 , '1');
	for( int i=sz-1 ; i>=0 ; i-- ){
		ans = mul( mk( 0 , cad[ i ] ) , ans );
		if( ans == mk( 0 , 'k') && der==-1 ) der = i; 
	}
	//cout<<"izqeuiera: "<<der<<endl;
	if( der!=-1 ) der = total - ( sz - der );
	if( izq !=-1 && der !=-1 && izq < der ) printf("Case #%d: YES\n" , ++caso );
	else printf("Case #%d: NO\n" , ++caso );
}

int main(){
	int tc;
	cin>>tc;
	while( tc-- ) doit();
}
