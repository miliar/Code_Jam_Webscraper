#include<stdio.h>
#include<string.h>
#include<map>
#include <iostream>
#include<fstream>
#include <string>
#include <vector>
#include <iterator>
#include <algorithm>
#include <stdio.h>
#include<math.h>
#include <stdlib.h>
#include <string>
#define gc getchar_unlocked
#define sz 100005
#define MOD 1000000009
#define getcx getchar_unlocked
#define lli long long int
using namespace std;
inline int getint()
{
        int num = 0;
        char c = getchar_unlocked();
        int flag = 0;
        while(!((c>='0' & c<='9') || c == '-'))
            c=getchar_unlocked();
        if(c == '-')
        {
            flag = 1;
            c=getchar_unlocked();
        }
        while(c>='0' && c<='9')
        {
            num = (num<<1)+(num<<3)+c-'0';
            c=getchar_unlocked();
        }
        if(flag==0)
            return num;
        else
            return -1*num;
}

void inc(int p[], int i, int Smax)
{
    int j=i;
    while(j<Smax+1)
    {
        p[j]++;
        j++;
    }

}

int main()
{
    ifstream myfile ("/Users/Ashish/Dropbox/April_15/inp.txt");
    ofstream outfile("/Users/Ashish/Dropbox/April_15/out.txt");
    if (myfile.is_open())
    {
            int t;
            myfile>>t;
            for(int l=1; l<=t; l++)
            {
                int Smax;
                string s;
                myfile>>Smax;
                myfile>>s;
                int p[Smax+1];
                p[0] = s[0]-48;
                int diff = 0,ctp = 0;
                for(int i=1; i<(Smax+1); i++)
                        p[i] = p[i-1] + (s[i]-48);
        //        for(int i=0; i<(Smax+1); i++)
        //            outfile<<p[i]<<" ";
        //            outfile<<endl;
                for(int i=0; i<(Smax+1); i++)
                        {
                            if(i==p[i] && p[i]==0)
                            {
                                diff = 1;
                                ctp += diff;
                                inc(p,i,Smax);
                                //outfile<<"Entered"<<endl;
                            }
                            else if(i>p[i-1] && (i-1)>=0)
                            {
                                diff = i-p[i-1];
                                //outfile<<i<<endl;
                                ctp += diff;
                                inc(p,i-1,Smax);
                                //outfile<<"Entered2"<<endl;
                            }
                        }
                    outfile<<"Case #"<<l<<": "<<ctp<<endl;
        //        for(int i=0; i<(Smax+1); i++)
        //            outfile<<p[i]<<" ";
        //            outfile<<endl;
        //            outfile<<ctp<<endl;
          }
    }
    myfile.close();
    outfile.close();
}
