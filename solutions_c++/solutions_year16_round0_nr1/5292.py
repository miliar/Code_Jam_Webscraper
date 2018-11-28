#include <stdio.h>
#include <string>
#include <iostream>

using namespace std;

int main(void) {
    /* number of test cases */
    int t,j,h,ud;
    long n,aux;
    cin >> t;

    for(int i=1; i <= t; i++) { //loops for each case
        cin >> n;
        if (n == 0) 
        {
			cout << "Case #" << i << ": INSOMNIA" << endl;
		}
		else
		{
			std::string inicial = "abcdefghij";

			//cout << "Mi string inicial" << inicial << endl;
			//cout << "Mi N es : " << n << endl;
			h = 0;
			while ((inicial != "0123456789"))
			{
				h = h+1;
				aux = h * n;
				while ((aux!=0) && (inicial != "0123456789")){
					ud = aux % 10;
					aux = aux / 10;
					inicial[ud] = (char)( (int)'0' + ud );
				}
				//cout << "Para mi h = " << h << " el string inicial me dio " << inicial << endl;
			}
			
			cout << "Case #" << i << ": " << h*n << endl;
		}
        
    }

    return 0;

}

