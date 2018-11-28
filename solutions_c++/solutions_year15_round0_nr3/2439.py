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

int red(char a)
{
    if(a=='1')
    return 0;
    if(a=='i')
    return 1;
    if(a=='j')
    return 2;
    if(a=='k')
    return 3;

}

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int test,t,i,j,n;
    string inpstr;
    ifstream myinpfile;
    ofstream myoutfile;
    myinpfile.open("i6.in");
    myoutfile.open("out1.txt");
    takeinp(test,myinpfile);
    int db[4][4]={{0,1,2,3},{1,0,3,2},{2,3,0,1},{3,2,1,0}};
    int sign[4][4]={{1,1,1,1},{1,-1,1,-1},{1,-1,-1,1},{1,1,-1,-1}};
    f(i,test)
        {
            int l,k;
            string inp;
            takeinp(l,myinpfile);
            takeinp(k,myinpfile);
            takeinp(inp,myinpfile);
            int cur=0,one=1,done=0,j=0,temp;

                while(done<=0&&j<l*k)
                {
                    temp=cur;
                    cur=db[cur][red(inp[j%l])];
                    if(cur==1)
                    done=1;
                    one*=sign[temp][red(inp[j%l])];
                    j++;
                }
                cur=0;
                while(done==1&&j<l*k)
                {
                    temp=cur;
                    cur=db[cur][red(inp[j%l])];
                    if(cur==2)
                    done=2;
                    one*=sign[temp][red(inp[j%l])];
                    j++;
                }
                cur=0;
                while(done==2&&j<l*k)
                {
                    temp=cur;
                    cur=db[cur][red(inp[j%l])];
                    if(cur==3)
                    done=3;
                    one*=sign[temp][red(inp[j%l])];
                    j++;
                }
                cur=0;
                while(j<l*k)
                {
                    temp=cur;
                    cur=db[cur][red(inp[j%l])];

                    one*=sign[temp][red(inp[j%l])];
                    j++;

                }
                if(done==3&&cur==0&&one==1)
                    myoutfile<<"Case #"<<i+1<<": "<<"YES"<<endl;
                else
                    myoutfile<<"Case #"<<i+1<<": "<<"NO"<<endl;






        }
		myinpfile.close();
		myoutfile.close();


    return 0;
}
