/*

*/

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

int bestAns;
int answer;
int motes[101];
int t,n,a;

void f (int num)
{
     
     int temp = a;
     
     if (num==n)
     {
                if (answer<bestAns)
                   bestAns = answer;
              return;  
     }
     
     if (motes[num]<a)
     {
          a += motes[num]; 
          if (a> 1000001)
             a = 1000001;
          f (num+1);
  
     }
     else
     {
         //Delete this mote and move on?
         answer++;
         f(num+1);
         answer--;
         
         //Add a smaller mote and move on? 
         
         if (a>1)
         {
             int counter = 0;
             while (a<=motes[num])
             {     
                   counter++;
                   answer++;
                   a += a - 1;
             }
             a += motes[num];
             if (a> 1000001)
              a = 1000001;  
             f(num+1);
             
             answer = answer - counter;
         }
     }
                
     a = temp;
}

int main ()
{
    
    freopen("A-large.in","r",stdin);   
    freopen("A-l.out","w",stdout);
    
    scanf ("%d\n", &t);
    
    for (int trial=1;trial<=t;++trial)
    {
        scanf ("%d %d\n", &a, &n);
        for (int i=0;i<n-1;++i)
        {
            scanf("%d ",&motes[i]);
        }
        scanf ("%d\n",&motes[n-1]);
        
        sort (motes, motes+n);
        
        
        //Loop over all motes in sorted order
        bestAns = 2000000000;
        answer = 0;
        f(0);
        
        cout<<"Case #"<<trial<<": "<<bestAns<<"\n";
    }
    return 0;
}
