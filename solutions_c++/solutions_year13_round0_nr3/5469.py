#include<iostream>
#include<cstdio>
#define max 1000
#include<fstream>
#include<cmath>
using namespace std;
int cases;
int pal(int no) //if no is palandrome return 1 else return 0
{
    if(no<10)
        return 1;
    int l=ceil(log10(no));
    while(no!=0)
    {
        int n1=no%10;
        int n2=no/pow(10,l-1);
        if(n1!=n2)
        {
        return 0;
        }
        no=no-n2*pow(10,l-1);
        no/=10;
        l-=2;
    }
    return 1;
}
int main()
{
    ofstream myfile;
    myfile.open ("3.txt");
    cin>>cases;
    for(int u=0;u<cases;u++)
    {
        int min1,max1;
        cin>>min1>>max1;
        int srmin=ceil(sqrt(min1));
        int srmax=floor(sqrt(max1));
        //cout<<"\nmax="<<max1<<"\t"<<srmax<<"\nmin="<<min1<<"\t"<<srmin;
        int count=0;
        for(int no=srmin;no<=srmax;no++)
        {
            if(pal(no) & pal(no*no))
                count++;
        }
        myfile<<"Case #"<<u+1<<": "<<count<<"\n";
    }
    myfile.close();
}
