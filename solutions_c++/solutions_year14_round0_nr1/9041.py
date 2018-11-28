#include <iostream>
#include <iostream>
#include <vector>
#include <string>
#include <sstream>

using namespace std;

int main()
{
    
    int cases = 0;
    int i1, i2, result,flag = 0;
    vector<vector<int>> matrix1(4,vector<int>(4)), matrix2(4,vector<int>(4));
    vector<int> row1(4);
    cin >> cases;
    int d = cases;
    std::stringstream ss;
    while(cases) {
        --cases;
	flag = 0;
        i1 = i2 = 0;
	result = 0;
        cin >> i1;
        i1 = i1 - 1 ;
        for(int i = 0; i < 4; ++i){
            for(int j = 0; j < 4;++j){
			
                cin >> matrix1[i][j]; 
		if(i == i1)
		    row1[j] = matrix1[i][j]; 
               
            }
        }
            
       /* for(int i = 0; i < 4; ++i) {
            cout << row1[i] <<" ";
        }
        */
        cin >> i2;
        
        for(int i = 0; i < 4; ++i){
            for(int j = 0; j < 4 ;++j){
            	cin >> matrix2[i][j]; 
            }
        }
        i2 = i2 - 1;
       // cout << "i2 " << i2 << endl;
        
        for(int i = 0; i < 4; ++i){
            for(int j = 0 ; j < 4; ++j){
                if(matrix2[i2][i] == row1[j]){
	//	    cout << " matched " << row1[j]<<"\n";
                    ++flag;
                    result = j;
                    if(flag > 1)
                    	break;
                }
            }
        }
        
        if(flag == 1)
            cout << "Case #" <<d - cases<<": "<< row1[result] << endl;
        if(flag == 0)
            cout<< "Case #" <<d - cases<<": " << "Volunteer cheated!\n";
        if(flag > 1)
            cout<< "Case #" <<d - cases<<": " << "Bad magician!\n";
            
      //--cases;      
    }
   
    return 0;
}


