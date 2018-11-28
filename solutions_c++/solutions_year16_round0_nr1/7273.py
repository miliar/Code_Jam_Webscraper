#include <iostream>
using namespace std;
#include <string>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#define EACH(it,a) for(auto it=begin(a);it!=end(a);it++)
#define LL long long
#define INF 0x3f3f3f3f

int main()
{
	ios_base::sync_with_stdio(0);
#ifdef _DEBUG
	freopen("A-large.in","r",stdin);
	freopen("a.out","w",stdout);
#endif
	int i,j,k,t,n,tmp,ans;
	cin>>t;
	k=0;
	while(++k<=t){
		cin>>n;
		if(n==0){
			cout<<"Case #"<<k<<": INSOMNIA"<<endl;
		}else{
			bool res[10]={false};
			i=1;
			for(;;){
				ans=tmp=(i++)*n;
				while(tmp!=0){
					res[tmp%10]=true;
					tmp/=10;
				}
				for(j=0;j<10 && res[j];j++) ;
				if(j==10)
					break;
			}
			cout<<"Case #"<<k<<": "<<ans<<endl;
		}
	}
	

	return 0;
}
