#include <iostream>
#include <set>
#include <vector>
using namespace std;

int iNaKupce, iMonet, DoIlu;
vector<int> monety;

int dasieDodawac(int ile);
vector<int> nastPermutacja(vector<int> tmp);
int plecak();
int positive(vector<int> d, int i);
int niemaPowtorzen(vector<int> tmp);

int main()
{
	int ilez;
	cin>>ilez;
	for(int aa=0; aa<ilez; aa++)
	{
		cin>>iNaKupce>>iMonet>>DoIlu;
		int tmp;
		for(int i=0; i<iMonet; i++)
		{
			cin>>tmp;
			monety.push_back(tmp);
		}

		int iDodac=0;
		
		while(1)
		{
			if(!dasieDodawac(iDodac))
				iDodac++;
			else break;
		}
		
		cout<<"Case #"<<aa+1<<": "<<iDodac<<endl;

		monety.clear();


	}
}
int dasieDodawac(int ile)
{
	if(ile==0)
		return plecak();
	
	vector<int> tmp;
	for(int i=0; i<ile; i++)
	{
		tmp.push_back(1+i);
	}


	while(1)
	{
		if(niemaPowtorzen(tmp))
		{
			for(int i=0; i<tmp.size(); i++)
			{
				monety.push_back(tmp[i]);
			}
			if(plecak()) return 1;
			for(int i=0; i<tmp.size(); i++)
			{
				monety.pop_back();
			}
		}

		tmp=nastPermutacja(tmp);
		
		int suma=0;
		for(int i=0; i<tmp.size(); i++)
		{
			suma+=tmp[i];
		}
		if(suma==tmp.size()) return 0;

	}
}
vector<int> nastPermutacja(vector<int> tmp)
{
	tmp[0]++;
	for(int i=0; i<tmp.size(); i++)
	{
		if(tmp[i]>DoIlu)
		{
			tmp[i]=1;
			if(i+1!=tmp.size())
			tmp[i+1]++;
		}
		else break;
	}
	return tmp;
}
int plecak()
{
	vector<int> dasie;
	for(int i=0; i<=DoIlu; i++) dasie.push_back(0);
	dasie[0]=1;
	for(int i=0; i<monety.size(); i++)
	{
		for(int q=0; q<iNaKupce; q++)
		for(int k=dasie.size()-1; k>=0; k--)
		{
			if(positive(dasie, k-monety[i]))
				dasie[k]=1;
		}
	}
	for(int i=0; i<dasie.size(); i++)
	{
		if(dasie[i]==0) return 0;
	}
	return 1;
}
int positive(vector<int> d, int i)
{
	if(i<0) return 0;
	return d[i];
}
int niemaPowtorzen(vector<int> tmp)
{
	set<int> s;
	for(int i=0; i<tmp.size(); i++)
	{
		s.insert(tmp[i]);
	}
	for(int i=0; i<monety.size(); i++)
	{
		s.insert(monety[i]);
	}

	if(s.size()==tmp.size()+monety.size()) return 1;
	return 0;
}
