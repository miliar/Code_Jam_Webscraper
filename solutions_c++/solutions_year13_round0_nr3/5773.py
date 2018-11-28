#include <iostream>
#include <sstream>
#include <string.h>
#include <vector>
#include <algorithm>
#include <math.h>

using namespace std;

int main()
{
	int n=0;
	int vi=0;
	int vf=0;
	int nro=0;
	int cont=1;
	string valor;
	cin>>n;
	for(int i=0; i<n; i++)
	{
		cin>>vi>>vf;

		for(int j=vi; j<=vf; j++)
		{
			stringstream ss;
			ss<<j;
			valor = ss.str();
			string v2 = valor;
			reverse(v2.begin(), v2.end());
			if(valor==v2)
			{			
				double d = (double)j;
				double d1 = sqrt(d);
				int i1 = (int)d1;
				if(i1==d1)
				{
					stringstream ss;
					ss<<i1;
					string vs = ss.str();
					string vs2 = vs;
					reverse(vs2.begin(),vs2.end());
					if(vs==vs2)			
						nro++;
				}
			}
		}

		cout<<"Case #"<<cont<<": "<<nro<<endl;
		cont++;
		nro=0;
	}

	return 0;
}
