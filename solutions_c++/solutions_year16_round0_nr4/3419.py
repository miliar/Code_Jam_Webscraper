#include<bits/stdc++.h>
using namespace std;

int main(int argc, char const *argv[])
{
	freopen("input4small.in", "r", stdin);
	freopen("output4small.in", "w", stdout);
	long long int c, k,q, s, t;
	cin>>t;
	q=1;
	while(t--){
		cin>>k>>c>>s;
		cout<<"Case #"<<q<<":";
		q++;
		for(int i=1;i<=s;i++)
			cout<<" "<<i;
		cout<<endl;
	}
	return 0;
}