//Ankit Kumar
#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<fstream>
#include<iomanip>
using namespace std;
int main()
{
    fstream f1,f2;
    f1.open("B-small-attempt2.in",ios::in);
    f2.open("out.txt",ios::out);
    int a,b,k;
    int case_no;
    f1>>case_no;
    for(int i=0;i<case_no;i++)
    {
        int ccount=0;
        f1>>a>>b>>k;
        int *a1=new int [a];
        int *a2=new int [b];
        for(int p=0;p<a;p++)
        {
            a1[p]=p;
        }
        for(int p=0;p<b;p++)
        {
            a2[p]=p;
        }
        for(int q=0;q<a;q++)
        {
            for(int p=0;p<b;p++)
            {
                int jj=(a1[q] & a2[p]);
                if(jj<k)
                {
                    ccount++;
                }

            }
        }
        f2<<"Case #"<<i+1<<": "<<ccount<<endl;
        ccount=0;
        delete[]a1;
        delete []a2;
    }
    return 0;
}
//Done
