#include<iostream>
using namespace std;
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<vector>
#include<map>
#include<queue>
#include<algorithm>
#include<cmath>
#include<set>
#include<ctime>
#include<stack>
#include<list>
typedef  pair<int,int> pii;
#define rep(i,j,n) for(i=j;i<n;i++)
#define pb push_back
#define sz(a) a.size()
#define ff first
#define ss second 
#define lli long long int

int main() {
		
	ios::sync_with_stdio(false);

	//clock_t start = std::clock();
	freopen ("inp.txt","r",stdin);
	freopen ("out.txt","w",stdout);
	
	int t,ca=0,i,smax,num;
	cin>>t;
	string s;
	long long answer = 0,count;
	while(t--){
		ca++;
		answer = count = 0;
		
		cin>>smax;
		cin>>s;
		
		for(i=0;i<=smax;i++){
			num = s[i]-'0';
			if(!num)	continue;
			if(count<i){
				answer += i-count;
				count += (i-count);
			}
			count += num;
		}
		
		cout<<"Case #"<<ca<<": "<<answer<<"\n";
		
	}
	
	
	//cout << "Time: " << (std::clock() - start) / (double)(CLOCKS_PER_SEC / 1000) << " ms" << std::endl;
	


	return 0;
}
