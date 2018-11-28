#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <cctype>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <string>
#include <sstream>

using namespace std;

#define REP(i,a,b) 	for(int i=a;i<(int)b;i++)
#define all(x) 		(x).begin(),(x).end()
#define pb 			push_back
#define clr(x,y)	memset(x,y,sizeof x)
#define oo 			(1<<30)
#define bit(x)		_builtin_popcount(x)
#define mp			make_pair
#define fst			first
#define snd			second



int main(){
	int a[]={1,4,9,121,484};
	int n;
	cin>>n;
	REP(ii,0,n){
		int A,B;
		cin>>A>>B;
		int ans=0;
		REP(j,0,5) if(A<=a[j] and a[j]<=B) ans++;
		cout<<"Case #"<<ii+1<<": "<<ans<<endl;
	}

    return 0;
}




