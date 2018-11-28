#include <iostream>
#include <iomanip>
#include <stdio.h>
#include <set>
#include <vector>
#include <numeric> 
#include <map>
#include <cmath>
#include <algorithm>
#include <memory.h>
#include <string>
#include <sstream>
using namespace std;
int main(){
	int n;
	long long t,p,q,k,m;
	double temp,test;
	string s;
	freopen("A-large.in", "rt", stdin);
  	freopen("outputA-large-attempt1.txt", "wt", stdout);
	cin>>t;
	for(k=0;k<t;k++){
		cin>>s;
		string delimiter = "/";

		size_t pos = 0;
		string token;
	while ((pos = s.find(delimiter)) != string::npos) {
    	token = s.substr(0, pos);
    	p = atoll(token.c_str());
   		s.erase(0, pos + delimiter.length());
	}
		q = atoll(s.c_str());
		//cout<<p<<" "<<q<<endl;
		n=0; temp = (double)p/(double)q;
		//cout<<temp;
		while(n<40 && temp<1.0){
			temp=temp*2;n++;
			//cout<<"yes"<<endl;
		}
		m=0;
		test=temp-floor(temp);
		if(temp-floor(temp)!=0){
			while(m<40-n && test-floor(test)!=0){
				test=test*2;
				m++;
			}
		}
		
		
			

	if(n>=40 || m>=40-n)
	cout<<"Case #"<<(k+1)<<": "<<"impossible"<<endl;
	else if (n<40 && m<40-n)
	cout<<"Case #"<<(k+1)<<": "<<n<<endl;
		
	}
	return 0;
}

