#include <iostream>
#include <fstream>
using namespace std;
int main()
{
    
    int cases,tot,a[1005];
    
    ifstream fin("/users/aman/desktop/input.txt",ios::in);
    ofstream fout("/users/aman/desktop/output.txt",ios::out);
    
    fin>>cases; tot=cases;
    
    while(cases--)
    {
        char ch; int n,friends=0;
        fin>>n;
        fin.ignore();
        
        fin>>ch;
        a[0] = (int)(ch - '0');
        
        for(int i=1;i<=n;i++)
        { fin>>ch;
            a[i]=(int)(ch - '0');  a[i]+=a[i-1]; }
        
        fin.ignore();
        
        /* for(int i=0;i<=n;i++)
         cout<<a[i]<<" "; */
        
        
        
        for(int i=1;i<=n;i++)
        {
            if(a[i-1]+friends<i)
                friends += i - (friends + a[i-1]);
        }
        
        
        fout<<"Case "<<"#"<<tot-cases<<": "<<friends<<endl;
    }
    
    fin.close(); fout.close();
    return 0;
}