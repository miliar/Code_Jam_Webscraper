#include <bits/stdc++.h>
using namespace std;

#define INF                         (int)1e9
#define bitcount                    __builtin_popcount  // counts 1 eg- 1101 has value 3


/* 
   const clock_t begin_time = clock();
   // do something
   cout << float( clock () - begin_time ) /  CLOCKS_PER_SEC;
*/

template<class T> T gcd(T a, T b) { return a ? gcd (b % a, a) : b; }
#define boost ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0)
// Useful container manipulation / traversal macros
#define fa(i, begin, end)           for (auto i = (begin) - ((begin) > (end)); i != (end) - ((begin) > (end)); i += 1 - 2 * ((begin) > (end)))
#define fe(v, c)                    for(auto v :c)
#define all(a)                      a.begin(), a.end()
#define in(a,b)                     ( (b).find(a) != (b).end())
#define pb                          emplace_back  // this will work almost always
#define fill(a,v)                    memset(a, v, sizeof a)
#define sz(a)                       ((auto)(a.size()))
#define mp                          make_pair
// comparision Guys 
#define maX(a,b)                     ( (a) > (b) ? (a) : (b))
#define abs(a)                       ( (a) > (0) ? (a) : (-a))
#define miN(a,b)                     ( (a) < (b) ? (a) : (b))
#define checkbit(n,b)                ( (n >> b) & 1)
#define DREP(a)                      sort(all(a)); a.erase(unique(all(a)),a.end()) //deletes repeat
#define sqr(x)                       ((x) * (x))
#define sqrt(x)                       sqrt(abs(x))
// The bit standard guys
#define bit(x,i)                    (x&(1<<i))  //select the bit of position i of x
#define lowbit(x)                   ((x)&((x)^((x)-1))) //get the lowest bit of x
#define higbit(x)                   (1 << ( auto) log2(x) )

// The vectors and pairs
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int>pa;
#define ft                 first
#define sd                 second

// the data types
#define ll long long
#define st string
#define ld long double

bool check(int arr[]){
	for(int i=0;i<10;i++){		if(arr[i]==0){		return false;

	
		}
	}
	return true;
}

int main(){
	long long temp2,t,n,temp,ans;
	freopen("ab.in","r",stdin);
    freopen("output_file_name.out","w",stdout);
	cin>>t;
	for(int i=1;i<=t;i++){
		cin>>n;
		temp=n;
		if(n==0){
			cout<<"Case #"<<i<<": "<<"INSOMNIA"<<endl;
		}
		else{
		  int arr[10];
		  memset(arr,0,sizeof(arr));
		  while(true){
		  	if(check(arr)){
		  		break;
		  	}
		  	temp2=n;
		  	while(n){
		  		arr[n%10]=1;
		  		n=n/10;
		  	}
		  	n=temp2 + temp;
		  }
		  cout<<"Case #"<<i<<": "<<temp2<<endl;

		}


	}

}