#include <iostream>
#include <algorithm>
#include <vector>
#include <deque>
#include <map>
#include <string>
using namespace std;

int main()
{
	int cn = 0;

    int m[4][4];
    int k[4][4];
    int row1=0, row2=0;
    int case_num = 0;
    int i=0, j=0 ;
    
    //initialization
    for ( i = 0; i < 4; i++) {
			for ( j = 0; j < 4; j++)
				m[i][j]=0;
                k[i][j]=0;
		}
    
	cin >> case_num;
	
	for ( cn = 0; cn < case_num; cn++) {

        cin >> row1;
        row1--;
        
        for ( i = 0; i < 4; i++) {
			for ( j = 0; j < 4; j++)
				cin >> m[i][j];
		}
        
        cin >> row2;
        row2--;
        
		for ( i = 0; i < 4; i++) 
			for ( j = 0; j < 4; j++)
				cin >> k[i][j];
		

		int exist = 0;
		int cheat = 0; //1 means m cheat, 2 means v cheat
		
		for ( i = 0; i < 4; i++) {			
			for ( j = 0; j < 4; j++)
				if (m[row1][i]== k[row2][j]) {
				   exist++; 
				   //cout << "cn is " << cn << endl;
				   //cout << "m[row1][i]" << m[row1][i]<< endl;
				   //cout << "k[row2][j]" << k[row2][j]<< endl;
				   //cout << "exist is " << exist << endl;
                 }
		}
		if (exist > 1  )
           cheat = 1;
        else if (exist == 0)
                  cheat = 2;
		
		int ans = 0;
		if (exist ==1 ) {
           for ( i = 0; i < 4; i++) {			
			for ( j = 0; j < 4; j++)
				if (m[row1][i]== k[row2][j]) {
				   ans =  m[row1][i];
                 }
		}
    }
		
		cout << "Case #" << cn + 1 << ": ";
		if (cheat == 0)
			cout << ans << endl;
		else if (cheat == 1)
			cout << "Bad magician!" << endl;	
            else if (cheat == 2)
			cout << "Volunteer cheated!" << endl;		
	}
}



