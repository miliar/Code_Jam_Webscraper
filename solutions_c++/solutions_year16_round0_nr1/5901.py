#include<iostream>
#include <string>
#include <cstdio>
#include <set>
using namespace std;

int main()
{
	
	freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
	long long T, N, ans;
	string n;
	cin>>T;
	for( long long i=1; i<=T; i++){
		cin>>N;
		if(N==0)
			cout<<"Case #"<<i<<": INSOMNIA"<<endl;
		else {
			
			int count=2;
			ans=N;

			// to check the apperance of the 10 digits
			set<char> digits;
			string n= to_string(N);
			for( unsigned int j=0; j<n.length(); j++)
					digits.insert(n[j]);

			while( digits.size() !=10){
				ans = count*N;
				n= to_string(ans);
				for( unsigned int j=0; j<n.length(); j++)
					digits.insert(n[j]);
			
			count++;
			}
				
			cout<<"Case #"<<i<<": "<<ans<<endl;
		}
	}

	return 0;
}