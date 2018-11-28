#include<iostream>
#include<cstdio>
#include<fstream>
using namespace std;

int main()
{
    FILE * pFile;
    pFile = fopen ("B_out.txt", "w");
    int t;
    double c,f,x;
    scanf("%d",&t);
    
    for(int i=1;i<=t;i++){
    scanf("%lf %lf %lf",&c,&f,&x);
    double a=2.00;
    double time=0.00;
    while(100000.0*(x/a)>100000.0*((c/a)+(x/(a+f)))) {
           time+=c/a;                      
           a+=f;
    }        
    time+=x/a;
    fprintf(pFile,"Case #%d: %.7lf \n",i,time);
    }
    fclose (pFile);
    return 0;    
}
