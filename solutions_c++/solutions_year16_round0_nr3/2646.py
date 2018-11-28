// Bismillahirrahmanirrahim
#include <bits/stdc++.h>
using namespace std;
typedef long long int Lint;
typedef pair < int , int > pii;
typedef pair < int , pii > piii;
#define foreach(_i,x)  for(__typeof(x.begin()) _i=x.begin() ; _i != x.end() ; _i++)
#define yeral() (struct node *)calloc(1,sizeof(struct node))
#define all(x) x.begin(),x.end()
#define mod 1000000007
#define pb push_back
#define mp make_pair
#define maxn 100005
#define sc second
#define ft first

int main(){
	freopen("C-small-attempt3.in","r",stdin);
	freopen("cikar.out","w",stdout);
		printf("Case #1:\n");
	printf("1111111111111111 3 2 5 2 7 2 3 2 11 \n");
	printf("1111111111111001 3 2 5 2 7 2 3 2 7 \n");
	printf("1111111111110111 7 13 3 31 5 3 59 7 3 \n");
	printf("1111111111110101 5 2 17 2 19 2 5 2 101 \n");
	printf("1111111111110011 3 2 5 2 7 2 3 2 11 \n");
	printf("1111111111101101 3 2 5 2 7 2 3 2 11 \n");
	printf("1111111111101011 5 2 17 2 37 2 5 2 101 \n");
	printf("1111111111100111 3 2 5 2 7 2 3 2 11 \n");
	printf("1111111111100001 3 2 3 2 7 2 3 2 3 \n");
	printf("1111111111011111 31 7 3 11 5 3 31 11 3 \n");
	printf("1111111111011101 17 2 257 2 73 2 7 2 19 \n");
	printf("1111111111011011 3 2 5 2 7 2 3 2 11 \n");
	printf("1111111111010111 5 2 17 2 37 2 5 2 101 \n");
	printf("1111111111001111 3 2 5 2 7 2 3 2 11 \n");
	printf("1111111111001101 5 7 23 21017 11 5 41 7 7 \n");
	printf("1111111111001011 11 1553 7 7 13613 67 181 103 197 \n");
	printf("1111111111001001 3 2 3 2 7 2 3 2 3 \n");
	printf("1111111111000011 3 2 3 2 7 2 3 2 3 \n");
	printf("1111111110111111 7 13 3 31 5 3 73 7 3 \n");
	printf("1111111110111101 3 2 5 2 7 2 3 2 11 \n");
	printf("1111111110111011 17 2 19 2 47 2 7 2 73 \n");
	printf("1111111110110111 3 2 5 2 7 2 3 2 11 \n");
	printf("1111111110110001 3 2 3 2 7 2 3 2 3 \n");
	printf("1111111110101111 5 2 17 2 11 2 5 2 7 \n");
	printf("1111111110100101 3 2 3 2 7 2 3 2 3 \n");
	printf("1111111110100011 7 2 3 2 43 2 73 2 3 \n");
	printf("1111111110011111 3 2 5 2 7 2 3 2 11 \n");
	printf("1111111110011001 3 2 3 2 7 2 3 2 3 \n");
	printf("1111111110010101 7 2 3 2 43 2 11 2 3 \n");
	printf("1111111110010011 3 2 3 2 7 2 3 2 3 \n");
	printf("1111111110001101 3 2 3 2 7 2 3 2 3 \n");
	printf("1111111110000111 3 2 3 2 7 2 3 2 3 \n");
	printf("1111111110000001 3 2 5 2 5 2 3 2 11 \n");
	printf("1111111101111101 5 2 7 2 11 2 5 2 79 \n");
	printf("1111111101111011 3 2 5 2 7 2 3 2 7 \n");
	printf("1111111101111001 7 29 83 41 19 13 15551 7 191 \n");
	printf("1111111101110111 17 2 29 2 1297 2 7 2 73 \n");
	printf("1111111101110101 3 7 13 3 31 43 3 73 7 \n");
	printf("1111111101101111 3 2 5 2 7 2 3 2 11 \n");
	printf("1111111101101001 3 2 3 2 7 2 3 2 3 \n");
	printf("1111111101100111 151 5 10987 307 647 2887 5 11 3148829 \n");
	printf("1111111101100011 3 2 3 2 7 2 3 2 3 \n");
	printf("1111111101100001 13 19 7 733 67 5869 29 1171 31 \n");
	printf("1111111101011111 5 2 17 2 37 2 5 2 101 \n");
	printf("1111111101011101 3 523 19 3 149 967 3 7 2689 \n");
	printf("1111111101011001 131 2 3 2 13 2 79 2 3 \n");
	printf("1111111101010101 5 2 3 2 37 2 5 2 3 \n");
	printf("1111111101010001 3 7 13 3 31 43 3 73 7 \n");
	printf("1111111101001011 3 2 3 2 7 2 3 2 3 \n");
	printf("1111111101000111 11 2 3 2 29 2 459013 2 3 \n");
	return 0;
}

//~ Lint a,b,q[50],cnt;
//~ Lint w[12];
//~ 
//~ Lint asal ( Lint x ){
	//~ for ( Lint i = 2 ; i*i <= x ; i++ )
		//~ if ( x%i == 0 )
			//~ return i;
	//~ 
	//~ return 0;
//~ }
//~ 
//~ Lint onluk;
//~ 
//~ Lint translate( Lint k ){
	//~ 
	//~ Lint kat = 1,ret =0;
	//~ 
	//~ for ( Lint i = a ; i >= 1 ; i--,kat *= k )
		//~ ret += q[i] * kat;
	//~ 
	//~ return ret;
//~ }
//~ 
//~ void f ( Lint cur ){
	//~ 
	//~ if ( cur > a ){
		//~ 
		//~ if ( q[1] == 0 || q[a] == 0 )
			//~ return ;
			//~ 
		//~ for ( Lint i = 2 ; i <= 10 ; i++ ){
			//~ w[i] = asal(translate(i));
			//~ if ( !w[i] )
				//~ return ;
		//~ }
		//~ printf("printf(\"");
		//~ for ( Lint i = 1 ; i <= a ; i++ )
			//~ printf("%lld",q[i]);
		//~ printf(" ");
		//~ 
		//~ for ( Lint i = 2 ; i <= 10 ; i++ )
			//~ printf("%lld ",w[i]);
		//~ printf("\\n\"");
		//~ printf(");");
		//~ puts("");
		//~ 
		//~ cnt ++;
		//~ return ;
	//~ }
	//~ 
	//~ q[cur] = 1;
	//~ f ( cur+1 );
	//~ 
	//~ if ( cnt == b )
		//~ return ;
		//~ 
	//~ q[cur] = 0;
	//~ f ( cur+1 );
//~ }
//~ 
//~ Lint cse;
//~ 
//~ void solve(){
	//~ 
	//~ scanf("%lld %lld",&a,&b);	
	//~ if ( b == 0 )
		//~ return ;
	//~ cnt = 0;
	//~ 
	//~ cse++;
//	printf("printf(\""):
	//~ printf("printf(\"");
	//~ printf("Case #%lld:\\n",cse);
//	printf("\");\n");
	//~ printf("\\n\");");
	//~ puts("");
	//~ 
	//~ f ( 1 );
	//~ 
//~ }
//~ 
//~ int main()
//~ {	
	//~ freopen("C-small-attempt0.in","r",stdin);
	//~ freopen("C-small-attempt0.out","w",stdout);
	//~ 
	//~ Lint T;	
	//~ scanf("%lld",&T);
	//~ 
	//~ while ( T-- )
		//~ solve();
	//~ 
	//~ return 0;
//~ }
