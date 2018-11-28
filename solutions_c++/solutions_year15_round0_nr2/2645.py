#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <stack>
#include <algorithm>
#include <fstream>
#include <string>

using namespace std;

#define f(i,n) for(i=0;i<n;i++)
#define takeinp(inp,fptr) fptr>>inp

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int test,t,i,j,n;
    string inpstr;
    ifstream myinpfile;
    ofstream myoutfile;
    myinpfile.open("i5.in");
    myoutfile.open("out1.txt");
    takeinp(test,myinpfile);
    f(i,test)
        {
            int d,k;
            takeinp(d,myinpfile);
            int * inp= new int[d];
            takeinp(inp[0],myinpfile);
            int curmin=inp[0],final=0;
            int curmax=inp[0];
            for(j=1;j<d;j++)
            {
                    takeinp(inp[j],myinpfile);
                    if(curmin>inp[j])
                    curmin=inp[j];
                    if(curmax<inp[j])
                    curmax=inp[j];

            }
            /*
            if(curmin<=1)
            final=curmin;
            else
            */
            final=curmax;
            for(j=1;j<=curmax;j++)
            {
                int countmin=0;
                for(k=0;k<d;k++)
                {
                    countmin+=ceil((double)(inp[k]-j)/j);

                }
                countmin+=j;
                if(final>countmin)
                {
                        final=countmin;
                        //myoutfile<<j<<" "<<ceil((double)(3-2)/2)<<endl;
                }

            }

            myoutfile<<"Case #"<<i+1<<": "<<final<<endl;

        }
		myinpfile.close();
		myoutfile.close();


    return 0;
}
