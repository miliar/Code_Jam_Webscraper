#include <iostream>
#include <vector>
#include <algorithm>
#include <sstream>
#include <stdio.h>
#include <set>
#include <math.h>
#include <map>
#include <stack>
#include <fstream>
using namespace std;

int main()
{int ts;
ifstream fin;
fin.open("inp.txt");
ofstream fout;
fout.open("out.txt");
fin>>ts;
int r,t;
int s=1;
while(ts--){
        fin>>r>>t;
        int ans=0;
        int x=r;
        do{
               t=t-((x+1)*(x+1)-(x*x)) ;
               x=x+2; 
               if(t>=0)
               ans++;  
                   }while(t>0);    
                   fout<<"Case #"<<s<<":"<<" "<<ans<<endl;
            s++;
            }
    
   //  system("pause"); 
    return 0;

}


