#include<iostream>
#include<fstream>
using namespace std;
int main()
{
	int n,k,s=0,suma=0,dif;
	char c[1001];
	ifstream in("A-large.in");
	ofstream out("out.out");
	in>>n;
	for(int i=1;i<=n;i++)
	{
		in>>k;
		in>>c;		
		for(int j=1;j<=k;j++)
		{
			s+=((int)c[j-1]-48);
			if(j>s && ((int)c[j]-48)>0)
			{
				dif=j-s;
				s+=dif;
				suma+=dif;
			}
		}
		out<<"Case #"<<i<<": "<<suma<<endl;		
		s=0;
		suma=0;
	}
}