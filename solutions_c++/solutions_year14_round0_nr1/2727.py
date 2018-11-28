#include <stdlib.h>
#include <fstream>
using namespace std;

int main ()
{
	ifstream R("A-small-attempt0.in");
    ofstream W("A-small-attempt0.out");
    
    int t;
    R>>t;
    int ans1, ans2, table1[5][5], table2[5][5];
    for (int ti=1;ti<=t;++ti)
    {
    	R>>ans1;
    	for (int row = 1; row <= 4; row ++ )
    		for (int col = 1; col <=4; col ++)
    			R>>table1[row][col];
    			
    	R>>ans2;
    	for (int row = 1; row <= 4; row ++ )
    		for (int col = 1; col <=4; col ++)
    			R>>table2[row][col];    	
    	
    	int count = 0;
    	int number;
    	
    	for (int i = 1; i <=4 ; i++)
    		for(int j = 1 ;j<=4 ;j++)
    			if(table1[ans1][i] == table2[ans2][j])
    			{
    				count ++;
    				number = table1[ans1][i];
    				break;
    			}
    	
    	if(count ==0)
			W<<"Case #"<<ti<<": "<<"Volunteer cheated!"<<endl;
		
		if(count ==1)
			W<<"Case #"<<ti<<": "<<number<<endl;
			
		if(count >=2)
			W<<"Case #"<<ti<<": "<<"Bad magician!"<<endl;
	}
}
