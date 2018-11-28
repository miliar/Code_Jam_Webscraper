#include<iostream>
#include<cstring>

using namespace std;

void reverse(char s[],int k)
{
	int l=0, r=k;
	while (l<r)
	{
		swap(s[l++],s[r--]);
	}
	for (int i=0; i<=k; i++)
	{
		if (s[i]=='+')
		{
			s[i]='-';
		}
		else
		{
			s[i]='+';
		}
	}
}

int main()
{
	char s[101];
	int T,i=1,k,dl,kol=0,rez=0;
	cin>>T;
	for (int q=1; q<=T; q++)
	{
		cin>>s;
		rez=0;
		kol=0;
		cout<<"Case #"<<q<<": ";
		dl=strlen(s);
		if (dl==1 && s[0]=='-')
		{
			cout<<"1"<<endl;
		}
		else
		{
			for (int j=0; s[j]; j++)
			{
				if (s[j]=='+')
				{
					kol++;
				}
			}
			if (kol==0)
			{
				cout<<"1"<<endl;
			}
			while ((kol!=dl) && (kol!=0))
			{
				i=1;
				while (s[i]==s[i-1] && s[i])
				{
					i++;
				}
				k=i-1;
				reverse(s,k);
				rez++;
				kol=0;
				for (int j=0; s[j]; j++)
				{
					if (s[j]=='+')
					{
						kol++;
					}
				}
				if (kol==0)     // то есть все минусы
				{
					cout<<rez+1<<endl;
				}
			}
			if (kol!=0)
			{
				cout<<rez<<endl;
			}
		}
	}
	return 0;
}