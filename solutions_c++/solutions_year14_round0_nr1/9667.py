#include <cstdlib>
#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    int cases;
    int* numbers = new int[4];
    int row;
    int found;
    int number;
    int foundNumber;
    
    int dummy;
    
    ifstream fin("A-small-attempt2.in");
        if (!fin) return 0;
        
    ofstream out("results.txt");
    
    fin >> cases;
    
    for (int n = 1; n <= cases; n++)
    {
        found = 0;
        
        fin >> row;
        cout << row << endl;
        
        for (int i = 1; i <= row - 1; i++)
        {
            fin >> dummy;
            cout << dummy << " ";
            fin >> dummy;
            cout << dummy << " ";
            fin >> dummy;
            cout << dummy << " ";
            fin >> dummy;
            cout << dummy << " " << endl;
        }
        
            
        fin >> numbers[0] >> numbers[1] >> numbers[2] >> numbers[3];
        cout << numbers[0] << " " << numbers[1] << " " << numbers[2] << " " << numbers[3] << " " << "*" <<endl;
        
        for (int i = 0; i < 4 - row; i++)
        {
            fin >> dummy;
            cout << dummy << " ";
            fin >> dummy;
            cout << dummy << " ";
            fin >> dummy;
            cout << dummy << " ";
            fin >> dummy;
            cout << dummy << " " << endl;
        }
            
            
        fin >> row;
        cout << row << endl;
        
        for (int i = 0; i < row - 1; i++)
        {
            fin >> dummy;
            cout << dummy << " ";
            fin >> dummy;
            cout << dummy << " ";
            fin >> dummy;
            cout << dummy << " ";
            fin >> dummy;
            cout << dummy << " " << endl;
        }
            
        for (int i = 0; i < 4; i++)
        {
            fin >> number;
            cout << number;
            for (int j = 0; j < 4; j++)
            {
                 if ( number == numbers[j])
                 {
                       found++;
                       foundNumber = number;
                       cout << "(" << numbers[j] << ")";
                 }
                 cout << " ";  
            }
        }
        cout << "*" <<endl;
        
        for (int i = 0; i < 4 - row; i++)
        {
            fin >> dummy;
            cout << dummy << " ";
            fin >> dummy;
            cout << dummy << " ";
            fin >> dummy;
            cout << dummy << " ";
            fin >> dummy;
            cout << dummy << " " << endl;
        }
        cout << endl;
        
        cout << "Found: " << found << " -";    
        cout << "Case #" << n << ": ";
        out << "Case #" << n << ": ";
             if (found ==1) cout << foundNumber << endl;
             if (found ==0) cout << "Volunteer cheated!" << endl;
             if (found > 1) cout << "Bad magician!" << endl; 
             cout << endl << endl;
             
             if (found ==1) out << foundNumber << endl;
             if (found ==0) out << "Volunteer cheated!" << endl;
             if (found > 1) out << "Bad magician!" << endl;
    }
    
    
    system("PAUSE");
    return EXIT_SUCCESS;
}
