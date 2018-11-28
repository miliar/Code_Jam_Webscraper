//qualification A
#include <iostream>
#include <fstream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <cstring>
using namespace std;
//#include <conio.h>
char str[1005];

int s;
int main()
{
    ifstream fin("input.txt");
    ofstream fout("output.txt");
    
    
    int t;
    
    fin>>t;
    
    int ind=1;
    
    while(t--)
    {
          fin>>s;
          fin>>str;     
           long int ans=0;
           long int got=0;
           
           //cout<<s<<" "<<str<<endl;
     
         fout<<"Case #"<<ind<<": ";
         //cout<<"Case #"<<ind<<": ";
         ind++;  
         
            long int n=strlen(str);
            int added;
            int required;
            for(long int i=0;i<n;i++)
            {
               if(str[i]=='0')continue;
               //str[i]!='0'
               
               added=str[i]-'0';
               required=i;
                     if(got>=s)break;
                 
                 if(got>=required&&got<s)got+=added;
                 else if(got<required)
                 {
                      ans+=required-got;
                      got=required;
                      got+=added;
                  }
                     //end of for
                     }
              
              fout<<ans<<endl;
             // cout<<ans<<endl;
              
              //end of while
              }
    
    
    
    fin.close();
    fout.close();
    
    //getch();
    return 0;
}
