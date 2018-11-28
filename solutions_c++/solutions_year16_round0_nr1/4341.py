#include<iostream>
#include<cmath>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<vector>
#include<algorithm>
#include<set>
#include<map>

#define MOD 1000000007
#define LL long long
#define ULL unsigned long long
#define RESET(a, b) memset(a,b,sizeof(a))

//CountingSheepA16

using namespace std;
int main(){
	std::ios_base::sync_with_stdio(false);
	#ifndef ONLINE_JUDGE
	freopen("A-large.in","r",stdin);
	#endif
	freopen("outputLarge.txt","w",stdout);

	ULL i, j, k, n, cases, t;
	cin>>cases;
	
	for(k=1;k<=cases;k++){
		
		cin>>t;
		n = 0;
		set<int> s;
		
		if(t!=0)
		for(i=1;i<MOD;i++)	
		{
			ULL num = t * i;
			n = num;
			while(num > 0){
				ULL last = num%10;
				num /= 10;
				s.insert(last);	
			}
			
			if(s.size() == 10)
				break;
		}
		
		cout<<"Case #"<<k<<": ";		
		if(s.size() == 10)
			cout<<n<<endl;
		else
			cout<<"INSOMNIA"<<endl;
	}
	
return 0;
}

