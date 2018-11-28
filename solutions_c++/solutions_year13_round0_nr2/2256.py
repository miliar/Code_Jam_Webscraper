        #include <fstream>
        #include <iostream>
        #include <string>
        #include <stdio.h>
        #include <math.h>
        
        
        using namespace std;
        
        int main()
        {
            ofstream fout ("2011gcj2out.txt");
            ifstream fin ("2011gcj2in.txt");
            
            int t;
            fin >> t;
            int n, m;
            
                      
                      
            for(int i=0; i<t; i++)
            {
                    
            fin >> n;
            fin >> m;
            
            int res=1;
            
            int table[n][m];
            
            for(int j=0; j<n; j++)
            for(int l=0; l<m; l++)
            fin >> table[j][l];
            
            for(int j=0; j<n; j++)
            for(int j1=j+1; j1<n; j1++)
            for(int l=0; l<m; l++)
            for(int l1=l+1; l1<m; l1++)
            {
            
            if((table[j][l]-table[j][l1])*(table[j][l]-table[j1][l])*(table[j1][l1]-table[j][l1])*(table[j1][l1]-table[j1][l]) != 0)
            res = 0;
            else
            {
            
            if(table[j][l]-table[j][l1] == 0 && table[j1][l1]-table[j1][l] != 0 && ((table[j][l]-table[j1][l])>0 || (table[j][l1]-table[j1][l1]) > 0))
            res = 0;
            
            if(table[j][l]-table[j1][l] == 0 && table[j1][l1]-table[j][l1] != 0 &&((table[j][l]-table[j][l1])>0||(table[j1][l]-table[j1][l1]) > 0))
            res = 0;
            
            
            if(table[j1][l1]-table[j][l1] == 0 && table[j][l]-table[j1][l] != 0 && ((table[j1][l1]-table[j1][l])>0||(table[j][l1]-table[j][l]) > 0))
            res = 0;
            
            
            if(table[j1][l1]-table[j1][l] == 0 && table[j][l]-table[j][l1] != 0 &&((table[j1][l1]-table[j][l1])>0||(table[j1][l]-table[j][l]) > 0))
            res = 0;
            
                 
                        
            }
            
            
            }
                    
            
            
            if(res==1)
            fout << "Case #" << i+1 << ": YES" << endl;
            else
            fout << "Case #" << i+1 << ": NO" << endl;
           
            }            
                                   
            
            return 0;
            
        }
        
        
