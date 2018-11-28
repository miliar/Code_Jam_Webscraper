#include <fstream>
#include <string>
#include <iostream>
#include <queue>
#include <list>
#include <algorithm>
#include <vector>
#include <stdio.h>
#include <deque>

using namespace std;


int main ()
{
    int t;
    double c,f,x; //cost of farm, extra rate, final objective
    
    
    freopen("B-large.txt","r",stdin);   
    freopen("Boutput.txt","w",stdout);
    
    cin>>t;
    
     
    for (int trial=1;trial<=t;++trial)
    {
        cin>>c>>f>>x;
        double currentRate = 2.0;
        double currentTime = 0.0;
        
        //Make a decision: buy a farm or wait until done.
        while (x>c && x/currentRate > (c/currentRate + x/(currentRate+f))) //wait until done if x<c OR if x/currentRate <= c/currentRate + x/(currentRate+f)
        {
           currentTime += c/currentRate;
           currentRate +=f;        
        }
        printf("Case #%d: %.7f \n", trial, (currentTime + x/currentRate));
        //cout<<"Case #"<<trial<<": "<<(currentTime + x/currentRate)<<"\n";
    }
    return 0;
}
