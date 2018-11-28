#include<cstdio>
#include<iostream>
#include<fstream>
using namespace std;
int t,a,b,d,c,e,chg,has,arr[5],arr2[5],s;
ofstream myfile("output.txt");
ifstream inp("A-small-attempt2.in");

int main()
{
    inp>>t;
    for(a=1;a<=t;a++)
    {
        inp>>b;
        for(c=1;c<=4;c++)
        {
            for(d=0;d<4;d++)
            {
                if(c==b) inp>>arr[d];            
                else inp>>s; 
            }  
        }                
        inp>>e;
        for(c=1;c<=4;c++)
        {
            for(d=0;d<4;d++)
            {
                if(c==e) inp>>arr2[d];            
                else inp>>s; 
            }  
        }
        chg=0;has=0;
        for(c=0;c<4;c++)
        {
            for(d=0;d<4;d++)
            {
                if(arr[c]==arr2[d])
                {
                    chg++;
                    has=arr[c];               
                }
            }            
        }
        if(chg==0) myfile<<"Case #"<<a<<": Volunteer cheated!"<<endl;
        else if(chg==1) myfile<<"Case #"<<a<<": "<<has<<endl;
        else myfile<<"Case #"<<a<<": Bad magician!"<<endl;
    }
    return 0;
}
