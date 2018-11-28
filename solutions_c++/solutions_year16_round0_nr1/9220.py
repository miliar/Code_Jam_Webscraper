/* sourabh1024  */
#include<bits/stdc++.h>

#define si(n)		(scanf("%d",&n))
#define pi(n)		(printf("%d",n))
#define sl(n)		(scanf("%I64d",&n))
#define pl(n)		(printf("%I64d",n))

#define lli long long int
#define ii pair<int,int>
#define vii pair< ii ,int>
#define pb(a) push_back(a)
using namespace std;
set<lli>s;
bool vis[10];

bool mark(lli curr) {
	if(curr==0) vis[curr] = true;
	while(curr>0) {
		lli val = curr%10;
		vis[val] = true;
		curr/=10;
	}
	for(int i=0;i<10;i++) {
		if(!vis[i]) return false;
	}
	return true;
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.txt","w",stdout);
	
	lli T,n,ca=0;
	cin>>T;
	while(T--) {
		ca++;
		cin>>n;
		
		s.clear();
		for(int i=0;i<10;i++)
			vis[i] = false;
			
	
		
		int res =0;
		lli curr = n;
		while(true) {
			if(s.find(curr)!=s.end()) {
				res=2;
				break;
			} else {
				s.insert(curr);
				if(mark(curr)) {
					res=1;
					break;
				}
			}
			curr = curr+n;
		}
		if(res==1) {
			//cout<<curr<<endl;
			cout<<"Case #"<<ca<<": "<<curr<<"\n";
		} else {
			cout<<"Case #"<<ca<<": INSOMNIA\n";
		}
	}
	return 0;
}

