#include<bits/stdc++.h>
using namespace std;
#define pb(x) push_back(x)
#define ppb pop_back
#define mp(x,y) make_pair((x),(y))
//#define sd(n) scanf("%d" , &n);
#define sz(v) int((v).size())
#define all(v) (v).begin(), (v).end()
#define mod 1000000007
#define maX(a,b)   ( (a) > (b) ? (a) : (b))
#define miN(a,b)   ( (a) < (b) ? (a) : (b))
#define bitcount   __builtin_popcount
#define mset(a,x) memset(a,x,sizeof(a)) //set elements of array to some value
#define char2Int(c) (c-'0')
#define present(c,x) ((c).find(x) != (c).end()) 
#define cpresent(c,x) (find(all(c),x) != (c).end())
#define forit(it, s) for(typeof((s).begin()) it = (s).begin(); it != (s).end(); ++it) 
#define F first
#define S second
#define RI(X) scanf("%d", &(X))
#define RII(X, Y) scanf("%d%d", &(X), &(Y))
#define RIII(X, Y, Z) scanf("%d%d%d", &(X), &(Y), &(Z))
#define DRI(X) int (X); scanf("%d", &X)
#define DRII(X, Y) int X, Y; scanf("%d%d", &X, &Y)
#define DRIII(X, Y, Z) int X, Y, Z; scanf("%d%d%d", &X, &Y, &Z)
#define LEN(X) strlen(X)
#define iOS ios_base::sync_with_stdio(false)
const double pi = acos(-1.0);

typedef vector<int> vi;
typedef pair<int,int> pii;
typedef vector<pair<int,int> > vpii;
typedef vector<long long> vl;
typedef pair<long long,long long> pll;
typedef vector<pair<long long,long long> > vpll;
typedef vector<string> vs;
typedef long double ld;
typedef  long long ll;
typedef unsigned long long ull;
string NumberToString ( ll Number )
{
	stringstream ss;
	ss << Number;
	return ss.str();
}


ll StringToNumber ( const string &Text )//Text not by const reference so that the function can be used with a 
{                               //character array as argument
	stringstream ss(Text);
	ll result;
	return ss >> result ? result : 0;
}
bool notFlag(vector<int> & arr){
	for(int i=0; i<arr.size(); i++){
		if(arr[i]!=-1){
			return true;
		}

	}
	return false;
}
bool allOnes(vector<int> & mxIdxs, vector<int> & arr){
	for(int i=0; i<mxIdxs.size(); i++){
		if(arr[mxIdxs[i]]!=-1){
			if(arr[mxIdxs[i]]!=1){
				return false;
			}
		}
	}
	return true;
}
int main(){
	//ifstream inp("./aSmall1.in");
	//ofstream out("./aSmall1.out");

	ifstream inp("./aLarge.in");
	ofstream out("./aLarge.out");
	int t;
	inp>>t;
	for(int a = 1; a<=t; a++){
		out<<"Case #"<<a<<": ";
		int n;
		vector<int> arr;
		inp>>n;
		//out<<" n is "<<n<<endl;
		for(int i=0; i<n; i++){
			int x ;
			inp>>x;
			arr.pb(x);
		}

		while(notFlag(arr)){

			int mx = -1;
			int mxIdx1 = -1;
			int mxIdx2 =-1;
			vector<int> mxIdxs;
			mxIdxs.empty();
			int ct =0;

			for(int i=0; i<arr.size(); i++){
				if(arr[i]==-1) continue;

				if(arr[i]>mx){
					mx=arr[i];
					mxIdxs.pb(i);
					mxIdx1 = i;
					ct = 1;
				}
				else if (arr[i]==mx){
					ct++;

					mxIdxs.pb(i);
					mxIdx2 = i;
				}
			}
			if(mx==-1) break;

			if(ct==3 && allOnes(mxIdxs, arr)){
				//out<<"no 1"<<endl;
				arr[mxIdx1]-=1;
				if(arr[mxIdx1]==0){
					arr[mxIdx1]=-1;
				}
				out<<char('A'+mxIdx1)<<" ";
			}
			else if(ct==1){
				//out<<"no 2"<<endl;
				if((arr[mxIdx1]-2)==0){
					arr[mxIdx1] = -1;

				}
				else arr[mxIdx1]-=2;
				out<<char('A'+mxIdx1)<<char('A'+mxIdx1)<<" ";
			}
			else if (ct>1){
				//out<<"no 3"<<endl;
				arr[mxIdx1]-=1;
				arr[mxIdx2]-=1;
				if(arr[mxIdx1]==0){
					arr[mxIdx1]=-1;
				}
				if(arr[mxIdx2]==0){
					arr[mxIdx2]=-1;
				}
				
				out<<char('A'+mxIdx1)<<char('A'+mxIdx2)<<" ";		
			}
		}
		out<<endl;
	}
}