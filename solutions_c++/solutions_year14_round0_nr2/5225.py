#include<iostream>
#include<cstdio>
#include<vector>
#include<fstream>
#include<iomanip>
using namespace std;
main()
{
    //FILE *file=fopen("output1.txt", "w");
    //FILE *ifile=fopen("A-small-attempt1.in", "r");
    ofstream ofile("output1.txt");
    ifstream ifile("B-large.in");
    int t;
    ifile>>t;
    //fscanf(ifile,"%d",&t);
    double c,f,x;
    for(int z=1;z<=t;++z)
    {
        ifile>>c>>f>>x;
        //fscanf(ifile,"%f%f%f",&c,&f,&x);
        int p=x/c-2.0/f;
        double sum=0;
        for(int i=0;i<p;++i)
        {
            sum+=c/(2+i*f);
        }
        if(p>=0)
            sum+=x/(2+p*f);
        else
            sum=x/2;
        //fprintf(file,"Case #%d: %.7f\n",z,sum);
        ofile<<"Case #"<<z<<": ";
        ofile.setf ( std::ios::floatfield, ios::fixed);
        ofile.precision(7);
        ofile<<sum<<endl;
    }
    //fclose(file);
    //fclose(ifile);
}
