#include <iostream>
#include <vector>
using namespace std;
#define int long long

string klaw, wzor;
vector<vector<int> >kombinacje;

void generate(int ile, int range);
int liczPowt(vector<int> kombinacja, string wzor);
int pasuje(vector<int> kombinacja, int i, string wzor);

main()
{
	int ilez;
	cin>>ilez;
	for(int aa=0; aa<ilez; aa++)
	{
		int iKlaw, iWzor, iPrzycisnie;
		cin>>iKlaw>>iWzor>>iPrzycisnie;

		cin>>klaw;
		cin>>wzor;

		kombinacje.clear();
		generate(iPrzycisnie, iKlaw);

//		for(int i=0; i<kombinacje.size(); i++)
//		{
//			for(int a=0; a<kombinacje[i].size(); a++)
//			{
//				cout<<kombinacje[i][a]<<" ";
//			}
//			cout<<endl;
//		}

		int maxi=0, suma=0;
		for(int i=0; i<kombinacje.size(); i++)
		{
			int tmp=liczPowt(kombinacje[i], wzor);
//			if(tmp>=0)
//			{
//				for(int a=0; a<kombinacje[i].size(); a++)
//				{
//					cout<<kombinacje[i][a]<<" ";
//				}
//				cout<<endl;
//			}
			maxi=max(maxi, tmp);
			suma+=tmp;
		}

		long double ilePrzyniesc=maxi;
		long double oczekiwana=(long double)suma/(long double)kombinacje.size();
		
		
		cout.precision(10);
		cout<<"Case #"<<aa+1<<": "<<ilePrzyniesc-oczekiwana<<endl;


	}
}
void generate(int ile, int range)
{
	vector<int> tmp;
	for(int i=0; i<ile; i++) tmp.push_back(0);

	kombinacje.push_back(tmp);
	while(1)
	{
		tmp[0]++;
		int suma=0;
		for(int i=0; i<ile; i++)
		{
			if(tmp[i]>=range)
			{
				tmp[i]=0;
				if(i+1!=ile)
				{
					tmp[i+1]++;
				}
			}
			suma+=tmp[i];
		}
		if(suma==0) break;
		else kombinacje.push_back(tmp);
		
	}
}
int liczPowt(vector<int> kombinacja, string wzor)
{
	int wynik=0;
	for(int i=0; i<kombinacja.size(); i++)
	{
		if(pasuje(kombinacja, i, wzor))
		{
			wynik++;
		}
	}
	return wynik;
}
int pasuje(vector<int> kombinacja, int i, string wzor)
{
	for(int a=0; a<wzor.size(); a++)
	{
		if((a+i)>=kombinacja.size()) return 0;
		if(wzor[a]!=klaw[kombinacja[i+a]]) return 0;
	}
	return 1;
}
