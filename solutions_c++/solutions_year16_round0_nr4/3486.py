#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main()
{
	ios::sync_with_stdio(false);
	int T,K,C,S,t=1;
	cin>>T;
	//works only if K = S
	while(t<=T)
	{
		cin>>K>>C>>S;
		cout<<"Case #"<<t<<":";
		for(int i=1;i<=S;i++)
			cout<<" "<<i;
		cout<<endl;
		t++;
	}
	return 0;
}