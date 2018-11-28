#include <iostream>
#include <fstream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <string>
#include <set>
#include <iomanip>
#include <vector>
#include <map>

#define p_b push_back
#define m_p make_pair


using namespace std;

int a,b,k,i,j,sum,t,tt;

int main()
{
	//ios_base::sync_with_stdio(false);
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	cin>>t;
	for (tt=1; tt<=t; tt++)
	{
		cin>>a>>b>>k;
		sum=0;
		for (i=0; i<a; i++)
			for (j=0; j<b; j++)
			{
				if ((i & j)<k) sum++;
			}
		cout<<"Case #"<<tt<<": "<<sum<<endl;
	}
	return 0;
}


