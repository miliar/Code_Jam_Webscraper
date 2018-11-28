#include<bits/stdc++.h>
#include<stdlib.h>
using namespace std;

int main(){
	freopen("input.in","r",stdin);
	freopen("output.txt","w",stdout);
	long int t;
	scanf("%ld",&t);
	for(long int c=1;c<=t;c++){
		set<char> s;
		long long n;
		long long i=1;
		string result;
		scanf("%lld",&n);
		if(n==0){
			cout<<"Case #"<<c<<": "<<"INSOMNIA"<<endl;
			continue;
		}
		while(1){
			ostringstream convert;
			convert << (n*i++);
			string str = convert.str();
//			cout<<str<<endl;
			for(size_t a =0; a < str.size() ;a++){
				s.insert(str[a]);
				if(s.size()>=10) break;
			}
			if(s.size() >=10) break;
		}
		cout<<"Case #"<<c<<": "<<--i*n<<endl;
	}
return 0;
}
