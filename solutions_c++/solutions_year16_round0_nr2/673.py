#include <bits/stdc++.h>
using namespace std;

#define f(i,a)  for(int i=0;(i)<(a);++i)
#define fab(i,a,b) for (int i = (a); (i) < (b); ++i)
#define fba(i,a,b) for (int i = (b) - 1; (i) >= (a); --i)
#define fit(it,c) for(__typeof((c).begin()) it = (c).begin(); it != (c).end(); ++it)
#define all(c) (c).begin(),(c).end()


typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef unsigned int uint;
typedef char u8;
typedef vector <int> vi;
typedef pair <int, int> pii;


int main()
{
    ios_base::sync_with_stdio(0);cin.tie(0);
    int T,t,n;
    string S;
    cin>>T;
    f(t,T){
        cout<<"Case #"<<t+1<<": "; 
        cin>>S;
	n=1;
	fab(i,1,S.size())
		if(S[i]!=S[i-1])
			n++;
	if(S[S.size()-1]=='+')
		n--;
    	cout<<n<<"\n";
    }
    return 0;
}
