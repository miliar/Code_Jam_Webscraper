
#include <iostream>
#include <stdio.h>
#include <cmath>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <cassert>
#include <fstream>
#include <ctime>
#include <cstdlib>
#include <algorithm>
#define Pi 3.14159
#define vi vector<int>
#define pi pair<int,int>
#define si stack<int>

typedef long long int ll;
using namespace std;

double ti (double c,double f,double t,double k)
{
if(t <= (c*(k+f)/f)){return t/k;}
else return c/k + ti(c,f,t,k+f);
}
int main ()
{
    FILE * pfile;
    pfile = fopen("myfile5.txt","w");
    ifstream inn;
    //ofstream out;
    //out.open("out.txt");
    inn.open("b.in");
    int test;
    inn>>test;
    for(int z = 1;  z <= test;z++)
    {
        double c,f,t;
        inn>>c>>f>>t;
        double  p = ti(c,f,t,2.0);
        fprintf(pfile,"Case #");
        fprintf(pfile,"%d",z);
        fprintf(pfile,": ");
        fprintf(pfile,"%.7f \n",p);
    }
    fclose(pfile);
}
