#include <iostream>
#include <cmath>
#include <string.h>
#include <list>
using namespace std;

long long convert(string s, int base){
	long long ret = 0;
	int len = s.size()-1;
	for(int i=len; i>=0; i--){
		if(s[i] == '1'){
			ret += pow(base, len-i);	
		}
	}
	return ret;
}

void recurse(string s, int index, list<string>& q){
	if(index == s.size()-1){
		q.push_back(s);
		return;
	}
	s[index] = '0';
	recurse(s, index+1, q);
	s[index] = '1';
	recurse(s, index+1, q);
	
	return;
}

long long fact(long long num){
	int last = sqrt(num);
	last++;
	for(int i=2; i<=last; i++){
		if(num%i == 0)
			return i;
	}
	return -1;
}

int main() {
	int t;
	static int count = 0;
	list<string> L;
	list<long long> F;
	cin>>t;
	for(int i=1; i<=t; i++){
		count = 0;
		L.clear();
		int N, J;
		cin>>N>>J;
		string s = "1";
		for(int j=1; j<N-1; j++){
			s += '0';
		}
		s+= '1';
		recurse(s, 1, L);
		
		cout<<"Case #"<<i<<":"<<endl;
		for(list<string>::iterator it = L.begin(); it != L.end(); it++){
			F.clear();
			for(int k=2; k<=10; k++){
				long long number = convert(*it,k);
				long long temp = fact(number);
				if( temp > 0){
					F.push_back(temp);
				}
				else
				{
					
					break;
				}
			}
			if(F.size() == 9){
				count++;
				cout<<*it;
				for(list<long long>::iterator iit = F.begin(); iit != F.end(); iit++){
					cout<<" "<<*iit;
				}
				cout<<endl;
			}
		
			if(count == J)
			break;
		
		}
		
	}
	return 0;
}