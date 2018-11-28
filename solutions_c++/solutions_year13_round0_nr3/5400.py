#include <iostream>
#include <stdio.h>
#include <string.h>
#include<cmath>
using namespace std;
//int arr={1,4,9,121,484};
int main()
{
    int t,a,b,e,d;cin>>t;
    while(t--)
    {
        cin>>b>>a;
        if(a>=484)d=5;
        else if(a>=121)d=4;
        else if(a>=9)d=3;
        else if(a>=4)d=2;
        else d=1;
        if(b>484)e=5;
        else if(b>121)e=4;
        else if(b>9)e=3;
        else if(b>4)e=2;
        else if(b>1)e=1;
        else e=0;     
        cout<<d-e<<endl;   
        
    }
    return 0;
    
}
