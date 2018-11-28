#include<iostream>
#include<cstdio>

using namespace std;

int main()
{
	
	int cases, a,b,k,c ;
	cin >> cases;

	for(int n = 1 ; n<=cases ; ++n)
	{
        
		cout << "Case #" << n << ": " ;

		cin >> a >> b >> k;
		c=0;
		
		for(int i=0 ; i<a ; i++)
		        for(int j=0 ; j<b ; j++)
		                if((i&j) < k && (i&j)>=0)
		                         c++;
		    cout << c << endl;
    }
}
