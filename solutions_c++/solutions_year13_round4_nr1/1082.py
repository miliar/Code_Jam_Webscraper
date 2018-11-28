#include<iostream>
#include<cstdio>
#include<string>
#include<algorithm>
#include<cmath>
#include<string.h>
#include<map>
//#include<pair>
using namespace std;

const long long Mod = 1000002013;
const long long Mod0 = 41;
const long long Mod1 = 181;
const long long Mod2 = 134753;

	static long long Gcd( long long a, long long b ){
		if( a < b ) swap( a, b );
		while( b!=0 ){ swap( a, b ); b %= a; }
		return a;
	}
	// calculate gcd(a,b) and the integer x and y where gcd(a,b)=a*x+b*y
	static long long Ext_Gcd( long long a, long long b, long long &x, long long &y ){
		if( b == 0 ){ x = 1; y = 0; return a; }
		long long d = Ext_Gcd( b, a%b, x, y );
		long long t = x;  x = y;  y = t-a/b*y;
		return d;
	}
	// get the smallest positive answer x where x % m1 = a1 and x % m2 = a2
	static long long Mod_L_EQ( long long a1, long long m1, long long a2, long long m2 ){
		long long x, y, c = Gcd( m1, m2 );
		if( abs(a1-a2)%c != 0 ) return -1;
		Ext_Gcd( m2/c, m1/c, x, y );
		x = a2+m2*(x*(a1-a2)/c);
		y = m1*m2/c;
		x %= y;
		return ( x<0 ? x+y:x );
	}

int main(){
    //for(int i=2; i<1000000; i++) if( Mod%i==0 ){ printf("%d ",i); }
    //cout<<endl;
    int T, n, m, o, e, p;
    scanf("%d",&T);
    for(int t=1; t<=T; t++){
        map<long long,long long> mp;
        map<long long,long long>::iterator it;
        scanf("%d%d",&n,&m);
        long long cost0 = 0, cost1 = 0, cost2 = 0;
        long long use0 = 0, use1 = 0, use2 = 0;
        for(int i=0; i<m; i++){
            scanf("%d%d%d",&o,&e,&p);
            cost0 = (cost0+(long long)(n+n-e+o+1)*(e-o)/2*p) % Mod0;
            cost1 = (cost1+(long long)(n+n-e+o+1)*(e-o)/2*p) % Mod1;
            cost2 = (cost2+(long long)(n+n-e+o+1)*(e-o)/2*p) % Mod2;

            it = mp.find(o);
            if( it==mp.end() ) mp.insert(make_pair(o,p));
            else it->second += p;
            
            it = mp.find(e);
            if( it==mp.end() ) mp.insert(make_pair(e,-p));
            else it->second -= p;
        }//cout<<cost<<endl;

        map<long long,long long> price, price2;
        map<long long,long long>::iterator pt;
        int st = 0;
        for(it=mp.begin(); it!=mp.end(); it++){
            int end = it->first, number = it->second;//cout<<"==  "<<end<<" "<<number<<endl;
            price2.clear();
            for(pt=price.begin(); pt!=price.end(); pt++){
                use0 = (use0+(long long)(2*pt->first-end+st+1)*(end-st)/2*pt->second) % Mod0;
                use1 = (use1+(long long)(2*pt->first-end+st+1)*(end-st)/2*pt->second) % Mod1;
                use2 = (use2+(long long)(2*pt->first-end+st+1)*(end-st)/2*pt->second) % Mod2;
                price2.insert(make_pair(pt->first-end+st,pt->second));
            }

            if( number>0 ){
                pt = price2.find(n);
                if( pt==price2.end() ) price2.insert(make_pair(n,number));
                else{ printf("error 0\n"); while(1); pt->second += number; }
            }else if( number<0 ){
                number = -number;
                pt = price2.end();
                for(--pt; true; pt--){
                    if( number<=pt->second ){ pt->second -= number; break; }
                    else{ number -= pt->second; pt->second = 0; }
                    if( pt==price2.begin() ){ printf("%d  error 1\n",number); while(1); }
                }
            }

            price.clear();
            for(pt=price2.begin(); pt!=price2.end(); pt++){
                //cout<<pt->first<<" "<<pt->second<<endl;
                if( pt->second!=0 ) price.insert(make_pair(pt->first,pt->second));
            }//cout<<end<<" "<<use<<" "<<it->second<<endl;

            st = end;
        }//cout<<use<<endl;
        
        long long a1 = (cost0-use0)%Mod0, m1 = Mod0;
        long long a2 = (cost1-use1)%Mod1, m2 = Mod1;
        long long a3 = (cost2-use2)%Mod2, m3 = Mod2;
        long long a12 = Mod_L_EQ( a1, m1, a2, m2 ), m12 = m1*m2;
        long long a123 = Mod_L_EQ( a12, m12, a3, m3 );
        printf("Case #%d: %lld\n",t,a123);
    }
    return 0;
}

