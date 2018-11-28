#include <string>
#include <iostream>
using namespace std;
int main()
{

	int n;
	cin>>n;
	for(int y=0;y<n;y++)
	{
		int k;
		string aud;
		cin>>k>>aud;
		int total=0;
		int needed=0;
		for(int x=0;x<k+1;x++)
		{
			if(aud[x]!='0')
			{
				if(total<x)
				{
					needed+=x-total;
				}
				total+=(int)aud[x]-48+needed;
			}
		}
		cout<<"Case #"<<y+1<<": "<<needed<<endl;
	}
	return 0;
}