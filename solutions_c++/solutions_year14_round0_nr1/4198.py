#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>  

using namespace std;

int main(int argc, char* argv[])
{
    ifstream myfile ("A-small-attempt0.in");
    ofstream outputfile ("output.txt");
    
    if (myfile.is_open())
    {
		int T_numTests, t1, t2, row1, row2;
        int cards1[4][4], cards2[4][4];
        myfile >> T_numTests; 

		//repeat per testcase 
        for (int testcase = 0; testcase < T_numTests; testcase++){
            //First read row indices and card matrices
			myfile >> t1;
            row1 = t1-1; //correcting human index 

            for(int i = 0; i < 4; i++){
                for (int j = 0; j < 4; j++){
                    myfile >> cards1[i][j];
                }
            }
           
            myfile >> t2;
            row2 = t2-1; 

            for(int i = 0; i < 4; i++){
                for (int j = 0; j < 4; j++){
                    myfile >> cards2[i][j];
                }
            }
			//Select rows according to given answers
            vector<int> answer1(4), answer2(4);

            for(int i = 0; i < 4; i++){
                answer1[i] = cards1[row1][i];
                answer2[i] = cards2[row2][i];
            }
            sort (answer1.begin(),answer1.end());    
            sort (answer2.begin(),answer2.end());  
			
			//Sort rows and calculate intersection of both vectors, the answer depends on size of the intersection
            vector<int> intersection(8);                      
            vector<int>::iterator it = set_intersection (answer1.begin(),answer1.end(),answer2.begin(),answer2.end(),intersection.begin());
            intersection.resize(it-intersection.begin());                      

            int possibility = intersection.size();
            switch( possibility ){ 
            case 0: 
                outputfile << "Case #" << testcase+1 << ": " << "Volunteer cheated!" << endl;
                cout << "Case #" << testcase+1 << ": " << "Volunteer cheated!" << endl; 
                break; 
            case 1: 
                outputfile << "Case #" << testcase+1 << ": " << intersection.at(0) << endl; 
                cout << "Case #" << testcase+1 << ": " << intersection.at(0) << endl; 
                break; 
            default: 
                outputfile << "Case #" << testcase+1 << ": " << "Bad magician!" << endl; 
                cout << "Case #" << testcase+1 << ": " << "Bad magician!" << endl; 
                break; 
            }

        }
        myfile.close();
        outputfile.close();
    }
    return 0;
}
