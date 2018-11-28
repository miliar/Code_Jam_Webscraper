#include <iostream>
#include <vector>
#include <set>
#include <string>
#include <map>
#include <utility>
#include <algorithm>
#include <cmath>
#include <deque>
using namespace std;

#define FROM_FILE

void prepare()
{
	ios_base::sync_with_stdio(0);
#ifdef FROM_FILE
	freopen("E:\\in.txt", "r", stdin);
	freopen("E:\\out.txt", "w", stdout);
#endif
}

void normalize(int &m, int &n)
{
	if(m>n)
		swap(m,n);
}

bool myBydloCodeFunction(int nOmino, int m, int n)
{
	normalize(m,n);
	if(nOmino==1)
		return true;
	if(nOmino==2)
	{
		if(m==1 && n==1)
			return false;
		if(m==1 && n==3)
			return false;
		if(m==3 && n==3)
			return false;
		return true;
	}
	if(nOmino==3)
	{
		if(m==2 && n==3)
			return true;
		if(m==3 && n==3)
			return true;
		if(m==3 && n==4)
			return true;
		return false;
	}
	if(nOmino==4)
	{
		if(m==3 && n==4)
			return true;
		if(m==4 && n==4)
			return true;
		return false;
	}
}

int main()
{
	prepare();
	int T;
	cin>>T;
	int a, b, c;
	for(int i=0; i<T; ++i)
	{
		cin>>a>>b>>c;
		bool answ = myBydloCodeFunction(a,b,c);
		if(answ)
			cout<<"Case #"<<i+1<<": GABRIEL"<<endl;
		else
			cout<<"Case #"<<i+1<<": RICHARD"<<endl;
	}
	return 0;
}







