#include<iostream>
#include<vector>
#include<algorithm>
#include<fstream>

using namespace std;

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("output.out","w",stdout);
	int t;
	cin>>t;
	for(int caset=1;caset<=t;caset++)
	{
		double c,f,x;
		cin>>c>>f>>x;
		double p=2;
		double prev=x/p;
		double curr=(c/p)+(x/(p+f));
		double s=0;
		p=p+f;
		while(prev>curr)
		{
			if(prev<=curr)
				break;
			prev = curr;
			curr = curr - (x/p) + (c/p) + (x/(p+f));
			p = p+f;
		}
		cout << "Case #" << caset << ": ";
		printf("%.7lf\n",prev);
	}
	return 0;
}