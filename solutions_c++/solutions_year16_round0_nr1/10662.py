#include <iostream>
#include <iomanip>
#include <cstring>
using namespace std;

int main()
{
    int t;
    int ns[101], digit[10] = {0}, n,r,alldigit=0,nn;
    cin >> t;
           
    for(int i=0; i<t; i++){
    	cin >> ns[i];
        //cout << "ns[i]" << ns[i] <<endl;
    	memset(digit, 0, sizeof(digit));
    	
        n = ns[i];
        if(n == 0)
            cout << "Case #" << i+1 << ": "<< "INSOMNIA" << endl;
        else{
            int j = 1;
            alldigit = 0;
            while(alldigit != 10){
                n = ns[i] * j;
                nn = n;
                //cout << "NN: " << nn << endl;
                while(n > 0){
                    r = n % 10;
                    if(digit[r] == 0){
                        digit[r] = 1;
                        alldigit++;
                    }
                    n = n/10;
                }    	
            	j++;
            }
    		cout << "Case #" << i+1 << ": "<< nn;
    		cout << endl;
        }
    	
        //cout << ns[i];
	}
}
