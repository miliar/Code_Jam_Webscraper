#include<iostream>
#include<stdio.h>
#include<fstream>

int a[10]={0,0,0,0,0,0,0,0,0,0};
int check()
{   for(int i=0;i<10;i++)
    {
    if(a[i]==0)
        return 1;
    }
    return 0;
}


using namespace std;
int main()
{
    ifstream fin;
    ofstream fout;
    fout.open("oo.txt");
     fin.open("rr.txt");

	long int t,n,f,m=1,s,r,c;
	fin>>t;
	for(int i=0;i<t;i++)
    {
        fin>>n;
        f=0;
        if(n==0)
            f=1;
        m=1;
        for(int i=0;i<10;i++)
        {
            a[i]=0;

        }
        while(check()&&f!=1)
        {
            s=m*n;
            c=s;
            m++;
            while(s>0)
            {
                r=s%10;
                if(a[r]!=1)
                    a[r]=1;
                s=s/10;
            }
        }
        if(f==1)
            fout<<"Case #"<<i+1<<": INSOMNIA\n";
        else
            fout<<"Case #"<<i+1<<": "<<c<<"\n";
    }
	fin.close();
fout.close();
return 0;
	}
