#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include<cstring>
// Input macros
#define s(n)  scanf("%d",&n)
#define sc(n) scanf("%c",&n)
#define sl(n) scanf("%lld",&n)
#define sf(n) scanf("%lf",&n)
#define ss(n) scanf("%s",n)
// Useful constants
#define INF (int)1e9
#define EPS 1e-9
// Useful hardware instructions
#define bitcount __builtin_popcount
#define gcd __gcd
// Useful container manipulation / traversal macros
#define forall(i,a,b) for(int i=a;i<b;i++)
#define foreach(v, c) for( typeof( (c).begin()) v = (c).begin();  v != (c).end(); ++v)
#define all(a) a.begin(), a.end()
#define in(a,b) ( (b).find(a) != (b).end())
#define pb push_back
#define fill(a,v) memset(a, v, sizeof a)
#define sz(a) ((int)(a.size()))
#define mp make_pair
// Some common useful functions
#define maX(a,b) ((a) > (b) ? (a) : (b))
#define miN(a,b) ( (a) < (b) ? (a) : (b))
#define checkbit(n,b) ( (n >> b) & 1)
#define DREP(a) sort(all(a)); a.erase(unique(all(a)),a.end())
#define INDEX(arr,ind) (lower_bound(all(arr),ind)-arr.begin())
using namespace std;
struct node{
	char Party;
	int count;
};
bool myfunc(struct node N1,struct node N2){
	if(N1.count<=N2.count){
		return false;
	}
	else{
		return true;
	}
}
string getResult(vector<node> P){		
	string result="";	
	if(P.size()==2){
		sort(P.begin(),P.end(),myfunc);
		while(P[0].count>P[1].count){
			result+=P[0].Party;
			result+=" ";
			P[0].count--;
		}
		while(P[0].count!=0){
			result+=P[0].Party;
			result+=P[1].Party;
			result+=" ";
			P[0].count--;
			P[1].count--;
		}		
	}
	else{		
		while(true){			
			sort(P.begin(),P.end(),myfunc);
			if(P[0].count==1 && P[1].count==1 && P[2].count==0){
				result+=P[0].Party;
				result+=P[1].Party;
				result+=" ";
				P[0].count--;
				P[1].count--;		
				break;
			}
			else{
				result+=P[0].Party;
				result+=" ";
				P[0].count--;
			}
		}		
	}	
	return result;
}
int main(){
	int T;
	int N;
	int temp;
	string str;
	scanf("%d",&T);
	for(int i=1;i<=T;i++){
		scanf("%d",&N);
		vector<node> P(N);
		for(int j=0;j<N;j++){
			scanf("%d",&temp);
			P[j]=node();
			P[j].Party=65+j;
			P[j].count=temp;
		}
		cout<<"Case #"<<i<<": "<<getResult(P)<<endl;	
		// cerr<<"Done with "<<i<<endl;
	}
	return 0;
}
