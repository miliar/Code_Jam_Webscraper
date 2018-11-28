#include <iostream>
#include <fstream>
#include <math.h>
#define f(i,n) for(int i=0;i<n;i++)
using namespace std;

int main()
{
    
    int cases,tot;
    
    ifstream fin("/users/aman/desktop/input.txt",ios::in);
    ofstream fout("/users/aman/desktop/output.txt",ios::out);
    
    fin>>cases; tot=cases;
    
    while(cases--)
    {
        int p[1005],d,sum=0,min=1000; fin>>d;
        int a[1001][1001];

        for(int i=0;i<d;i++)
           fin>>p[i];
            
        for(int i=1;i<=1000;i++)
        {
            sum=0;
            
            for(int j=0;j<d;j++)
            {   if(p[j]>i)
                 { a[i][j]= ceil( (float(p[j]-i))/ (float(i)) );   sum=sum+a[i][j]; }
               else
                   a[i][j]=0;   }
            
            if(sum+i<min)
                min = sum+i;
        }
       
        
        
        fout<<"Case "<<"#"<<tot-cases<<": "<<min<<endl;
        
        
    }
    
    fin.close(); fout.close();
    return 0;
}