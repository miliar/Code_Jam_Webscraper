#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cctype>
#include <climits>
#include <ctime>
#include <algorithm>
using namespace std;
//#define BENCHMARK

int t,T;

inline void Do(){
	string s;
	cin>>s;
	char c[1005];
	int i=0,j=1;
	c[0]=s[0];
	int p,len=s.length();
	for(p=1;p<len;++p){
		if(s[p]>=c[i]){
			if(--i<0)
				i+=1005;
			c[i]=s[p];
		}
		else
			c[j++]=s[p];
	}
	char str[1005];
	p=0;
	while(i!=j){
		str[p++]=c[i];
		i=(++i)%1005;
	}
	str[p]='\0';
	cout<<str;
}

int main(int argc,char **argv){
	cin>>T;
	for(t=1;t<=T;++t){
		cout<<"Case #"<<t<<": ";
		Do();
		cout<<'\n';
	}

#ifdef BENCHMARK
	printf("Time elapsed: %.3f sec\n",(float)clock()/CLOCKS_PER_SEC);
#endif
	return 0;
}