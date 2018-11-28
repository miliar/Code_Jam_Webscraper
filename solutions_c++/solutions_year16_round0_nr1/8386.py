#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
	long long t,i=1,n,s,j;
	cin>>t;
	while(t--){
		set<int> s1;
		cin>>n;
		s=n;
		j=2;
		if(n==0){
			cout<<"Case #"<<i<<": "<<"INSOMNIA"<<endl;
		    i++;
		}
		else{
		while(s1.size()!=10){
		while(s!=0){
			s1.insert(s%10);
			s=s/10;
		}
		s=j*n;
		j++;
		}
		cout<<"Case #"<<i<<": "<<(j-2)*n<<endl;
		i++;
		}
	}
	return 0;
}
