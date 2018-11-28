#include<iostream>
#include<string>
using namespace std;
int tab[1010];
int main()
{
    ios_base :: sync_with_stdio(0);
    int t, x, suma, w;
    cin >> t;
    string y;
    for(int te = 0; te < t; te++)
    {
        suma = 0;
	w = 0;
        cin >> x >> y;
        
        for(int i = 0; i <= x; i++)
        {
            tab[i] = y[i] - '0';
            cout << y[i] - '0' << " ";
        }
        //if(suma >= x) cout << "Case #" << te+1 << " " << 0 << "\n";
        //else cout << "Case #" << te+1 << " " << x - suma << "\n";
        //for(int i = 0; i < 10; i++) cout << tab[i] << " ";
        suma += tab[0];
	for(int i = 1; i <= x; i++)
	{
	  if(tab[i] != 0)
	  {
	    if(suma < i)
	    {
	      w += (i - suma);
	      suma += (i - suma);
	      suma += tab[i];
	    }
	    else
	    {
	      suma += tab[i];
	    }
	  }
	}
	for(int i = 0; i <= x; i++) tab[i] = 0;
        cout << "Case #" << te+1 << ":"<< " " << w << "\n";
    }
    return 0;
}