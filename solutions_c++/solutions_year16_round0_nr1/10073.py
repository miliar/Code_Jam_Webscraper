#include <bits/stdc++.h>
#define INF 1e9
#define DEBUG(x) cout << '>' << #x << ':' << x << endl;
using namespace std;
typedef long long ll;
typedef pair<int,int> ii;
main(){
	ios::sync_with_stdio(false);
	int t,n,cases=0;
	cin>>t;
	while(cases<t){
		cin>>n;
		if(n==0){
			cout<<"Case #"<<(cases+1)<<": INSOMNIA\n";
		}else{
			int ar[10],count=0,N=n;
			for(int i=0;i<10;i++)
				ar[i]=0;
			while(count<10){
				int temp=n;
				while(temp>0){
					if(ar[temp%10]==0)
						count++,ar[temp%10]++;
					if(count==10)
						break;
					temp/=10;
				}
				if(count==10)
					break;
				n+=N;
			}
			cout<<"Case #"<<(cases+1)<<": "<<n<<"\n";
		}
		cases++;
	}	
}