#include<iostream>
#include<iomanip>
#include<string>
#include<vector>
#include<set>
#include<stack>
#include<queue>
#include<cmath>
#include<cstdio>
#include<stdlib.h>
#include<algorithm>
#include<fstream>
#include<memory.h>

using namespace std;

bool isp(long long in){
	vector <int> v;
	for(int i=1;i<=in;i*=10)
		v.push_back((int)(in%(i*10))/i);
	for(int i=0;i<(v.size()+1)/2;i++)
		if(v[i] != v[v.size()-1-i])
			return false;
	return true;
}

int main(){
	
	int t;
	cin>>t;
	for(int p=0;p<t;p++){
		long long a,b;
		cin>>a>>b;
		long long i = (long long)sqrt(a);
		if(i*i<a)
			i++;
		long long r =0;
		for(;i*i <= b;i++ ){
			if(isp(i)){
				if(isp(i*i)){
					//cout<<"#"<<i<<endl;
					r++;
				}
			}
		}
		cout<<"Case #"<<p+1<<": "<<r<<endl;
	}
	
	return 0;
}
