#include <iostream>
#include <vector>
#include <fstream>
using namespace std;

double time1 (double act, double x, double f ){
	return (x/(act+f));
}

double time2(double act, double x)
{
	return x/act;
}

int main()
{
		   ifstream plik("B-large.in");
		   ofstream wynik("wynik.txt");
			int n;
			double c,f,x,act=2.0,pom=0.0;

			plik>>n;

			for(int i=1;i<=n;i++)
			{
				wynik.precision(15);

				plik>>c>>f>>x;
				pom=0.0;
				act=2.0;
				while(time1(act,x,f)+c/act<time2(act,x))
						{
							pom+=c/act;
							act+=f;
						}
				wynik<<"Case #"<<i<<": ";
				wynik<<pom+x/act<<endl;
			}
								plik.close();
								wynik.close();

            return 0;
}

