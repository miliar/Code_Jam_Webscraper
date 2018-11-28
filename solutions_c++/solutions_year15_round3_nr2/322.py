#include<bits/stdc++.h>
using namespace std;

const int N = 300;

int cnt[N];


string keys,pat;
vector<int> pi;

vector < int > prefix_function ( string s ) {
	int n = ( int ) s. length ( ) ;
	vector < int > pi ( n ) ;
	for ( int i = 0 ; i < n ; ++ i )
		for ( int k = 0 ; k <= i ; ++ k )
			if ( s. substr ( 0 ,k ) == s. substr ( i - k + 1 ,k ) )
				pi [ i ] = k ;
	return pi ;
}
int k,l,s;


bool vst[N][N];
double dp[N][N];

double f(int pos,int match)
{


  //  cout<<pos<<" "<<match<<endl;
  //  cout<<s<<" "<<l<<endl;

    double &ret=dp[pos][match];
    if( vst[pos][match] )return ret;
    vst[pos][match]=1;

    if( match==l )return ret=1.0+f( pos, pi[ match-1 ]  );
    if(pos==s)return ret=0.0;

    ret=0;

    int i;

    for( i=0;i<26;i++ )
    {
        int j=match;
       // cout<<"(";
        while( j && pat[j]!=i+'A' ){j=pi[j-1];}
       // cout<<")";

       // if( pos==1 && match==1 )cout<<(char)(i+'A')<<" "<<j<<" "<<pat[j]<<endl;

        if( pat[j]==i+'A' )j++;



        ret+=(double)(cnt[i]*f(pos+1,j))/(double)k;
    }




    return ret;
}



int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B_large_out.txt","w",stdout);

    int T,need,i,j;
    cin>>T;

    for( int ks=1;ks<=T;ks++ )
    {
        cin>>k>>l>>s;
        cin>>keys>>pat;

        if( s<pat.size() ){ printf("Case #%d: %.10lf\n",ks,0.0); continue; }


        memset(cnt,0,sizeof(cnt));


        for(i=0;keys[i];i++ )cnt[keys[i]-'A']++;

        for( i=0;pat[i];i++ )if(!cnt[ pat[i]-'A' ])break;
        if( pat[i] ){ printf("Case #%d: %.10lf\n",ks,0.0); continue; }


        need=0;

        pi=prefix_function( pat );



        need=1+(s-l)/(l-pi[l-1]);

//        printf("%d->>%d\n",ks,need);

        memset(vst,0,sizeof(vst));
        double ex=f( 0,0 );

       // cout<<"e";

        printf("Case #%d: %.10lf\n",ks,need-ex);
       // while(1);


    }
    return 0;
}
