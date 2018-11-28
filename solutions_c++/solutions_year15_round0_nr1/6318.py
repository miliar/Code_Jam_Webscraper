#include<iostream>
#include<stdlib.h>
using namespace std;
int main()
{
    int t;
    cin>>t;
    int smax,countpr,countreq,input2int[1020];
    string inputcase;
    for(int i=0;i<t;i++)
    {   
        cin>>smax;
        cin>>inputcase; 
        countpr = 0;
        countreq = 0;
        for(int j=0;j<=smax;j++)
        {
                       input2int[j]=inputcase[j]-'0';
                       if(countpr<j )
                       {
                        countreq= countreq+j-countpr;
                        countpr=countpr+j-countpr+input2int[j];
                       }
                       else 
                       countpr= countpr +input2int[j];
        }
        
    cout<<"Case #"<<i+1<<": "<<countreq++<<endl;
}
}
