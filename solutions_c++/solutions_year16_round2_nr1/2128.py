#include <bits/stdc++.h>
using namespace std;

#define f(i,a)  for(int i=0;(i)<(a);++i)
#define fab(i,a,b) for (int i = (a); (i) < (b); ++i)
#define fba(i,a,b) for (int i = (b) - 1; (i) >= (a); --i)
#define fit(it,c) for(__typeof((c).begin()) it = (c).begin(); it != (c).end(); ++it)
#define all(c) (c).begin(),(c).end()
#define MOD 1000000007

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef unsigned int uint;
typedef char u8;
typedef vector <int> vi;
typedef pair <int, int> pii;

ll pw(ll b, int p){
    ll a=1;
    while(p){
        if(p&1)
            a=(a*b)%MOD;
        b=(b*b)%MOD;
        p>>=1;
    }
    return a;
}
int A[26],B[10];
void reduce(string S, int x){
	f(i,S.size())
		A[S[i]-'A']-=x;
}
int main() {
    ios_base::sync_with_stdio(0);cin.tie(0);
    int T,t;
	string S;
    cin>>T;
    f(t,T){
        cout<<"Case #"<<t+1<<": ";
		cin>>S;
		f(i,26)
			A[i]=0;
		f(i,10)
			B[i]=0;
		f(i,S.size())
			A[S[i]-'A']++;
//		f(i,26)
//			cout<<A[i]<<" ";
		B[0]=A['Z'-'A'];
		reduce("ZERO",B[0]);
		B[8]=A['G'-'A'];
		reduce("EIGHT",B[8]);
		B[6]=A['X'-'A'];
		reduce("SIX",B[6]);
		B[7]=A['S'-'A'];
		reduce("SEVEN",B[7]);
		B[5]=A['V'-'A'];
		reduce("FIVE",B[5]);
		B[4]=A['F'-'A'];
		reduce("FOUR",B[4]);
		B[3]=A['R'-'A'];
		reduce("THREE",B[3]);
		B[2]=A['T'-'A'];
		reduce("TWO",B[2]);
		B[1]=A['O'-'A'];
		reduce("ONE",B[1]);
		B[9]=A['I'-'A'];
		f(i,10)
			while(B[i]--)
				cout<<i;
		cout<<"\n";
    }
    return 0;
}
