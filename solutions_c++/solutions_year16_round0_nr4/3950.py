#include <bits/stdc++.h>
using namespace std;

#define INF                         (int)1e9
#define forall(i,a,b)               for(int i=a;i<b;i++)
#define bitcount                    __builtin_popcount  // counts 1 eg- 1101 has value 3
// with bitcount be careful with data types

// Useful container manipulation / traversal macros
#define forall(i,a,b)               for(int i=a;i<b;i++)
#define foreach(v, c)               for( typeof( (c).begin()) v = (c).begin();  v != (c).end(); ++v)
#define all(a)                      a.begin(), a.end()
#define in(a,b)                     ( (b).find(a) != (b).end())
#define pb                          push_back
#define fill(a,v)                    memset(a, v, sizeof a)
#define sz(a)                       ((int)(a.size()))
#define mp                          make_pair

// comparision Guys 
#define maX(a,b)                     ( (a) > (b) ? (a) : (b))
#define abs(a)                       ( (a) > (0) ? (a) : (-a))
#define miN(a,b)                     ( (a) < (b) ? (a) : (b))
#define checkbit(n,b)                ( (n >> b) & 1)
#define DREP(a)                      sort(all(a)); a.erase(unique(all(a)),a.end()) //deletes repeat

// The bit standard guys
#define bit(x,i)                    (x&(1<<i))  //select the bit of position i of x
#define lowbit(x)                   ((x)&((x)^((x)-1))) //get the lowest bit of x
#define hBit(msb,n)        asm("bsrl %1,%0" : "=r"(msb) : "r"(n)) //get the highest bit of x, maybe the fastest
#define higbit(x)                   (1 << ( int) log2(x) )

// The vectors and pairs
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> ii;
#define ft                 first
#define sd                 second

// the data types
#define ll long long
#define st string
int spec(string s){
	int l=s.length();for(int i=0;i<l;i++){if(s[i]!='+'){return 0;} }
	 return 1;
}
string flip(string str,int i){
	int l=str.length();	string flipped;	string flip=str.substr(0,i+1);
	reverse(flip.begin(),flip.end());
	for(int j=0;j<flip.length();j++){
		flip[j] = ((flip[j]=='+')) ? '-' : '+';

	}
	flipped=flip+str.substr(i+1,l-(i+1));
	return flipped;

}

map<string,int> indexer;
map<int,string> reverter;
int finalscores[1200],p,n,m,placore[1200],w,people=0;;
string names;
vector<pair<int,string> > myvaues;
pair<int,string>reader,prev;


int main(){
		freopen("i.in","r",stdin);
    freopen("output_file_name.out","w",stdout);
	int t,k,c,s,ans;
	cin>>t;
	for(int j=1;j<=t;j++){
		cin>>k>>c>>s;
		if(k==1){
			 cout<<"Case #"<<j<<": "<<"1"<<endl;
		}
		else if(c==1 && s==k){
			cout<<"Case #"<<j<<": ";
			for(int i=1;i<=k;i++){
			   cout<<i<<" ";
			}
			cout<<" "<<endl;
		}
		else if(c==1 && s<k){
			 cout<<"Case #"<<j<<": "<<"IMPOSSIBLE"<<endl;
		}
		else if(c>1 && s<k-1){
			 cout<<"Case #"<<j<<": "<<"IMPOSSIBLE"<<endl;
		}
		else if(c>1 && s>=k-1){
			cout<<"Case #"<<j<<": ";
			for(int i=2;i<=k;i++){
			    cout<<i<<" ";
			}
			cout<<" "<<endl;

		}

	}

}