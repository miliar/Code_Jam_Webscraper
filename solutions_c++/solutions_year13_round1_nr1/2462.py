#include<iostream>
#include<fstream>
#include <cmath>
using namespace std;

int main()
{
       ifstream fin;
       ofstream out("out.out");
       fin.open("A-small-attempt0.in");
       
       
       int n,t;
       double r;
       fin>>n;                // test cases
       
       int ans;
       bool end = false;
       
       for(int i=0;i<n;i++)
       {
                  fin>>r;
                  fin>>t;
                  end = false;
                  r= r+1;
                  ans =0;
                  
                  while(!end)
                  {
                             if(t>=(pow(r,2)-pow(r-1,2)))
                             {                         ans++;
                                                       t = t -( pow(r,2) - pow(r-1,2));
                             }
                             else
                                 end = true;
                                 
                                 r+=2;
                  }
                  
                  out<<"Case #"<<i+1<<": "<<ans<<endl;
       }
       

    fin.close();
    system("pause");
    return 0;
}
