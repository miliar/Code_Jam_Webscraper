#include <fstream>
#include<iostream>
using namespace std;
#include<math.h>
#include<string.h>
int main()
{
    int t,z,h,u,v,x,w,n,q=1,g,r,s,o,i,len;
    string str;
    ofstream outpu;
    outpu.open("output.in");
    ifstream inpu;
    inpu.open("A-large (2).in");
    inpu>>t;
    getline(inpu,str);
    while(t--)
    {
        z=h=u=v=x=w=n=s=o=g=0;
        outpu<<"Case #"<<q<<": ";
        getline(inpu,str);
        len=str.size();
        for(i=0;i<len;i++)
        {
            if(str[i]=='Z')
            {
                z++;
            }
            else if(str[i]=='R')
                r++;
            else if(str[i]=='H')
                h++;
            else if(str[i]=='U')
            {
                u++;
            }
            else if(str[i]=='V')
            {
                v++;
            }
            else if(str[i]=='X')
            {
                x++;
            }
            else if(str[i]=='W')
            {
                w++;
            }
            else if(str[i]=='N')
            {
                n++;
            }
            else if(str[i]=='S')
            {
                s++;
            }
            else if(str[i]=='O')
            {
                o++;
            }
            else if(str[i]=='G')
                g++;
            else continue;
        }
            for(i=0;i<z;i++)
                outpu<<"0";
            for(i=0;i<o-z-w-u;i++)
                outpu<<"1";
            for(i=0;i<w;i++)
                outpu<<"2";
            for(i=0;i<h-g;i++)
                outpu<<"3";
            for(i=0;i<u;i++)
                outpu<<"4";
            for(i=0;i<v-s+x;i++)
                    outpu<<"5";
            for(i=0;i<x;i++)
                    outpu<<"6";
            for(i=0;i<s-x;i++)
                    outpu<<"7";
            for(i=0;i<g;i++)
                    outpu<<"8";
            for(i=0;i<(n-(s-x)-(o-z-w-u))/2;i++)
                    outpu<<"9";
            outpu<<"\n";
            q++;
    }
    inpu.close();
    outpu.close();
    return 0;
}
