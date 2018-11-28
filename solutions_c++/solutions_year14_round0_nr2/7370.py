#include<iostream>
#include<cstdio>
#include<fstream>
#include<cstdlib>
#include<iomanip>
using namespace std;

int main()
{
    FILE * file=fopen("B-large.in","r");
    FILE * file2=fopen("output.txt","w");
    cout<<fixed<<setprecision(7);
	double c, f, x;
	int count;
	fscanf(file,"%d",&count);
	for (int i = 0; i < count; i++)
	{
	    double dur1,dur2;
        fscanf(file,"%lg",&c);
        fscanf(file,"%lg",&f);
        fscanf(file,"%lg",&x);
        dur1=x/2;
        dur2=c/2 + x/(f+2);
        for(int j=1;dur1>dur2;j++)
        {
            dur1=dur2;
            dur2=dur2-x/(j*f+2)+c/(j*f+2)+x/((j+1)*f+2);
        }
        cout<<"Case #"<<i+1<<":"<<dur1<<endl;
        fprintf(file2,"Case #%d: %.7f\n",i+1,dur1);
	}
	fclose(file);
	fclose(file2);
}
