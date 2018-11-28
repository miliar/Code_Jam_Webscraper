#include <iostream>
#include <fstream>
#include <cmath>
#include <cstdio>

using namespace std;

bool isFF(unsigned long long x) {
	char sx[101]={0};
	sprintf(sx,"%llu",x);
	int j=strlen(sx)-1;
	int i=0;
	for (;i<j;i++,j--)
		if (sx[i]!=sx[j])
			return false;
	sprintf(sx,"%llu",x*x);
	j=strlen(sx)-1;
	i=0;
	for (;i<j;i++,j--)
		if (sx[i]!=sx[j])
			return false;
	return true;
}

int mysolve(ifstream &fi)  {
	int res(0);
	unsigned long long x,y;
	unsigned long long m,n,a,b;
	fi>>m>>n;
	a=ceil(sqrt((long double)m));
	b=floor(sqrt((long double)n));
	for (unsigned long long i=a;i<=b;++i)
		if (isFF(i)) res++;
	return res;
}

int main()  {
	int n(0);
	int res(0);
	//ifstream fi("test.txt");
	ifstream fi("C-small-attempt0.in");
	//ifstream fi("B-large.in");
	ofstream fo("output.txt");
	fi>>n;
	for (int i(0);i<n;++i)  {
		res=mysolve(fi);
		cout<<"Case #"<<i+1<<": "<<res<<endl;
		fo  <<"Case #"<<i+1<<": "<<res<<endl;
	}
	//cin>>n;
	return 0;
}