#include <iostream>
#include <cstdio>
#include <fstream>
#include <algorithm>
#include <cstring>
#include <string>

using namespace std;

int main()
{
    int t,j,d,count;
    ofstream outfile("output.in");
    ifstream infile("B-small-attempt3.in");

    infile>>t;
    for(int i=1;i<=t;i++)
    {
        count=0;
        infile>>d;
        int p[24]={0};
        for(j=0;j<d;j++)
        {
            infile>>p[j];
        }
        sort(p,p+24);
        reverse(p,p+24);
        if(p[0]==9 && p[1]<=3)
            {
                p[0]=3;
                count+=2;
            }
        else if(p[0]==9 && p[1]==9 && p[2]<=3)
        {
            p[0]=3;
            p[1]=3;
            count+=4;
        }
        else if(p[0]==9 && p[1]>=7 && p[1]<=9 && p[2]==6)
        {
            p[0]=6;
            p[1]=6;
            count+=2;
        }
        else if(p[0]==9 && p[1]>=7 && p[1]<=9 && p[2]<=5 && p[2]>=4)
        {
            p[0]=5;
            p[1]=5;
            count+=2;
        }
        else if(p[0]==9 && p[1]<=8 && p[1]>=7 && p[2]<=3)
        {
            p[0]=4;
            p[1]=3;
            count+=3;
        }
        else if(p[0]==9 && p[1]<=6 && p[1]>=5 && p[2]<=3)
        {
            p[0]=3;
            p[1]=3;
            count+=3;
        }
        else if(p[0]==9 && p[1]>=6 &&p[1]<=9 && p[2]>=6 &&p[2]<=9 && p[3]<=5)
        {
            p[0]=5;
            p[1]=5;
            p[2]=5;
            count+=3;
        }
        else if(p[0]==8 && p[1]>=5 && p[1]<=8 && p[2]<=4)
        {
            p[0]=4;
            p[1]=4;
            count+=2;
        }
        else if(p[0]==8 && p[1]>=6 && p[1]<=8 && p[2]>=5 && p[2]<=8 && p[3]<=4)
        {
            p[0]=4;
            p[1]=4;
            p[2]=4;
            count+=3;
        }
        else if(p[0]==7 && p[1]>=5 && p[1]<=7 && p[2]<=4)
        {
            p[0]=4;
            p[1]=4;
            count+=2;
        }
        else if(p[0]==6 && p[1]>=4 && p[1]<=6 && p[2]<=3)
        {
            p[0]=3;
            p[1]=3;
            count+=2;
        }

        if(p[0]-p[1]>1)
        {
            if(p[0]%2==1)
                p[0]=(p[0]/2)+1;
            else
                p[0]/=2;
            count++;
            if(p[0]<p[1])
            swap(p[0],p[1]);
        }
        count+=p[0];


        outfile<<"Case #"<<i<<": "<<count<<endl;
    }
    return 0;

}
