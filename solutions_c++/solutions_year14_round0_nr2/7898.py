#include<iostream>
#include<stdio.h>
#include <stdlib.h>
#include<iomanip>
#include<fstream>
using namespace std;
int main()
{
    ifstream fin;
    fin.open("abc.txt");
    ofstream fout;
    fout.open("ans.txt");
    int t;
    fin>>t;
    //scanf("%d",&t);
    for(int i=1;i<=t;i++)
    {
        double c,f,x;
        fin>>c;
        fin>>f;
        fin>>x;
       // scanf("%lf",&c);
       // scanf("%lf",&f);
       // scanf("%lf",&x);
        double time=0,temp1=0,temp2=x/2;
        double cookies=c,rate=2,rare,grand,quick=1;
        if(c>x)
        {

            fout<<"Case #"<<i<<": "<<std::fixed << std::setprecision(7) << x/2<<"\n";
            continue;
        }

        int count=0;
        rare=0;
        while(true)
        {
            rare+=(c/rate) ;
            grand=(x/(rate+f));
            //cout<<rare<<"\t"<<grand<<"\n";
            time+=rare;
            rate+=f;

            temp1=rare + grand;
            //cout<<temp1<<"\t"<<temp2<<"\n";

            if(temp2<temp1)
            {
                fout<<"Case #"<<i<<": "<<std::fixed << std::setprecision(7) << temp2<<"\n";
                break;
            }
            temp2=temp1;
            count++;
        }

        //printf("Case #%d: %.7lf\n",i+1,(time+temp2));
        //std::cout <<"Case #"<<i+1<<" " << time+temp2 << "\n";

    }
}
