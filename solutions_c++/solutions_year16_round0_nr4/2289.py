#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <vector>
#include <string.h>
#include <math.h>

using namespace std;




int main(int argc, char const *argv[])
{
	int N,k,c,s;
	cin>>N;
	for (int ii = 1; ii <= N; ++ii)
	{
		cin>>k>>c>>s;
		cout<<"Case #"<<ii<<": ";
		for (int i = 0; i < s; ++i)
		{
			cout<<i+1<<" ";
		}
		cout<<endl;
	}
	return 0;
}