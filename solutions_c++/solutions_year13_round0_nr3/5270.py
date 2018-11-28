#include <iostream>
#include <sstream>
#include <vector>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <fstream>

using namespace std;


//long long vec[1010];


//long long toi(string s){istringstream is(s);long long x;is>>x;return x;}
string tos(long long t){stringstream st; st<<t;return st.str();}


bool es_pali(long long a)
{
	string aa = tos(a);
	string b = aa;
	reverse(b.begin(),b.end());
	return (aa==b);
}



int main()
{
	
	//freopen("C-small-attempt0.in","r",stdin);
	//freopen("outputc.out","w",stdout);

	vector<long long> vec(1010,-1);
	vector<long long> esp(1010,-1);
	for(int i = 1; i < 1010 ; i++)
		if(es_pali(i))
		{
			esp[i]=1;
			int ra = (int)sqrt(i);
			if(ra*ra == i && esp[ra]==1)
			{
				vec[i]=ra;
			}
		}

	int n;

	cin>>n;
	int a,b;
	for(int caso=1;caso<=n;caso++)
	{
		cin>>a>>b;
		int res=0;
		for(int i  = a; i<=b;i++)
			if(vec[i]!=-1)res++;
		cout<<"Case #"<<caso<<": "<<res<<endl;
	}

	return 0;
}
