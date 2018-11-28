#include<iostream>
#include<sstream>
#include<fstream>


using namespace std;


void add(int a[100], int b[100], int c[100])
{
    for (int i=0; i<100; i++)c[i] = a[i] + b[i];
        
    for (int i=0; i<100-1; i++) 
    {
        c[i+1] += c[i] / 10;
        c[i] %= 10;
    }
    
}



int main()
{
    
    
    int a[100] = {0}, b[100] = {0} ,c[100] = {0};

    long long T,N,Nsize,counter = 0;
    ifstream fin("A.in");
    ofstream fout("O.txt");
    
    fin >> T;
    
    while(counter != T)
    {
            
        fin >> N;
        if(N == 0)
        {
             fout << "Case #" << counter+1 <<": INSOMNIA" << endl; 
             counter++;
             continue;
        }
        for(int i = 0;i < 100;i++)
        {
                a[i] = 0;
                b[i] = 0;
                c[i] = 0;
        }     
         
        int poision[10] = {0};
        int i = 0;
        
        while(N != 0)
        {
           a[i++] = N % 10;
           N /= 10;           
        }
        bool ch = false;
    
        while(!ch)
        {
            for(int i = 0; i < 100; i++)
            {
                    b[i] = c[i];
                    c[i] = 0;
            }
            
            add(a,b,c);

            int j = 100 -1;
             
            while (c[j] == 0) j--;
            while (j >= 0)poision[c[j--]] = 1;
            
            int pcounter = 0;
            for(int i = 0;i < 10;i++)
            {
              if(poision[i] == 1)pcounter++;
              
            }   
                 
            if(pcounter == 10)ch = true;
            
   
            
        }
        fout << "Case #"<< counter+1 <<": ";
        
        int k = 100 -1;
        while (c[k] == 0) k--;
        while (k >= 0) fout << c[k--];
        fout << endl;
                       
        counter++;
       
       
       
    }
    

    
    system("pause");
    return 0;
}
