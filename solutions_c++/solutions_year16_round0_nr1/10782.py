#include<bits/stdc++.h>
using namespace std;
int  main()
{
	ofstream os;
	os.open ("output.txt");
	ifstream is ("A-large.in");
	int t; is>>t;
	int c = 1;
	while(t--){
		long long n; is>>n;
		set<int>s;
		long long ans = -1;
		for(int i=1;i<=1000;i++){
			long long x = n * i;
			while(x){
				s.insert(x%10);
				x/=10;
			}
			if(s.size()==10){
				ans = n * i;
				break;
			}
		}
		os << "Case #"<<c++<<": ";
		if(s.size()==10)os<<ans<<'\n';
		else os<<"INSOMNIA\n";
	}
}
