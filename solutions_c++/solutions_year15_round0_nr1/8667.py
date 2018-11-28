#include <iostream>
#include <iomanip>
using namespace std;
int main()
{
    int t, sMax, s, fn, currentStand;
    char shy[1010], ss;
    cin >> t;
           
    for(int i=0; i<t; i++){
    	cin >> sMax;
    	cin >> shy;
    	
    	fn = 0;
    	    	
    	ss = shy[0];
    	s = ss - '0';
    	currentStand = s;
    	
    	if(s == 0){
    		fn++;
    		currentStand++;
		}
    	for(int j=1; j<=sMax; j++){
    		ss = shy[j];
    		s = ss - '0';
    		
    		if(j > currentStand && s > 0){
    			fn = fn + (j-currentStand);
    			currentStand += (j-currentStand);
			}
    		    			
    		currentStand += s;	
		}
		cout << "Case #" << i+1 << ": "<< fn;
		cout << endl;
    	
	}
}
