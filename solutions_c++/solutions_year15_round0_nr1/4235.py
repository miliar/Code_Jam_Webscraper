#include <fstream>
#include <vector>
#include <algorithm>
#include <stdlib.h>
#include <string>
using namespace std;


int main()
{
	ifstream cin("input.txt");
	ofstream cout("output.txt");
	int q;
	cin>>q;
	for (int qq=0;qq<q;qq++)
	{
		cout<<"Case #"<<qq+1<<": ";
		int cmax;
		cin>>cmax;
		int ans=0;
		int kol=0;
		string h;
		cin>>h;
		for (int i=0;i<=cmax;i++)
		{
			int f=h[i]-'0';
			while (f>0)
			{
				if (i>kol)
				{
					ans+=(i-kol);
					kol=i;
				}
				kol++;
				f--;
			}
		}
		cout<<ans<<endl;
	}
	return 0;
}
