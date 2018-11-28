#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<fstream>
#include<cmath>
#include<sstream>
using namespace std;
string convertInt(int number)
{
   stringstream ss;
   ss << number;
   return ss.str();
}
bool is_power_of_2(int i) {
    if ( i < 0 || i==0 ) {
        return 0;
    }
    return ! (i & (i-1));
}
string checkAsc(int p,int q)
{
    double t=(double)q/p;
    cout.precision(5);
    int temp=ceil(t);
    cout<<p<<" "<<q<<" "<<temp<<endl;
    if(p!=1)
    {
        if(p%q==0)
        {
            q=temp;
            p=1;
        }
    }
    if(!is_power_of_2(q))
        return "impossible";
    if(temp<2||temp==2)
    {
        return "1";
    }
    else
    {
        return(convertInt(ceil(log2(temp))));
    }
}
int main()
{
    double prod;
    int t;
    string val;
    int i=1;
    string in;
    int p,q;
    fstream fin,fout;
    fin.open("A-small-attempt3.in",ios::in);
    fin>>t;
    fout.open("out.txt",ios::out);
    while(i<t+1)
    {
        p=0,q=0;
        fin>>in;
        int j=0;
        while(in[j]!='/')
        {
            p=(p*10)+(in[j++]-48);
        }
        j++;
        while(j<in.length())
        {
            q=(q*10)+(in[j++]-48);
        }
        //cout<<p<<" "<<q<<endl;
        val=checkAsc(p,q);
        fout<<"Case #"<<i<<": "<<val<<endl;
        i++;
    }
    fin.close();
}
