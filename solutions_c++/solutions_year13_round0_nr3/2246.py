									/*ba yade oo */
//Mehrdad AP

#include <iostream>
#include <string>
#include <cstdio>
#include <string.h>
#include <algorithm>
#include <stdio.h>
#include <math.h>
#include <cstring>
#include <sstream>
#include <queue>
#include <vector>
#include <stack>
#include <set>
#include <map>



using namespace std;

#define PI 3.14159265358997
#define absol(x) ((x)>(0) ? (x):(-1)*(x))
#define pow2(x) ((x)*(x))
#define EPS 1e-7
#define INF 100000000
#define MAX 10000
#define MODE 1000000007
#define Left(x) (2*x)
#define Right(x) ((2*(x)+1)
//#define inRange(x,y) (x>=0 && x<N && y>=0 && y<M)

typedef vector<int> vi;
typedef pair<int,int> pii;
typedef pair<int,pii> piii;
typedef long long int lli;


lli rev(lli x){
	lli ans=0;
	while (x){
		ans=ans*10LL+x%10;
		x/=10LL;
	}
	return ans;
}

vector<lli> nums;

int main ()
{


	int tc,TC=0;

	for (lli i=1;i<=10000000;i++){
		if (i==rev(i) && i*i==rev(i*i) ) 
			nums.push_back(i*i);
	}
	//cout<<nums.size()<<endl;
	lli A,B;

	cin>>tc;
	
	while (tc--){
		cin>>A>>B;
		int sz=nums.size();
		int ans=0;
		for (int i=0;i<sz;i++){
			if (nums[i]>=A && nums[i]<=B) ans++;
		}
		printf("Case #%d: %d\n",++TC,ans);

	}
	


	return 0;
}
