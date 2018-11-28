#include<iostream>
#include<fstream>

using namespace std;

int main()
{
    ifstream alpha("A-small-attempt0.in");
    ofstream beta("output.txt");
    int N,k,m;
    alpha>>N;
    unsigned long long x;
    unsigned long long y;
    
    for(k=0;k<N;k++)
    {
                    alpha>>x>>y;
                    m=0;
                    
                    while(y>=(x+1)*(x+1)-(x*x))
                    {
                                              m++;
                                              y = y-((x+1)*(x+1)-(x*x));
                                              x = x+2;
                                              }
                    beta<<"Case #"<<k+1<<": "<<m<<endl;
                    }
                    
    return 0;
    }
