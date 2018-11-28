#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <string>
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
#include <cstring>
#include <cassert>
#include <fstream>
#include <cctype>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> ii;

#define sz(a) (a).size()
#define pb push_back
#define fill(a, val) (memset(a,val,sizeof(a)))
#define pow2(x) (1 << (x)) 
#define fin(i,a,n) for(int i = a; i < n; i++)
#define fdc(i,n,a) for(int i = n-1; i >= a; i--)
#define scn(t) scanf("%d",&t)
#define scnt(t) int t;scanf("%d",&t)
#define newline printf("\n")
#define all(v) v.begin(),v.end()
#define MAX 1000000007

string fun(long long int n) 
{
	string s1;
	while ( n > 0 ) {
		s1.push_back((char)(n%10 + 48));
		n = n/10;
	}
	return s1;
}


int func(long long int a)
{
	string s = fun(a);
	string s1 = s;
	reverse(s.begin(),s.end());
	if(s==s1){
		long long int b = a*a;
		string t = fun(b);
		string t1 = t;
		reverse(t.begin(),t.end());
		if(t==t1){
			return 1;		
		}	
	}
	return 0;
	
}
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	
	int t;
	cin >> t;
	long long int arr[39] = {1,4,9,121,484,10201,12321,14641,40804,44944,1002001,1234321,
	4008004,100020001,102030201,104060401,121242121,123454321,125686521,400080004,404090404,
	10000200001,10221412201,12102420121,12345654321,40000800004,1000002000001,1002003002001,
	1004006004001,1020304030201,1022325232201,1024348434201,1210024200121,1212225222121,
	51214428244121,1232346432321,1234567654321,4000008000004,4004009004004};
	                                         int k  = 1;
	while(t--){
		long long int a,b;
		cin >> a >> b;
		int coun = 0;
		for(int i = 0; i < 39; i++){
			if(arr[i] >= a && arr[i] <= b){
					coun++;
					//cout << arr[i] << " i = " <<i << "\n" ;
			}
		}
	/*	for(long long int i = a; i <= sqrt(b); i++){
			if(func(i) == 1){
				cout << i*i << ",";
				coun++;
				
			}
		}
	*/
		cout << "Case #"<<k++<<": "<<coun << endl;
	}
	return 0;
}
