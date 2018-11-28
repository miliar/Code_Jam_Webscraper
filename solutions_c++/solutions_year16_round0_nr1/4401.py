#include<iostream>
#include<stdio.h>
#include<stdlib.h>

#include <fstream>
#include <string>
using namespace std;
int main()
{
    int t,t1=0;


    //if(fgets(line,100,file)!= NULL)
       //t = atoi(line);
       cin>>t;

    while(t--)
    {
        t1++;
        long long N;

        cin>>N;
        if(N==0)
        {
            cout<<"Case #"<<t1<<": INSOMNIA\n";
            continue;
        }
        int h[10]={0};
        int counter = 0;
        int temp,i=0;
        long long n1 = N,res;
        while(counter<10)
        {
            i++;
            N = n1*i;
            res = N;
            while(N>0)
            {
                temp = N%10;
                N=N/10;
                if(h[temp]==0)
                {
                    h[temp]++;
                    counter++;
                }

            }

         }
         cout<<"Case #"<<t1<<": "<<res<<"\n";

    }
}
