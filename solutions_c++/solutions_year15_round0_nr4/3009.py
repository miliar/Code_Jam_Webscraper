#include <iostream>
using namespace std;

int wypisane[100];
int tab[3];
void wypisz(int i, int a);

int main()
{
	int ile;
	cin>>ile;
	for(int i=0; i<ile; i++)
	{
		cin>>tab[0]>>tab[1]>>tab[2];

		if(tab[2]>tab[1]) swap(tab[1], tab[2]); //tab2 mniejszy
		if(tab[0]>tab[1]) wypisz(i,0);
		if(tab[0]==1) wypisz(i, 1);
		if(tab[1]==2 && tab[2]==1)
		{
			wypisz(i,1);
		}
		if(tab[1]==2 && tab[2]==2)
		{
			if(tab[0]==3) wypisz(i, 0);
			else wypisz(i, 1);
		}
		if(tab[1]==3 && tab[2]==1)
		{
			wypisz(i,0);
		}
		if(tab[1]==3 &&tab[2]==2)
		{
			if(tab[0]==2 || tab[0]==3) wypisz(i, 1);
			wypisz(i, 0);
		}
		if(tab[1]==3 &&tab[2]==3)
		{
			if(tab[0]==3) wypisz(i, 1);
			wypisz(i, 0);
		}
		if(tab[1]==4 && tab[2]==1)
		{
			if(tab[0]==3 || tab[0]==4) wypisz(i, 0);
			wypisz(i, 1);
		}
		if(tab[1]==4 && tab[2]==2)
		{
			if(tab[0]==2) wypisz(i, 1);
			wypisz(i, 0);
		}
		if(tab[1]==4 && tab[2]==3)
		{
			wypisz(i, 1);		
		}
		if(tab[1]==4 && tab[2]==4)
		{
			if(tab[0]==3) wypisz(i, 0);
			wypisz(i, 1);
		}
	}
}

void wypisz(int i, int a)
{
	i++;
	if(wypisane[i]>0)
		return;
	wypisane[i]=1;
	cout<<"Case #"<<i<<": ";
	if(a)
		cout<<"GABRIEL";
	else cout<<"RICHARD";
	cout<<endl;
}
