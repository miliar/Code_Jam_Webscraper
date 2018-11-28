#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <math.h>
#include <fstream>
#include <string>
#include <sstream>
using namespace std;
void swapp(int *a,int *b)
{
    int n=*a;
    *a=*b;
    *b=n;
}
int main()
{
    fstream in;
    int t;
    in.open("//Volumes//TRANSCEND//programming //training//training//in.txt");
    int smax,*au,i,stand,fr,**sor;
    string str;
    in>>t;
    for(int time=1;time<=t;time++)
    {
        in>>smax>>str;
        au=new int[smax+1];
        sor=new int*[2];
        for(i=0;i<2;i++) sor[i]=new int[smax+1];
        for(i=0;i<smax+1;i++)
            au[i]=str[i]-48;
        fr=0;
        stand=au[0];
        for(i=1;i<=smax;i++)
        {
            if(stand>=i || au[i]==0) stand+=au[i];
            else {
                
                fr=i-stand+fr;
                stand=i;
                stand+=au[i];
            }
    
        }
        cout<<"Case #"<<time<<": "<<fr<<endl;
        
    }
}
