#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <fstream>

using namespace std;

int main()
{
    ifstream in("input2.txt");
    ofstream out("output2.txt");
    int po=0;
    in>>po;
    for(int co=0;co<po;co++)
    {
        int x,y;
        in>>x>>y;
        int ansmap[x][y];
        int map[x][y];
        for(int xx=0;xx<x;xx++)
        {
            for(int yy=0;yy<y;yy++)
            {
                in>>ansmap[xx][yy];
                map[xx][yy]=105;
            }
        }
        
        for(int xx=0;xx<x;xx++)
        {
            int maxi=0;
            for(int yy=0;yy<y;yy++)
            {
                if(ansmap[xx][yy]>maxi) maxi=ansmap[xx][yy];
            }
            for(int yy=0;yy<y;yy++)
            {
                if(map[xx][yy]>maxi) map[xx][yy]=maxi;
            }            
        }
        for(int yy=0;yy<y;yy++)
        {
            int maxi=0;
            for(int xx=0;xx<x;xx++)
            {
                if(ansmap[xx][yy]>maxi) maxi=ansmap[xx][yy];
            }
            for(int xx=0;xx<x;xx++)
            {
                if(map[xx][yy]>maxi) map[xx][yy]=maxi;
            }            
        }
        int flag=0;
        for(int xx=0;xx<x;xx++)
        {
            for(int yy=0;yy<y;yy++)
            {
                if(ansmap[xx][yy]!=map[xx][yy])
                {
                    flag=1;
                    break;
                }
            }
            if(flag==1) break;
        }

        if(flag==0) out<<"Case #"<<co+1<<": YES"<<endl;
        else if(flag==1) out<<"Case #"<<co+1<<": NO"<<endl;
    }
    return 0;
}
        
        
    
