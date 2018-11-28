#include <iostream>
using namespace std;
int main()
{
	int ilez;
	cin>>ilez;
	for(int aa=0; aa<ilez; aa++)
	{
		int R, C, W;
		cin>>R>>C>>W;

		int wynik=0;
		for(int i=1; i<R; i++)
		{
			wynik+=C/W;
		}
		while(C>=2*W)
		{
			wynik++;
			C-=W;
		}
		if(C==W)
		{
			wynik+=W;
		}
		else
		{
			wynik+=W;
			wynik++;
		}
		
		cout<<"Case #"<<aa+1<<": "<<wynik<<endl;


	}
}
