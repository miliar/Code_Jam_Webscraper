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
   	int N = 0;
   	int war =0;
   	int d_war =0;

    
    std::vector<double> myvector1;
    std::vector<double> myvector2;
    double input;

	cin >> case_num;
	
	for ( cn = 0; cn < case_num; cn++) {

    cin >> N;

    war = 0; d_war =0;
 
    myvector1.clear();
    myvector2.clear();


      for (int i = 0; i < N; i++) {
          cin >> input;
          myvector1.push_back (input);
          }
          
      std::sort (myvector1.begin(), myvector1.end()); 
      
      for (int i = 0; i < N; i++) {
          cin >> input;
          myvector2.push_back (input);
          }
      
       
      std::sort (myvector2.begin(), myvector2.end());  

/*
      for (std::vector<double>::iterator it=myvector1.begin(); it!=myvector1.end(); ++it)
    std::cout << ' ' << *it;
    std::cout << '\n';
    
    for (std::vector<double>::iterator it=myvector2.begin(); 
      it!=myvector2.end(); ++it)
    std::cout << ' ' << *it;
    std::cout << '\n';
    */
    
    //Deceitful War
    j=0;
    for (int i = 0; i < N; i++) {
        if ( myvector2[j] < myvector1[i]  ) {
			j++;
			d_war++;					
		}
    }
    
    cout << "Case #" << cn + 1 << ": "  << d_war << " " ;
    
    //War
    j=N-1;
    for (int i = N-1; i >= 0; i--) {
		if ( myvector2[j] <= myvector1[i] ) 
		   war++;				
         else j--;
    }
      	
		
	cout << war << endl;
		
	}
}



