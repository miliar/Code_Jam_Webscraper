#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;




int main()
{
	int case_num = 0;
	int i,j,k,p,q,r,s,row,column =0;
	int lawnmower [100][100];
	string result = "";
	bool vertical,horizontal = false;
	bool status = false;
	cin >> case_num; 


    
	for (i = 0; i < case_num; i++) {
        status =vertical=horizontal= false;
        cin >> row >> column;
        for (j = 0; j < row; j++)
            for (k = 0; k < column; k++)
                cin >> lawnmower[j][k];
             /*   for display
        for (j = 0; j < row; j++){
            for (k = 0; k < column; k++)
                cout << lawnmower[j][k];
            cout << endl;
            }
               */ 
                
        for (p = 0; p < row; p++)
            for (q = 0; q < column; q++) {
                
                vertical = horizontal = false;
                
                for (r = 0; r < row; r++)
                    if (lawnmower[p][q] < lawnmower[r][q]) 
                     vertical = true;
                                    
                    //cout << "lawnmower(" <<p<< ","<<q<< ")<lawnmower("<<r<<","<<q<<")" << endl;
                    
                   
                for (s = 0; s < column; s++)
                    if (lawnmower[p][q] < lawnmower[p][s]) 
                       
                       horizontal = true;
                                        
                    //cout << "lawnmower(" <<p<< ","<<q<< ")<lawnmower("<<p<<","<<s<<")" << endl;
                    
                
                if (vertical && horizontal) status = true;
                                
                }//end of q loop
                
        if (status) result="NO"; else result = "YES";

		cout << "Case #" << i + 1 << ": " << result << endl;
	}//end of case_num loop
}

