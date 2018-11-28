#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <stack>
#include <algorithm>
#include<fstream>
#include<string>
#include<string.h>
#include<stdlib.h>
#include<math.h>
using namespace std;

#define f(i,n) for(i=0;i<n;i++)
#define fback(i,n) for(i=n-1;i>0;i--)
#define f1(i,n) for(i=1;i<n;i++)
#define takeinp(inp,fptr) fptr>>inp
#define ll long long

#define takeinp(inp,fptr) fptr>>inp
int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int test,t,i,j,n,id,k,r,c,d,v;//a,b;
    ifstream myinpfile;
    ofstream myoutfile;
    myinpfile.open("i12.in");
    myoutfile.open("myout.txt");
    takeinp(test,myinpfile);
    f(t,test)
    {
        int temp=0,minscore=0;
        takeinp(c,myinpfile);
        takeinp(d,myinpfile);
        takeinp(v,myinpfile);
        int *den=new int [d];
        f(j,d)
        {
            takeinp(den[j],myinpfile);
        }
        sort(den,den+d);
        j=0;
        int minreq=0,sum=0,current=1;
        while(current<=v)
        {
            if(j<d)
            {
                if(current<den[j])
                {
                    minreq++;
                    sum+=current;
                    //current=(c+1)*current;
                    current=sum*c+1;
                }
                else if(current>=den[j])
                {
                    sum+=den[j];
                    current=sum*c+1;
                    j++;
                }
//                else
//                {
//                    j++;
//                    sum+=current;
//                    //current=(c+1)*current;
//                    current=sum*c+1;
//
//                }
            }
            else
            {
                    minreq++;
                    sum+=current;
                    //current=(c+1)*current;
                    current=sum*c+1;

            }

        }


              myoutfile<<"Case #"<<t+1<<": "<<minreq<<endl;
    }
    return 0;
}
