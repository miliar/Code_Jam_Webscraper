#include <iostream>
#include <fstream>
using namespace std;
int main()
{
	ifstream I("A2.in");
	ofstream O("A2.out");
	int t;
	string res,s,aux;
	I>>t;
	for(int i=1;i<=t;i++)
	{
		I>>s;
		res+=s[0];
		for(int j=1;j<s.size();j++)
		{
			if(int(s[j])>=int(res[0]))
			{
				aux=res;
				res=s[j];
				res+=aux;
			}
			else
			{
				res+=s[j];
			}
			//cout<<res<<endl;
		}
		O<<"Case #"<<i<<": "<<res<<endl;
		res.clear();
		aux.clear();
	}
	return 0;
}