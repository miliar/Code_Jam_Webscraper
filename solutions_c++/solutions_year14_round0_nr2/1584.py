#include<iostream>
using namespace std;

int main()
{
	int t; cin >> t;
	
	for(int i=1; i<=t; i++)
	{
		double c,f,x; cin >> c >> f >> x;
		
		//program
		double time = 0.0, produkcia = 2.0; 		
		while(true)
		{
			if( ( (c/produkcia) + (x/(produkcia+f)) ) < x/produkcia)
			{
				time+= c/produkcia;
				produkcia+=f;
			}
			else
			{
				time+= x/produkcia; 
				break;
			}
		
		}
		
		cout.setf(ios::fixed,ios::floatfield);
    	cout.precision(7);
		
		cout << "Case #" << i << ": " << time << endl;		
	}
	
	return 0;	
}





