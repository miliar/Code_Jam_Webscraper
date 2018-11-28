#include<iostream>
#include<fstream>
using namespace std;

int main()
{
     ifstream input("input.txt");
    ofstream output("output.txt",ios::trunc);
    int t,p;
    input>>t;
    double c,f,x,a=0,b=0,rate=2,r,co=0,time=0,temp;
    for(p=1;p<=t;p++)
    {
        input>>c>>f>>x;
        while(true)
        {
            if(co>=x)
                break;
            if(co<c && c<x)
            {
                temp=(c-co)/rate;
                time=temp+time;
                co=co+rate*temp;

            }
            else
                    {
                        a=(x-co)/rate;
                            b=(x-co+c)/(rate+f);
            if(b<=a)
            {
                co=co-c;
                rate=rate+f;
            }
            else
            {
                temp=(x-co)/rate;
                time=time+temp;
                break;
                            }
                    }
        }
        output<<"Case #"<<p<<": ";
        char out[255];
        for(int i=0;i<255;i++)
            out[i]='\0';
        sprintf(out, "%0.7f", time);
        int i=0;
        while(out[i]!='\0')
        {
            output<<out[i];
            i++;
        }
        output<<endl;
        //printf("%0.7f\n",time);
        //fputs(out,output);
        rate=2;
        time=0;
        co=0;
    }




return 0;
}


