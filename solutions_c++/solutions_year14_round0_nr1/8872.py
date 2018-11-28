#include <iostream>
#include <vector>
#include <fstream>
using namespace std;

vector <int> det_Win ( int ans_One , int ans_Two , vector<vector<int> > arr_One, 
              vector<vector<int> > arr_Two)
{
    vector<int> firstChoice = arr_One.at(ans_One-1);
    vector<int> secChoice = arr_Two.at(ans_Two-1);
    vector<int> magic_num;
    
    for ( int i = 0; i < 4; ++i)
    {
        for (int j = 0; j < 4; ++j)
        {
            if (firstChoice.at(i) == secChoice.at(j))
                magic_num.push_back(firstChoice.at(i));
        }
    }
    return magic_num;
}
                
int main ()
{
    int num_Cases;
    
    ifstream read("A-small-attempt0.in");
    if (!read.is_open())
    {
        cout << "Error opening file" << endl;
        exit(0);
    }
    
    ofstream write("codeout_1.txt");
    if (!write.is_open())
    {
        cout << "Error opening file" << endl;
        exit(0);
    }
    
    read >> num_Cases;
    
    for (int i = 0; i < num_Cases; ++i)
    {
        int ans_One , ans_Two;
        vector<int> magicNums;
        vector<vector<int> > arrange_One , arrange_Two;
        
        read >> ans_One;
       
        for ( int j = 0; j < 4; ++j)
        {
            vector<int> line;
            for (int k = 0; k < 4; ++k)
            {
                int curNum;
                read >> curNum;
                line.push_back(curNum);
            }
            arrange_One.push_back(line);
        }
        
        read >> ans_Two;
        
        for ( int l = 0; l < 4; ++l)
        {
            vector<int> line;
            for (int m = 0; m < 4; ++m)
            {
                int curNum;
                read >> curNum;
                line.push_back(curNum);
            }
            arrange_Two.push_back(line);
        }
       
        magicNums = det_Win(ans_One , ans_Two, arrange_One , arrange_Two);
        
        write << "Case #" << i + 1 << ": ";
        
        if (magicNums.size() == 1)
            write << magicNums.at(0) << endl;
            
        else if (magicNums.size() == 0)
            write << "Volunteer cheated!" << endl;
            
        else 
            write << "Bad magician!" << endl;
    }
    read.close();
    write.close(); 
    return 0;
}
            
        
        
        
        
        
        
                
        
    
    
