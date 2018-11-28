
// Author: ngoyal2707

#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <iomanip>
#include <vector>
#include <stack>
#include <queue>
#include <cstdlib>
#include <map>
#include <algorithm>
#include <set>
#include <unordered_map>
#include <unordered_set>
#define FORALL(i,a,b)               for(decltype(a) i=a;i<b;i++)
#define FORALLR(i,a,b)               for(decltype(a) i=a;i>=b;i--)
#define FOREACH(v, c)               for( decltype( (c).begin()) v = (c).begin();  v != (c).end(); ++v)
#define FOREACHR(v, c)               for( decltype( (c).rbegin()) v = (c).rbegin();  v != (c).rend(); ++v)
#define PRINT1(x) cout<<"Passed Argument is:  "<<x<<"\n";
#define PRINT2(x,y) cout<<"1st value:  "<<x<<"\t2st value:  "<<y<<"\n";
#define PRINT3(x,y,z) cout<<"1st value:  "<<x<<"\t2st value:  "<<y<<"\t3st value:  "<<z<<"\n";
#define PRINT4(x,y,z,w) cout<<"1st value:  "<<x<<"\t2st value:  "<<y<<"\t3st value:  "<<z<<"\t4th value:  "<<w<<"\n";
#define PRINTEACH(v) FOREACH(it,v){ cout<<*it<<"\t"; } cout<<"\n";
#define PRINTEACH2(v) FOREACH(it,v){ FOREACH(it1,it){ cout<<*it1<<"\t"; } cout<<"\n"};
#define ALL(a)                      a.begin(), a.end()
#define IN(a,b)                     ( (a).find(b) != (a).end())
#define SIZE(a)                       ((int)(a.size()))
#define PRESENT(v,c)				((v).find(c)!=(v).end())
#define FIND(v,c)					v.find(c)-v.begin()
#define make_pair MP

using namespace std;
typedef long long int LL;
typedef long int L;
typedef vector<int> vi;
typedef vector<vector<int>> vvi;
typedef vector<char> vc;
typedef vector<vector<char>> vvc;
typedef vector<string> vs;
typedef vector<long> vl;
typedef vector<vector<long>> vvl;
typedef vector<long long int> vll;
typedef vector<vector<long long int>> vvll;
typedef vector<pair<int,int>> vpi;
typedef vector<pair<LL,LL>> vpll;


int main(){
	int T;
	cin>>T;
	int test_case=1;
	while(T--){
		LL N;
		cin>>N;
		if(N==0){
			cout<<"Case #"<<test_case<<": INSOMNIA\n";
		}else{
			int final = -1;
			unordered_set<int> digits;
			LL num = N;
			int count = 1; 
			while(digits.size()<10){
				// PRINT2(num, N)
				num = count*N;
				while(num>0){
					int digit = num%10;
					digits.insert(digit);
					num /= 10;
				}
				final = count*N;
				// num += N;
				count++;
			}
			cout<<"Case #"<<test_case<<": "<<final<<"\n";
		}
		test_case++;
	}
}
