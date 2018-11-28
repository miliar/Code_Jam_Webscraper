#include <iostream>
#include <vector>
#include <cmath>
#include <utility>
#define NN 200000000
#define lld unsigned long long 
using namespace std;
unsigned int A[NN/64];
unsigned int primes[12078937];
int total;

int check(int i){
  int j = i/64;
  int k = (i%64)/2;
  return (A[j] & 1<<k)>>k;
}

void set(int i){
  int j = i/64;
  int k = (i%64)/2;
  A[j]=(A[j] | 1<<k);
}

void sieve(){
  int i,j,k,temp,c;
  A[0]=1;
  k =sqrt(NN);
  for(i=3;i<=k;i+=2){
    if(!check(i)){
      for(j=i+2*i;j<=NN;j+=2*i){
		set(j);
      }
    }
  }
  primes[0]=2;
  total = 1;
  for(i=3;i<NN;i+=2)
    if(!check(i)){
    	//total++;
      primes[total++]=i;
    }
   // cout<<total<<endl;
}

string getBinary(int i,int j){
	string s ="";
	for(int k=0;k<j;k++){
		if(i & (1<<k))
			s = "1"+s;
		else
			s = "0"+s;
	}
	return "1"+s+"1";
}

int get_divisor( long long int num){
	for(int i=0;i<total && primes[i]<sqrt(num)-1;i++){
		if(num%primes[i]==0){
			return primes[i];
		}
	}
	return 1;
}

long long int getNum(long long int a,long long int b, int n){
	long long int ans = 1;
	for(int i=n-1;i>=0;i--){
		ans = ans*b;
		if(a & (1<<i))
			ans += 1;
	}
	return ans*b + 1;
}

int main(){
	int num_cases;
	sieve();
	cin>>num_cases;
	//num_cases = 1;
	for(int t=1;t<=num_cases;t++){
		cout<<"Case #"<<t<<":"<<endl;
		int N,J;
		cin>>N>>J;
		//N=16;
		//J=50;
		int c=0;
		//cout<<"here"<<endl;
		for(int i=0;(i<(1<<(N-2))) && (c<J);i++){
			//cout<<"here"<<endl;
			//cout<<i<<" ";
			//cout<<"Get binary"<<endl;
			//cout<<getBinary(i,N-2)<<endl;
			vector<pair<int,int> > v;
			//cout<<"here"<<endl;
			for(int k=2;k<=10;k++){

				long long int num = getNum(i,k,N-2);
			///	cout<<"base = "<<k<<endl;
			//	cout<<"num = "<<num<<endl;
				//cout<<"here"<<endl;
				int divi = get_divisor(num);
				//cout<<"divi : "<<divi<<endl;
				if( divi != 1)
					v.push_back(make_pair(k,divi));
			}
			if(v.size()==9){
				cout<<getBinary(i,N-2)<<" ";
				for(int p=0;p<v.size();p++){
					cout<<v[p].second<<" ";
				}
				c++;
				cout<<endl;
			}
		}

	}
	
}