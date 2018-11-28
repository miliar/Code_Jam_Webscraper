#include <iostream>
#include <string>
#include <sstream>
#include <cmath>
using namespace std;
bool espal(int k)
{
	ostringstream oss;
	oss << k;
	string s=oss.str();
	for(int i=0; i<s.size()/2;i++)
	{
		if(s[i]!=s[s.size()-1-i]) return false;
	}
	return true;
}
int main()
{
	int t, a,b;
	cin >>t;
	for(int i=0; i<t;i++)
	{
		cin >>a >>b;
		cout <<"Case #" <<i+1 <<": ";
		int cont=0;
		float sq=sqrt(a);
		bool fs=true;
		for(int j = (int) sq;j*j<=b;j++)
		{
			if (fs) if (j*j<a) continue;
			fs=false;
			if(espal(j)) if(espal(j*j)) cont++;//cout <<"---" <<j <<"---" <<j*j <<endl;}
		}
		cout <<cont <<endl;
	}
	return 0;
}
