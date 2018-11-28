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

bool wayToSort(int i, int j) { return i > j; }
int main ()
{
    
    freopen("A-small.txt","r",stdin);   
    freopen("Aout.txt","w",stdout);
        
    int T, n, x;
    int sizes[10000];

    cin>>T;
    for (int trial=1;trial<=T;++trial)
    {
        cin>>n>>x;
        for (int j=0;j<n;++j)
        {
            cin>>sizes[j];        
        }
        
        sort (sizes, sizes+n, wayToSort);
        int start = 0;
        int end = n-1;

       
        int answer = 0;
        
        while (start<end)
        {
              
              if (sizes[start]+sizes[end]<=x)
              {
                 start++;
                 end--;
                 answer++;                               
              }
              else
              {
                  answer++;
                  start++;    
              }
        }
        
        if (start==end)
           answer++;
        
        cout<<"Case #"<<trial<<": "<<answer<<"\n";
    }
    
    return 0;
}
