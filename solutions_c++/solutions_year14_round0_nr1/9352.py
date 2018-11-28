#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;
int main ()
{
    string line,line1,line2;
    int row,col;
    vector <int> my_vector;
    int x =0;
    int num_test_case,row_num1,row_num2;
    float my_array1[4][4];
    float my_array2[4][4];
    int y =0;
    ifstream pFile ("small.in");
    if (pFile.is_open())
    {
        getline(pFile, line1);
        stringstream ss1(line1);
        ss1 >> num_test_case;
        for(int xx =0; xx < num_test_case; xx++) {
            getline(pFile, line2);
            stringstream ss2(line2);
            ss2 >> row_num1;
            x = 0;
            row=0;
            while(x <= 3)
            {
                getline(pFile, line);
                stringstream ss(line);
                col=0;
                while(ss >> my_array1[row][col])
                {
                    col++;
                }
                row++;
                x++;
            }
            x =0;
            row = 0;
            getline(pFile, line2);
            stringstream ss3(line2);
            ss3 >> row_num2;

            while(x <= 3)
            {
                getline(pFile, line);
                stringstream ss(line);
                col=0;
                while(ss >> my_array2[row][col])
                {
                    col++;
                }
                row++;
                x++;
            }
            for(int i=0;i<4;i++){
                for(int j=0;j<4;j++){
                    if(my_array1[row_num1-1][i] == my_array2[row_num2-1][j])
                        my_vector.push_back(my_array2[row_num2-1][j]);
//                        cout <<my_array1[row_num1-1][i] << " " <<  my_array2[row_num2-1][j] << endl; 
                }
            }
            if(my_vector.size() == 1)
                cout << "Case" << " #"<< y+1 <<": "<< my_vector[0] << endl;
            else if(my_vector.size() > 1) 
                cout << "Case" << " #"<< y+1 <<": "<<"Bad magician!" << endl;
            else if(my_vector.size() == 0)
                cout << "Case" << " #"<< y+1 <<": "<<"Volunteer cheated!" << endl;
            y++;     
//            cout << "rownum1 " << row_num1 << " rowNum2 " << row_num2 << endl;
            my_vector.clear();
        }
        pFile.close();
    }
    else 
        cout << "Unable to open file";

       return 0;

}
