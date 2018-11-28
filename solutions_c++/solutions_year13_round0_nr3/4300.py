


//		ABHINAV SINGI  		//

#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<sstream>
#include<cassert>
#include<cmath>
#include<cstdlib>
#include<queue> 		//FIFO
#include<map>
#include<set>
#include<vector>
#include<cstring>
#include<stack>			//LIFO

using namespace std;
#define pop_count(n) __builtin_popcount(n)
#define FOR(i,a,b) for(int i= (int)a; i<= (int)b; i++)
#define FORD(i,a,b) for(int i= (int)a; i>= (int)b; i--)
#define REP(i,n) FOR(i,0,n)
#define PB push_back
#define ALL(x) x.begin(),x.end()
#define LET(x,a) __typeof(a) x(a)
#define IFOR(i,a,b) for(LET(i,a);i!=(b);++i)
#define EACH(it,v) IFOR(it,v.begin(),v.end())
#define MP make_pair

typedef pair<int,int> PI;
typedef vector<int> VI;
typedef long long LL;
#define INF 1000000000
#define ALPHABET_SIZE 26


int main() 
{
	int arr[1000010]={0};
	long long int ans[] = {1,4,9,121,484,10201,12321,14641,40804,44944,1002001,1234321,4008004,100020001,102030201,104060401,121242121,123454321,125686521,400080004,404090404,10000200001,10221412201,12102420121,12345654321,40000800004,1000002000001,1002003002001,1004006004001,1020304030201,1022325232201,1024348434201,1210024200121,1212225222121,1214428244121,1232346432321,1234567654321,4000008000004,4004009004004,100000020000001};
	long long int T,a,b;
	cin >> T;
	int count=0,cnt=0;
	while(T--){
		count++;
		cnt=0;
		cin >> a >> b;
		FOR(i,0,39){
			if(ans[i] <= b && ans[i] >= a)
				cnt++;
		}
		cout << "Case #" << count<< ": " << cnt << endl;
	}
	return 0;
}	
	

