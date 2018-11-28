#include<cstdio>
#include<algorithm>
#include<fstream>
using namespace std;
double x,c,f,a,produce,tp,tf,tn;
int main()
{
    int t,k;
    ifstream ifile;
    ifile.open("B-large.in");
    ifile>>t;
    FILE * pf=fopen("ans.txt","w");
    //FILE *sf =fopen("b.txt","w+");
    //fscanf(sf,"%d",&t);
    for(k=1;k<=t;k++)
    {
        //fscanf(sf,"%lf%lf%lf",&c,&f,&x);
        ifile>>c>>f>>x;
        tp=x/2;
        tn=c/2+x/(2+f);
        tf=c/2+c/(2+f);
        produce=2+2*f;
        while(tn<tp)
        {
            //printf("%lf ",tp);
            tp=tn;
            tn=tf+x/produce;
            tf=tf+c/produce;
            produce+=f;
            //printf("%lf ",tp);
        }
        fprintf(pf,"Case #%d: %.7lf\n",k,tp);
    }
    fclose(pf);
}
