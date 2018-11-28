        #include <fstream>
        #include <iostream>
        #include <string>
        #include <stdio.h>
        #include <math.h>
        
        
        using namespace std;
        
        int main()
        {
            ofstream fout ("2014gcj2out.txt");
            ifstream fin ("2014gcj2in.txt");
            fout.precision(15);
            
            int t;
            fin >> t;
            double c, f, x, r;
            double res;
            double n;
            int m;
            
                      
                      
            for(int i=0; i<t; i++)
            {
            
            res = 0;
            r=2;
                   
            fin >> c;
            fin >> f;
            fin >> x;
            
            
            n = x-c;
            n = n/c;
            n = n*f;
            n = n-2;
            n = n/f+1;
            
            m = (int)n;
            
            for(int j=0; j<m ; j++)
            {
            res = res + c/(2+j*f);
            
            }
            
            res = res + x/(2+m*f);
            
            
            
            if(x > c)
            fout << "Case #" << i+1 << ": " << res << endl;
            else
            {
            res = x/2;
            fout << "Case #" << i+1 << ": " << res << endl; 
            }
            }            
                                   
            
            return 0;
            
        }
        
        
