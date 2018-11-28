#include <iostream>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;


int main()
{
	int t;
	int cont=1;
	int n,m;
	int alt;
	int final[100][100];
	bool possivel;
	bool aux;
	cin>>t;
	for(int i=0;i<t;i++)
	{
		possivel=true;
		cin>>n;
		cin>>m;
		for(int j=0;j<n;j++)
			for(int k=0;k<m;k++)
				cin>>final[j][k];
		for(int j=0;j<n && possivel;j++)
		{
			for(int k=0;k<m && possivel;k++)
			{
				alt=final[j][k];
				for(int l=0;l<n && possivel;l++)
				{
					if(final[l][k]>alt)
						possivel=false;
				}
				if(!possivel)
				{
					possivel=true;
					for(int l=0;l<m && possivel;l++)
					{
						if(final[j][l]>alt)
							possivel=false;
					}
				}
			}
		}
		cout<<"Case #"<<cont<<": ";
		if(possivel)
			cout<<"YES\n";
		else
			cout<<"NO\n";
		cont++;
	}
}