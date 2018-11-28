#include <iostream>
#include <string.h>
#include <string>
#include <math.h>
#include <stdio.h>
#include <fstream>
#include <iomanip>
#include <algorithm>
#include <list>
#include <vector>
#include <deque>
#include <functional>
using namespace std;

int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("o.out","w",stdout);
    string map[5][5];
    map[1][1]="1";
    map[1][2]="2";
    map[1][3]="3";
    map[1][4]="4";

    map[2][1]="2";
    map[2][2]="-1";
    map[2][3]="4";
    map[2][4]="-3";

    map[3][1]="3";
    map[3][2]="-4";
    map[3][3]="-1";
    map[3][4]="2";

    map[4][1]="4";
    map[4][2]="3";
    map[4][3]="-2";
    map[4][4]="-1";
    int a,b,c,d,t,l,x;
    bool neg;
    cin>>t;
    int ch=1,chk;
    string str;
    for (a=0;a<t;a++)
    {
        cout<<"Case #"<<a+1<<": ";
        cin>>l>>x>>str;
        if (l*x<3){cout<<"NO"<<endl;continue;}
        replace( str.begin(), str.end(), 'i', '2');
        replace( str.begin(), str.end(), 'j', '3');
        replace( str.begin(), str.end(), 'k', '4');
        ch=1;
        chk=2;
        neg=false;
        //cout<<"str="<<str<<endl;
        for(b=0;b<x;b++)
        {
            for (c=0;c<l;c++)
            {   //cout<<" ch="<<ch<<" str[c]="<<str[c]<<" c="<<c<<"map[ch][str[c]]"<<map[ch][str[c]-48]<<endl;
                if(map[ch][str[c]-48][0]=='-'){neg=!neg;ch=map[ch][str[c]-48][1]-48;}
                else
                ch=map[ch][str[c]-48][0]-48;
                if (ch==chk)
                {ch=1;chk++;}

            }
        }

        if (chk==5&&ch==1&&neg==false)
        cout<<"YES"<<endl;
        else
        cout<<"NO"<<endl;
    }
    return 0;
}
