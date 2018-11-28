#include <iostream>
#include <string>
#include <vector>

using namespace std;

long long prime(long long nr){
	for(long long i=2;i<nr/2;i++){
		if(nr%i==0)
			return i;
	}
	return -1;
}

long long convto(long long base,long long nr){
	long long res=0;
	long long fact=1;
	while(nr!=0){
		res += (nr%10)*fact;
		//cout<<"nr"<<nr<<"fact"<<fact<<"res"<<res<<endl;
		nr/=10;
		fact*=base;
	}
	return res;
}

long long convback(long long base,long long nr){
	long long res=0;
	if(nr/base !=0){
		res = convback(base,nr/2);
	}
	return (10*res)+(nr%2);
}

int main(){
	long long t,n,l,s,curr;
	long long found = 0;
	bool poss;
	vector<long long> res(9);
	cin>>t;
	for(int i=0;i<(int)t;i++){
		cin>>l>>n;
		cout<<"Case #"<<i+1<<":"<<"\n";
		found = 0;
		s=1;
		for(long long j=1;j<l;j++){
			s*=2;
		}
		s++;
		//cout<<"start:"<<s<<endl;
		while(found<n){
			poss = true;
			cout<<s<<endl;
			//cout<<endl;
			//cout<<"s:"<<s<<"\n";
			for(long long k=2;k<11;k++){
				curr = convto(k,convback(2,s));
				//cout<<"curr"<<curr<<endl;
				if(prime(curr)<0){
					//cout<<"prime"<<curr<<"sys"<<k<<endl;
					poss = false;
					break;
				}
				else{
					res[k-2]=prime(curr);
				}
			}
			if(poss){
				found++;
				//cout<<found<<endl;
				cout<<convback(2,s);
				for(long long h=0;h<9;h++){
					cout<<" "<<res[h];
				}
				cout<<"\n";
			}
			s+=2;
		}
	}
	return 0;
}