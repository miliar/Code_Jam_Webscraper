#include <iostream>
using namespace std;
int main()
{
	int ilez;
	cin>>ilez;
	for(int aa=0; aa<ilez; aa++)
	{
		int ile;
		cin>>ile;
		char tmp;
		int ileStoi=0;
		int ileDodac=0;
		for(int i=0; i<ile; i++)
		{
			cin>>tmp;
			ileStoi+=tmp-'0';
			while(ileStoi<i+1)
			{
				ileDodac++;
				ileStoi++;
			}
		}
		cin>>tmp;
		cout<<"Case #"<<aa+1<<": "<<ileDodac<<endl;
	}
}
