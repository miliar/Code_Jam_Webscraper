#include <bits/stdc++.h>
using namespace std;
string el(string a)
{
	string aux="";
	aux+=a[0];
	int j=0;
	for(int i=1;i<a.size();i++)
		if(a[i]!=aux[j])
			aux+=a[i], j++;
	return aux;
}
int main()
{
	int t;
	scanf("%i", &t);
	string a;
	for(int i=1;i<=t;i++)
	{
		cin>>a;
		a=el(a);
		if(a.size()==1)
			if(a[0]=='+')
			{
				printf("Case #%i: 0\n", i);
				continue;
			}
			else
			{
				printf("Case #%i: 1\n", i);
				continue;
			}
		if(a[0]=='-' and a.size()%2==1)
			printf("Case #%i: %i\n", i,  a.size());
		else
			if(a[0]=='-' and a.size()%2==0)
				printf("Case #%i: %i\n", i, a.size()-1);
			else
				if(a[0]=='+' and a.size()%2==1)
					printf("Case #%i: %i\n", i,  a.size()-1);
				else
					printf("Case #%i: %i\n", i, a.size());
	}

	return 0;
}