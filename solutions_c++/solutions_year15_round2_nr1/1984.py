#include <iostream>
#include <fstream>
#include <math.h>
#define lli long long int
#define f(i,n) for(int i=0;i<n;i++)
using namespace std;

lli rev(lli a)
{
    
    lli opp=0,rem;
    
    while(a>0)
    {
        rem=a%10;
        a=a/10;
        opp= opp*10 + rem;
    }
    
    return opp;
}

int main()
{
    
    int cases,tot;
    
    ifstream fin("/users/aman/desktop/input.txt",ios::in);
    ofstream fout("/users/aman/desktop/output.txt",ios::out);
    
    fin>>cases; tot=cases;
    
    int *a = new int[1000001];
    bool *found = new bool[1000001];
    
    f(i,1000001)
    { a[i]=9000000; found[i]=false; }
    
    a[0]=0; a[1]=1; a[2]=2;
    
    for(int i=3;i<1000001;i++)
    {
        a[i] = a[i-1]+1;
        
        lli opp = rev(i);
        
        if((a[i]+1)<a[opp])
        {  a[opp]=a[i]+1;  found[opp]=true; }
        
        if( found[opp]==true && i%10 !=0)
        {
          a[i]=min(a[i],(a[opp]+1));
            found[i]=true;
         }
    }
    
    while(cases--)
    {
        lli n;
        fin>>n;
        
        lli min = a[n];
        
        fout<<"Case "<<"#"<<tot-cases<<": "<<min<<endl;
        
        
    }
    
    fin.close(); fout.close();
    return 0;
}