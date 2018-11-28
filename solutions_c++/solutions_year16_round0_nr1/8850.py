#include<bits/stdc++.h>
using namespace std;

int t,n,m;

int main()
{
ios::sync_with_stdio(false);

ifstream file;
file.open("A-large.in");

ofstream gadha;
gadha.open("rascal.txt");

file>>t;

int j=1;
    while(file>>n)
    {
    
    int a[10]={0},count=0;
    for(int i=1;count<10&&count>=0;i++)
    {
    count=0;
    
        if(2*n==3*n)
        count=-1;
        else
        {
        m=i*n;
        
            while(m>0)
            {
            int x=m%10;
            m/=10;
            a[x]++;
            }
          m=i*n;  
        }
        
       for(int x=0;x<10;x++)
       {
        if(a[x]>0)
        count++;
       }
       
     }
     
     gadha<<"Case #"<<j<<": ";
     
     if(count!=10)
     gadha<<"INSOMNIA"<<endl;
     else
     gadha<<m<<endl;
     
     j++;
    }
    
  file.close();
  gadha.close();
return 0;
}
