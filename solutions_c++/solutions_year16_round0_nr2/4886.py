#include <bits/stdc++.h>

#define pi 2*acos(0)
#define INF 1e18
#define MIN 1e-9
#define S(a) scanf("%d",&a)
#define SS(a,b) scanf("%d %d",&a,&b)
#define min(a,b) (((a)<(b))?(a):(b))
#define max(a,b) (((a)>(b))?(a):(b))
#define m_p make_pair
#define p_b push_back
#define n_p(a) next_permutation(all(a))
#define all(v) v.begin(),v.end()
#define allr(v) v.rbegin(),v.rend()
#define ii pair<int, int>
#define vi vector<int>
#define vii vector<ii>
#define rev(s) reverse(all(s))
#define ull unsigned long long
#define ll long long
#define mod 1000000007
#define mem(a,k) memset(a,k,sizeof a)
#define REP(i, a, b) for (int i = int(a); i <= int(b); i++)
#define u_b(X,V) upper_bound(X.begin(),X.end(),V)
#define l_b(X,V) lower_bound(X.begin(),X.end(),V)
#define cnt(s,c) count(all(s),c)

using namespace std;

int n,m,i,j,k,t,ans,p;

int main(){

	ios_base::sync_with_stdio(0);
	static const size_t npos = -1;
	//istringstream iss(s,istringstream::in);
	freopen("B-large.in","r",stdin);
	freopen("output.txt","w",stdout);			

	cin>>t;

	p=1;
	string s,s1;
	
	while(t--){
		cin>>s;
			while(1){
				j=s.find_last_of('-');
				if(j==npos){
					cout<<"Case #"<<p<<": "<<n<<endl;
					n=0;
					++p;
					break;
				}
				++n;

				if(s[0]=='-'){
					j=0;
					while(s[j]=='-'){
						++j;
					}
					for(k=0;k<j;k++){
						s[k]='+';
					}

				}
				else{
					j=0;
					while(s[j]=='+'){
						++j;
					}
					for(k=0;k<j;k++){
						s[k]='-';
					}										
				}
		}
		
	}
	

	return 0;
}

