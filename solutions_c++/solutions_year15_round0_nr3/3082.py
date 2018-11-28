#include<bits/stdc++.h>
#define mxn 10005
using namespace std;

int l,x;
int id,test;
int suf[mxn];
char str[mxn];
int ar[mxn];

int mat[5][5] = {
	{0,0,0,0,0},
	{0,1,2,3,4},
	{0,2,-1,4,-3},
	{0,3,-4,-1,2},
	{0,4,3,-2,-1}
};

int main(){
	
	freopen( "input.txt"  , "r" , stdin );
	freopen( "output.txt" , "w" , stdout);
	
	int n,i,j,flag,a,b;
	
	scanf( "%d" , &test );
	
	for( id=1 ; id<=test ; id++ ){
	
		scanf( "%d %d" , &l , &x );
		scanf( "%s" , str+1 );
		
		for( i=1 ; i<=l ; i++ )
		switch( str[i] ){
			case '1': ar[i] = 1; break;
			case 'i': ar[i] = 2; break;
			case 'j': ar[i] = 3; break;
			case 'k': ar[i] = 4; break;
		}
		
		for( i=1 ; i<=l ; i++ )
		for( j=0 ; j<x ; j++ )
			ar[l*j+i] = ar[i];
		
		n = l*x;
		suf[n] = ar[n];
		for( i=n-1 ; i>=1 ; i-- )
			if( ar[i]*suf[i+1]<0 )	suf[i] = -mat[ abs(ar[i]) ][ abs(suf[i+1]) ];
			else 					suf[i] =  mat[ abs(ar[i]) ][ abs(suf[i+1]) ];
		
		a = 1;
		flag = false;
		for( i=1 ; !flag && i<=n ; i++ ){
			
			if( a*ar[i]<0 )	a = -mat[abs(a)][abs(ar[i])];
			else			a =  mat[abs(a)][abs(ar[i])];
			
			if( a==2 ){
				
				b = 1;
				for( j=i+1 ; !flag && j+1<=n ; j++ ){
					
					if( b*ar[j]<0 )		b = -mat[abs(b)][abs(ar[j])];
					else				b =  mat[abs(b)][abs(ar[j])];
					if( b==3 && suf[j+1]==4 )		flag = 1;
					
				}
				
			}
		
		}
		
		if( flag==true )	printf( "Case #%d: YES\n" , id );
		else 				printf( "Case #%d: NO\n"  , id );
		
	}
	
	return 0;
	
}
