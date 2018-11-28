#include <iostream>
#include <fstream>
#include <string>
#include <cstring>
using namespace std;

int main()
{
	freopen("b2222.in","r",stdin);
	freopen("b2222.out","w",stdout);
	int T;
	cin>>T;
	for (int id=1;id<=T;id++)
	{
		int n;cin>>n;
		string sa,sb;
		cin>>sa>>sb;
		int la=sa.length();
		int lb=sb.length();
		int ia=0,ib=0;
		int flag=0;
		int sum=0;
		while (ia!=la && ib!=lb)
		{	
			while (sa[ia]!=sb[ib])
			{
				if (sa[ia-1]==sa[ia]) {ia++;sum++;}
				else
				{
					if (sb[ib-1]==sb[ib]) {ib++;sum++;}
					else
					{
						flag=1;
						break;
					}
				}
			}
			if (flag==1) break;
			else{ia++;ib++;}
		}
		if (flag==1) {cout <<"Case #"<<id<<": Fegla Won"<<endl;continue;}
		if (ia==la)
		{
			int ff=0;
			for (int i=ib;i<lb;i++)
			{
				if (sb[i]!=sa[la-1]) {cout <<"Case #"<<id<<": Fegla Won"<<endl;ff=1;break;}
			}
			if (ff==0) {sum+=lb-ib;cout <<"Case #"<<id<<": "<<sum<<endl;}
		}
		else
		{
			if (ib==lb)
			{
				int ff=0;
				for (int i=ia;i<la;i++)
				{
					if (sa[i]!=sb[lb-1]) {cout <<"Case #"<<id<<": Fegla Won"<<endl;ff=1;break;}
				}
				if (ff==0) {sum+=la-ia;	cout <<"Case #"<<id<<": "<<sum<<endl;}
			}
		}
	}
	return 0;
}