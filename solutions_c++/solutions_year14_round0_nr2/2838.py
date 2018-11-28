#include <iostream>
#include <stdlib.h>
#include <vector>
#include <algorithm>
#include <map>
#include <math.h>
#include <stdio.h>
#include <string.h>
#include <limits.h>
#include <fstream>

using namespace std;
int fastread()
{
    int input;
    char c=0;
    while (c<33) c=getchar();
    input=0;
    while (c>33)
    {
        input=input*10+c-'0';
        c=getchar();
    }
    return input;
}

int main()
{
    int i,j,k,m,n,s,t;
    double c,f,x,cookies=0;
    double time=0,rate, time1, time2;
    ifstream myfile;
    myfile.open("/Users/jigyayadav/Downloads/B-large.in.txt");
    ofstream outfile;
    outfile.open("/Users/jigyayadav/Downloads/outFileLargeB.txt");
    myfile>>t;
    for(s=1;s<=t;s++)
    {
        cookies=0;
        time=0;
        rate=2;
        myfile>>c>>f>>x;
        while(cookies<x)
        {
            if((x-cookies)<=c)
            {
                time+=(x-cookies)/rate;
                cookies+=(x-cookies);
            }
            else
            {
                time+=c/rate;
                cookies+=c;
                time1=(x-cookies)/rate;
                time2=x/(rate+f);
                if(time1<time2)
                {
                    time+=time1;
                    break;
                }
                else
                {
                    rate+=f;
                    cookies=0;
                }
            }
        }
        outfile.precision(8);
        outfile.setf(ios::fixed, ios::floatfield );
        outfile<<"Case #"<<s<<": "<<time<<endl;
    }
    myfile.close();
    outfile.close();
    return 0;
}