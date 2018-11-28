#include <iostream>       // std::cout
#include <string>         // std::string
#include <stdio.h>
#include <sstream>
#include <vector>
#include <limits.h>
using namespace std;

// Number -> String
template <typename T>
  string NumberToString ( T Number )
  {
     ostringstream ss;
     ss << Number;
     return ss.str();
  }

long long sheep(long long N){
	if(N==0){
		return 0;
	}
	long long ans=0;
	long long i;
	i=1;
	vector<char> digits;
	digits.clear();
	digits.push_back('0');
	digits.push_back('1');
	digits.push_back('2');
	digits.push_back('3');
	digits.push_back('4');
	digits.push_back('5');
	digits.push_back('6');
	digits.push_back('7');
	digits.push_back('8');
	digits.push_back('9');
	digits.push_back('*');	//extra char
	string N_str;
	ans=i*N;
	bool found;
	while(ans<LLONG_MAX && digits.size()>1){ //LLONG_MAX
		N_str=NumberToString(ans);
		for(int j=0;j<N_str.length();j++){
			for(int m=0;m<digits.size();m++){
				if(N_str[j]==digits[m]){
					digits.erase (digits.begin()+m);
				}
			}
		}
		i++;
		ans=i*N;
	}
	if(digits.size()==1){
		i--;
		ans=i*N;
		return ans;
	}
	return 0;
}


int main(){
	int T,i;
	long long N,res;
	cin>>T;
	for(i=0;i<T;i++){
		cin>>N;
		res=sheep(N);
		if(res==0){
			cout<<"Case #"<<i+1<<": INSOMNIA\n";
		}
		else{
			cout<<"Case #"<<i+1<<": "<<res<<"\n";
		}
	}
	
	return 0;
}
