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
	freopen("B-large.in","r",stdin);
	freopen("a.out","w",stdout);
#endif
	int i,j,k,t,n,tmp,ans;
	string s;
	cin>>t;
	k=0;
	while(++k<=t){
		cin>>s;
		int slen=s.length();
		ans=0;
		for(i=slen-1;i>=0 && s[i]=='+';i--) ;
		if(i!=-1)
			ans++;
		for(j=i;j>0;j--){
			if(s[j]!=s[j-1])
				ans++;
		}
		
		cout<<"Case #"<<k<<": "<<ans<<endl;

	}
	
	return 0;
}
