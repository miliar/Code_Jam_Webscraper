/*--------------------- Author - Akshit ----------------------*/

#include<iostream>
#include<cstdio>
#include<cmath>
#include<string>
#include<cstring>
#include<algorithm>
#include<vector>
#include<stack>
#include<list>
#include<queue>
#include<cstdlib>
#include<numeric>
#include<set>
#include<map>
#include<deque>
#include<climits>
#include<cassert>
#include<cctype>
#include<ctime>
#include<iterator>
#include<iomanip>
#include<functional>
#include<fstream>
#include<ostream>
#include<istream>

using namespace std;

#define sf(n)                scanf("%d",&n) 
#define pf(n)                printf("%d",n)          
#define pfln(n)              printf("%d\n",n)         

#define vi                   vector <int > 
#define pb                   push_back()
#define debug(in)             printf("n = %d\n",n)
#define PI 3.14159265358979
#define LL 1000000007

int main()
{
	std::ios_base::sync_with_stdio(false);
	int t,a,b,k;
	cin>>t;
	int no = 1;
	while(no<=t){
		int ans = 0;
		cin>>a>>b>>k;
		for (int i = 0 ; i < a ;i++){
			for(int j = 0 ; j <b ;j++){
				if((i&j) < k)
					ans++;
			}
		}
		cout<<"Case #"<<no<<": "<<ans<<"\n";
		no++;
	}

	return 0;
}
