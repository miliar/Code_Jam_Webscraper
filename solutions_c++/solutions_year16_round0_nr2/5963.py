#include<iostream>
#include <string>
#include <cstdio>
#include <deque>
using namespace std;

int main()
{
	
	freopen("B-large.in","r",stdin);
    freopen("output.txt","w",stdout);
	int T, ans;
	string S;
	cin>>T;
	for( int i=1; i<=T; i++){
		cin>>S;
		ans=0;

		for (int j=1; j< S.length(); j++)
			if(S[j] != S[j-1])
				ans++;
		if(S[S.length()-1]=='-')
			ans++;
		
		cout<<"Case #"<<i<<": "<<ans<<endl;
		}
	
	return 0;
}