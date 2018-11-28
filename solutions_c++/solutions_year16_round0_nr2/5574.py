#include <iostream>
#include <string>
#include <cstdio>

using namespace std;

int main(int argc, char** argv) {
	freopen("BL.in","r",stdin);
	freopen("BL.out","w",stdout);
	int T,i;
	cin>>T;
	for(i=1;i<=T;i++)
	{string S; int j,N,ans=0;
		cin>>S; S+="+"; N=S.size();
		for(j=1;j<N;j++)ans+=S[j]!=S[j-1];
		cout<<"Case #"<<i<<": "<<ans<<endl;
		//cout<<S.substr(0,N-1)<<endl;
	}
	return 0;
}
