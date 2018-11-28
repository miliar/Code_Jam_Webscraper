#include <vector>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <string>
#include <set>
#include <map>

#define rep(i,n) for((i)=0;(i)<(n);(i)++)
#define rp(i,s,n) for((i)=(s);(i)<(n);(i)++)	
#define ll long long
#define MP make_pair 
#define PB push_back
#define X first
#define Y second
#define ALL(a) (a).begin(),(a).end()
#define sz(a) a.size()
#define len(s) s.length() 

using namespace std;			

template <class T>
void out(vector<T> & a,string s="%3d "){
	int i,n=a.size();
	rep(i,n) printf(s.c_str(),a[i]);
	printf("\n");
}

template <class T> 
void out(T * a,int n,string s="%3d "){
	int i;
	rep(i,n) printf(s.c_str(),a[i]);
	printf("\n");
} 

ll i,j,N,M,n,m,k,p;

int main() {

#ifndef ONLINE_JUDGE
	freopen("C:\\Olimp2013\\GoogleCodeJam13\\CSqr\\input.txt","r",stdin);freopen("C:\\Olimp2013\\GoogleCodeJam13\\CSqr\\output.txt","w",stdout);
	//FILE * f, *g; f = fopen ("input.txt","r");//g = fopen ("output.txt","w");
#endif
/*
    set<string> st;
    string nl="", nl2="";
	nl.resize(25,'0');
	st.insert("1"+nl+"2"+nl+"1");

	rep(i,25){
		nl[i]='1';
		nl2=nl;
		reverse(ALL(nl2));
		st.insert("1"+nl+"2"+nl2+"1");
		nl[i]='0';
	}

	st.insert("1");
	st.insert("4");
	st.insert("9");
    
	nl="";
	rep(i,25){
        st.insert("4"+nl+"8"+nl+"4");
        nl.PB('0');
    }
	
	nl="";
	rep(i,13){
        st.insert("4"+nl+"4"+nl+"9"+nl+"4"+nl+"4");
        nl.PB('0');
    }
    nl=nl;
    
	*/
/*
        int s=121;
        for(j=1;j<=s;j *= 10);
        int b = j/10;
        int l=10;
        
        int flag=1;
        for(;b>(l/10);s=(s - (s/b)*b)/10 , b /= 100) 
           if (s/b != s%l) {flag=0; break;}
           
        if (flag) cout<<flag<<endl;
*/
	cin>>n;
    int p=0;
	rep(p,n){
		int A,B;
		
	cin>>A>>B;	
	int kk=0;
    rp(i,A,B+1){
        
		ll s=i;
        
        for(j=1;j<=s;j *= 10);
        ll b = j/10;
        ll l=10;
        
        ll flag=1;
        for(;b>(l/10);s=(s - (s/b)*b)/10 , b /= 100) 
           if (s/b != s%l) {flag=0; break;}
        
        
        if (!flag) continue;
		int pp=sqrt(i);
		if (pp*pp!=i) continue;

        s=pp;
        for(j=1;j<=s;j *= 10);
        b = j/10;
        l=10;
        
        flag=1;
        for(;b>(l/10);s=(s - (s/b)*b)/10 , b /= 100) 
           if (s/b != s%l) {flag=0; break;}
        if (flag) kk++;
        
    }

	printf("Case #%d: %d\n",p+1,kk);

	}

	
return 0;
}