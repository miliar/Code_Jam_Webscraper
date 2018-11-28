#include <iostream>
#include <fstream>
#include <string>
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <iomanip>
#include <math.h>

using namespace std;

int main()
{
    int noOfCases;
    int ans1,ans2;
    string temp;
    int cards1[16];
    int cards2[16];
    int card=0;
    int count=0;

    ofstream ans;
    ans.open ("ansMagic.txt");
    ifstream in;
    in.open("a.txt");

    in>>temp;
    noOfCases=atof(temp.c_str());

    for(int i=0;i<noOfCases;i++)
    {
        in>>temp;
        ans1=atof(temp.c_str());

        for(int j=0;j<16;j++)
        {
            in>>temp;
            cards1[j]=atof(temp.c_str());
        }

        in>>temp;
        ans2=atof(temp.c_str());

        for(int j=0;j<16;j++)
        {
            in>>temp;
            cards2[j]=atof(temp.c_str());
        }

        count=0;
        for(int a=(ans1-1)*4,c=0;c<4;c++,a++)
        {
            for(int b=(ans2-1)*4,d=0;d<4;d++,b++)
            {
                if(cards1[a]==cards2[b])
                {
                    count++;
                    card=cards1[a];
                }
            }
        }
        if(count==1)
        {
            cout<<"Case #"<<i+1<<": "<<card<<endl;
            ans<<"Case #"<<i+1<<": "<<card<<endl;
        }
        else if(count==0)
        {
            cout<<"Case #"<<i+1<<": Volunteer cheated!"<<endl;
            ans<<"Case #"<<i+1<<": Volunteer cheated!"<<endl;
        }
        else
        {
            cout<<"Case #"<<i+1<<": Bad magician!"<<endl;
            ans<<"Case #"<<i+1<<": Bad magician!"<<endl;
        }

    }

    return 0;
}
