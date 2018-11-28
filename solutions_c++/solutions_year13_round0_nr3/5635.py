#include <algorithm>
#include <functional>
#include <utility>
#include <memory>
#include <numeric>
#include <iterator>

#include <string>
#include <bitset>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <deque>

#include <stdexcept>
#include <iomanip>
#include <iostream>
#include <sstream>
#include <fstream>

#include <cstdlib>
#include <cstring>
#include <cassert>
#include <cctype>
#include <cstdio>
#include <ctime>
#include <cmath>

using namespace std;
bool isfair(int s)
{
	int v[20];
	int i=0;
	while(s)
	{
		v[i] = s%10;
		s = s/10;
		++i;
	}

	for(int k=0; k<i/2; ++k )
	{
		if(v[k] != v[i-1-k]) return false;
	}
	return true;
}
int main()
{
	int T;
	cin>>T;
	for( int t=1; t<=T; ++t )
	{
		int A,B;
		cin>>A>>B;
		int n=0;

		int up=floor(sqrt(double(B)));
		for(int i=ceil(sqrt(double(A))); i<=up; ++i)
		{
			int s=i*i;
			if(isfair(i) && isfair(s)) { n++; }
		}
		cout<<"Case #"<<t<<": ";
		cout<<n<<endl;
	}

	return 0;
}
