#include <bits/stdc++.h>
using namespace std;
set<int>s;
void check(long long n){
	long long z=0;
	while(n){
		z=n%10;
		s.insert(z);
		n/=10;
	}
	}
int main() {
    freopen("A-large.in", "rt", stdin);
	freopen("output.out", "wt", stdout);
 	int T;
 	cin>>T;
 	for(int i= 1 ;i<=T; i++){
    int j;
    long long x;
    cin>>x;
 	if (x==0){
 	cout<<"Case #"<<i<<": INSOMNIA"<<endl;
 	goto AA;}
 	else {
      for(j=1 ;j<=10000;j++){
      if(s.size()==10)
        break;
       check(x*j);
      }
   	}
   	if(s.size()!=10){
        cout<<"Case #"<<i<<": INSOMNIA"<<endl;
   	}
   	else{
   	 cout<<"Case #"<<i<<": "<<x*(j-1)<<endl;
   	}
 	s.clear();
    AA: int EE;
 	}

	return 0;
}
