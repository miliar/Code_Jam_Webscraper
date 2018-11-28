#include <iostream>
#include <algorithm>
#include <vector>
#include <deque>
#include <map>
#include <string>
#include <math.h>
using namespace std;

int main()
{
 int case_num = 0;
      int i=0, j=0 ;
      	int cn = 0;
      int farm=0;
      
    double c , f ,x ;
    double ans, time;
    

	cin >> case_num;
	
	for ( cn = 0; cn < case_num; cn++) {

    
    cin >> c >> f >> x; 
    ans = ((f * (x-c)) - (2*c)) / (f*c) ;
    farm = (int) ceil(ans);
    if (farm < 0) farm=0;
    
    time=0;
    	
		cout << "Case #" << cn + 1 << ": ";
		
			//cout << ans << endl;
			for (i=0 ; i <=farm-1 ; i++)
			    time+= c / (2 + (i*f) );
          time+= x/ (2+(farm * f));
	
           cout<<std::fixed;
           cout.precision(7);
           cout << time << endl;		
	}
}



