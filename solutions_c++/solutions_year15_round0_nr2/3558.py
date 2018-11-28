#include <fstream>
#include <math.h>
#include <vector>
#include <algorithm>
using namespace std;

void resi(int i, ifstream &cin, ofstream &cout)
{
	vector<int>zasedenost;
	int kroznikov;
	cin>>kroznikov;
	for(int j=0;j<kroznikov;j++)
	{
		int polni;
		cin>>polni;
		zasedenost.push_back(polni);
	}
	sort(zasedenost.rbegin(),zasedenost.rend());
	int minimum=zasedenost.at(0);
	int f=zasedenost.at(0)+1;
	for(int j=1;j<f;j++)
	{
		int potrebnih=0;
		for(int k=0;k<kroznikov;k++)
		{
			if(zasedenost.at(k)>=j)
			{
				int a=(zasedenost.at(k)+j-1)/j-1;
				//cout<<a<<endl;
				potrebnih=potrebnih+a;
			}
		}
		potrebnih+=j;
		if(potrebnih<minimum)
			minimum=potrebnih;
		//cout<<j<<" "<<potrebnih<<endl;
	}
	cout<<"Case #"<<i+1<<": "<<minimum<<endl;
}

int main()
{
	ifstream cin("/home/simon/Downloads/B-large.in");
	ofstream cout("/home/simon/palacinke.out");
	int primerov;
	cin>>primerov;
	for(int i=0;i<primerov;i++) resi(i,cin,cout);
	cin.close();
	cout.close();
}
