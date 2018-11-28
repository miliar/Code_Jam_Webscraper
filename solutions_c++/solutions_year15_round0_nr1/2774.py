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
    myinpfile.open("i1.in");
    myoutfile.open("out1.txt");
    takeinp(test,myinpfile);
    f(i,test)
        {
            int sofar=0,needed=0,smax,temp;
            char tc[1];
            takeinp(smax,myinpfile);
            takeinp(inpstr,myinpfile);
            tc[0]=inpstr[0];
            sofar=atoi(tc);
            for(j=1;j<=smax;j++)
            {
                tc[0]=inpstr[j];
                temp =atoi(tc);
                if(j>sofar+needed)
                {
                    needed=j-sofar;

                }
                sofar+=temp;

            }

            myoutfile<<"Case #"<<i+1<<": "<<needed<<endl;

        }
		myinpfile.close();
		myoutfile.close();


    return 0;
}
