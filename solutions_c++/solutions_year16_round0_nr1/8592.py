#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cstring>
#include <fstream>

using namespace std;

int main()
{
ifstream in; //Creating object for input stream
ofstream out; //Creating object for output stream

in.open("input.in");    //open a file to read input
out.open("output_sheep.txt"); //open a file to write output

    long long t,n,x,cnt,t_num,i,dg;
    bool dgt[10];
    in>>t;
    for(x=1;x<=t;x++)
    {
        in>>n;
        memset(dgt,false,sizeof dgt);
        cnt=0;
        if(n==0)
        out<<"Case #"<<x<<": "<<"INSOMNIA"<<endl;
        else
        {
            for(i=1;cnt!=10;i++)
        {
            t_num=i*n;
            do
            {
                    dg=t_num%10;
                    if(!dgt[dg])
                    {
                        dgt[dg]=true;
                        cnt++;
                    }
                    t_num/=10;
            }
            while(t_num>0&&cnt!=10);
        }
		out<<"Case #"<<x<<": "<<((i-1)*n)<<endl;
        }
	}

in.close();             //closing the input file
out.close();            //closing the output file

    return 0;
}
