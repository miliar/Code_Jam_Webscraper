#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string>
#include <cstring>
#include <cmath>
#include <queue>
#include <deque>
#include <stack>
#include <map>
#include <set>
#include <cstdlib>
#include <vector>
#define ll long long
#define s second
#define f first
#define PB push_back
using namespace std;
map<ll,ll>mp;
typedef pair<int,int>pib;

#define SWAP(a, b) (((a) ^= (b)), ((b) ^= (a)), ((a) ^= (b)))

int compare (const void * a, const void * b)
{
  return ( *(int*)a - *(int*)b );
}
double cookie(double c,double f,double x){
	
	double time=0.0,ans=10000000.0,key=2.0;
	
	for(int i=0;i<100000;i++){
		
	double	total=time+(x/key);
		ans=min(ans,total);
		time=time+(c/key);
		key=key+f;
		
	}
	return ans;
}
	
	
	

int main(){

ll t;
cin>>t;
cout.precision(7);
for(int cases=1;cases<=t;cases++){
	
	double c,f,x;
	cin>>c>>f>>x;
	  std::cout <<std::fixed;
	 double result=cookie(c,f,x);
	 cout<<"Case #"<<cases<<": ";
	 cout<<result<<endl;
}

cin.get();
return 0;
}

