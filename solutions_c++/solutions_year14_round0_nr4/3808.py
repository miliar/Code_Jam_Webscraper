        #include <fstream>
        #include <iostream>
        #include <string>
        #include <stdio.h>
        
        
        using namespace std;
        
        int main()
        {
            ofstream fout ("2014gcj4out.txt");
            ifstream fin ("2014gcj4in.txt");
            
            int t;
            fin >> t;
            int n;
            double aux;
            int res;
            int res2;
            
            
            for(int i=0; i<t; i++)
            {
            
            res = 0;
            res2= 0;
            fin >> n;
            
            double one[n];
            double two[n];
            double three[n];
            double four[n];
            double aux;
            
            for(int j=0; j<n; j++)
            fin >> one[j];
            
            
            for(int j=0; j<n; j++)
            fin >> two[j];
            
            for(int j=0; j<n; j++)
            for(int k=j+1; k<n; k++)
            if( one[j] > one[k])
            {
            aux = one[j];
            one[j] = one[k];
            one[k] = aux;
            }
            
            for(int j=0; j<n; j++)
            for(int k=j+1; k<n; k++)
            if( two[j] > two[k])
            {
            aux = two[j];
            two[j] = two[k];
            two[k] = aux;
            }
            
            for(int j=0; j<n; j++)
            {
            three[j] = one[j];
            four[j] = two[j];
            }
            
            for(int j=0; j<n; j++)
            {
            if(one[j] > two[0])
            {
            res++;
            for(int k=0; k<n-j-1; k++)
            two[k] = two[k+1];
                  
            }
            }
            
            for(int j=0; j<n; j++)
            {
            aux = 0;
            for(int k=0; k<n-j; k++)
            if(four[k] > three[j])
            {
            aux = 1;
            for(int l=k; l<n-j-1; l++)
            four[l] = four[l+1];
            break;
            }
            
            if(aux == 0)
            {
            res2 =  n-j;
            break;
            }
            }
            
                        
            
            
            fout << "Case #" << i+1 << ": " << res << " " << res2 << endl;
                    
          
                     
            }
             
            
            
            
            
            return 0;
            
        }
        
        

