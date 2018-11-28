#include<iostream>
#include<stdio.h>
#include<fstream>
#include<iomanip>
using namespace std;
int main()
{
    ifstream fin;
    fin.open("abc.txt");
    ofstream fout;
    fout.open("ans.txt");
    int test;
    fin>>test;
    for(int z=1;z<=test;z++)
    {
        double c,f,x;
        fin>>c>>f>>x;
        double prev=x/2;
        double next=0;
        double time=0;
        double div=2;
        double tobe=0;
        double sum=0;
        //int count=1;
       // int flag=0;
        while(true)
        {
            time+= c/div;
            div+=f;
            tobe=x/div;
            sum=time+tobe;
            if(sum>prev)
            {
                fout<<"Case #"<<z<<": "<<std::fixed << std::setprecision(7) << prev<<"\n";
                //fout<<std::fixed << std::setprecision(7) << prev;
                //fout<<"\n";
                //printf("%.7f",prev);
                //flag=1;
                break;
            }
            prev=sum;
        }
    }
    return 0;
}
