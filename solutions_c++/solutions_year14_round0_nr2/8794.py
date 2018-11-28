#include<iostream>
#include<string>
#include<fstream>
#include<iomanip>
#include<sstream>
using namespace std;

int main()
{
    ofstream output("output1.txt");
    int t;
    bool flag;
    long double c, f, x, p, a, b, totalTime, addp=0;
    cin>>t;
    for(int i=0; i<t; i++)
    {
               cin>>c;
               cin>>f;  
               cin>>x;  
                                            
               p=2.00;
               addp = 0;
               flag = true;
               while(flag)
               {
                          a=(c/p)+(x/(p+f));
                          b=x/p;
                          if(a>b)
                                 flag = false;
                          else
                          {
                              addp+=1;
                              p=p+f;  
                          }     
               }
               totalTime = 0;
               if(p!=2.0)
                   totalTime += c/2.000;
               for(int j=0; j<addp-1; j++)
               {
                       totalTime += c/(((j+1)*f)+2);
               }
               totalTime += x/p; 
               output<<"Case #"<<i+1<<": "<<std::setprecision(7)<<totalTime<<endl;
    }
    cin.get();
    return 0;
}
