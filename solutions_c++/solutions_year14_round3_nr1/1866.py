        #include <fstream>
        #include <iostream>
        #include <string>
        #include <stdio.h>
        #include <math.h>
        #include <limits>
        
        
        using namespace std;
        
        long long gcd(long long a, long long b)
{
    a = a % b;
    if (a == 0)
    {
        return b;
        
    }
    if(b ==0)
    return a;
    else
    return gcd(a, b-a);
}
        
        int main()
        {
            ofstream fout ("2014gcj1out.txt");
            ifstream fin ("2014gcj1in.txt");
            
            
            
            int t;
            
            long long a, b;
            char c;
            long long aux;
            long long aux2;
            
            
           
            fin >> t;
            
            
            
            for(int i=0; i<t; i++)
            {
            
            fin >> a;
            
            fin >> c;
            fin >> b;
            
           
            
            aux = gcd(a,b);
            
            a = a/aux;
            b = b/aux;
            
         
            
            aux =0;
            
            aux2 = b;
            
            for(int j=1; j<50; j++)
            {
            if(aux2 == 1)
            break;
            else
            {
            if(aux2%2 == 1)
            {
            aux = 1;
            break;
            }
            else
            aux2 = aux2/2;
            }
            }
            
            if(aux == 1)
            fout << "Case #" << i+1 << ": impossible" << endl;
            else
            {
            
            long long aux3 = a;
            int k=0;
            for(; k<50; k++)
            {
            aux3 = aux3*2;
            if(aux3 >= b)
            break; 
            }
            
            
            
            fout << "Case #" << i+1 << ": " << k+1 << endl;
            }
            
            
            }
            
            return 0;
              
        }
        
        
