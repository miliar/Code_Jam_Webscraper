        #include <fstream>
        #include <iostream>
        #include <string>
        #include <stdio.h>
        #include <math.h>
        #include <limits>
        
        
        using namespace std;
        
        int main()
        {
            ofstream fout ("2014gcj1out.txt");
            ifstream fin ("2014gcj1in.txt");
            
            
            
            int t;
            int r1;
            int r2;
            int matrix[4][4];
            int matrixx[4][4];
            int aux;
            int res;
          
            fin >> t;
            
            for(int i=0; i<t; i++)
            {
                 
            aux =0;  
            fin >> r1;
            
            for(int j=0; j<4; j++)
            for(int k=0; k<4; k++)
            fin >> matrix[j][k];
            
         
            
            fin >> r2;
            
            for(int j=0; j<4; j++)
            for(int k=0; k<4; k++)
            fin >> matrixx[j][k];
            
            for(int j=0; j<4; j++)
            for(int k=0; k<4; k++)
            if(matrix[r1-1][j] == matrixx[r2-1][k])
            {
            aux++;
            res = matrix[r1-1][j];
            }
                                
            if(aux == 0)            
            fout << "Case #" << i+1 << ": " << "Volunteer cheated!" << endl;
            else
            {
            if(aux == 1)
            fout << "Case #" << i+1 << ": " << res << endl;
            else
            fout << "Case #" << i+1 << ": " << "Bad magician!" << endl;
            }
            
            }
            return 0;
            
        }
        
        
