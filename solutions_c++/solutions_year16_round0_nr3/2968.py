#include<bits/stdc++.h>
#include<stdint.h>
#include<sstream>
using namespace std;

bool isOne(int64_t n,int64_t u){
	int64_t x = 1;
	if(((x<<u) & n) &&  (1&n)){
		return true;
	}
	return false;
}

bool isPrime(int64_t n){
	for(int64_t i=2;i*i<=n;i++){
		if(n%i == 0){
			return false;
		}
	}
	return true;
}

bool getBase(int64_t n,int64_t base,int64_t x){
	
	int64_t sum = 0;
	int64_t y = 1,up = 1;
	for(int64_t i=0;i<x;i++){
		
		if((y<<i) & n){
			sum += up;
		}
		
		up*=base;
		
	}
	if(!isPrime(sum)){
		return true;
 	}
    return false;
}

int64_t getBase1(int64_t n,int64_t base,int64_t x){
	
	int64_t sum = 0;
	int64_t y = 1,up = 1;
	for(int64_t i=0;i<x;i++){
		
		if((y<<i) & n){
			sum += up;
		}
		
		up*=base;
		
	}
	return sum;
}

bool X(int64_t n,int64_t o){
	
	if(!isOne(n,o-1)) return false;
	
	bool f = true;
	for(int64_t i=2;i<=10;i++){
		f &= getBase(n,i,o);
	}
    return f;	
}

vector<int64_t> process(){
	vector<int64_t> v;
	for(int64_t i=1;i<=65535;i++){
		if(X(i,16)){
			cout<<i<<"\n";
			v.push_back(i);
		}
	}
	return v;
}


int getDiv(int64_t n){
	for(int64_t i=2;i*i <=n;i++){
		if(n%i == 0) return i;
	}
	return -1;
}

vector<int64_t> getList(int64_t n){
	vector<int64_t> v;
	for(int i=2;i<=10;i++){
		int64_t u = getBase1(n,i,16);
		
		int di = getDiv(u);
		//cout<<u<<" "<<di<<"\n";
		if(di != -1){
			v.push_back(di);
		}
	}
	return v;
}

string getBin(int64_t n){
	stringstream ss;
	while(n > 0){
		if(n%2 == 0){
			ss<<'0';
		}
		else{
			ss<<'1';
		}
		n/=2;
	}
	
	string s = ss.str();
	reverse(s.begin(),s.end());
	return s;
}

int main(){
	vector<int64_t> v = process();
	//v.push_back(35);
	int c = 0;
	
	for(int i=0;i<v.size();i++){
		vector<int64_t> vv = getList(v[i]);
		//return 0;
		//cout<<vv.size();
		if(vv.size() == 9){
			++c;
			cout<<getBin(v[i])<<" ";
			for(int j=0;j<vv.size();j++){
				cout<<vv[j]<<" ";
			}
			cout<<"\n";
			if(c == 50) return 0;
		}
	}
	
	
}
