#include <bits/stdc++.h>
using namespace std;


pair<bool, unsigned long long> isPrime(unsigned long long x){
	for(unsigned long long i=2,l=sqrt(x);i<=l;i++){
		if(x%i == 0)
			return make_pair(false, i);		
	}
	return make_pair(true, 0);
}

int main(){
	// freopen("inputp4.txt","r",stdin);
//	freopen("output2.txt","w",stdout);
	unsigned long long n=16, k=50,found = 0;
	cout<<"Case #1:"<<endl;

	for(unsigned long long i=(1<<(n-1))+1,l=1<<n;i<l&&found<k;i+=2){
		vector<unsigned long long> divisors;
		for(unsigned long long b=2;b<=10;b++){
			unsigned long long temp = i,m=0,sum=0;
			while(temp){
				if(temp&1)
					sum+=pow(b,m);
				m++;
				temp = temp>>1;
			}
			pair<bool,unsigned long long> p = isPrime(sum);
			if(p.first)
				break;
			else
				divisors.push_back(p.second);
		}
		if(divisors.size()==9){
			found++;
			unsigned long long temp = i;
			stringstream ss;
			while(temp){
				ss<<(temp&1);
				temp=temp>>1;
			}
			string s;
			ss>>s;
			reverse(s.begin(),s.end());
			cout<<s<<" ";
			for(unsigned long long p=0;p<divisors.size();p++)
				cout<<divisors[p]<<" ";
			cout<<endl;
		}
	}

	return 0;
}