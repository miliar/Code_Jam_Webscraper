#include<iostream.h>
#include<fstream.h>

using namespace std;

int main()
{
 fstream fil,fout;
 fil.open("input.txt",ios::in);
 fout.open("output.txt",ios::out);
 int cases = 0;
 fil>>cases;
 for(int l =1;l<=cases;l++)
 {
         
         unsigned long long a,b,k;
         fil>>a>>b>>k;
         long long count = 0;
         for(int i=0;i<a;i++)
         {
                 for(int j=0;j<b;j++)
                 {
                         if((i&j)<k)
                         count++;
                 } 
         }
           
    
    fout<<"Case #"<<l<<": "<<count<<endl;
    }  
    cout<<"done"<<endl;
    return 0; 
}
