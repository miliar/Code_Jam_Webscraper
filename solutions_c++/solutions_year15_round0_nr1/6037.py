#include<iostream>
#include<fstream>
using namespace std;

int main()
{
    int i,j,t,s,r,sum,y;
    char a[1002];
    fstream fin,fout;
    fin.open("A-large.in",ios::in);
    fout.open("op.txt",ios::out);
    fin>>t;
    //cin>>t;
    for(i=1;i<=t;i++)
    {
        fin>>s;
        fin>>a;
        sum=y=0;
        for(j=0;a[j]!='\0';j++)
        {
            if(a[j]-'0'>0)
            {
                if(j<=sum)
                    sum+=a[j]-'0';
                else
                {
                    r=j-sum;
                    y+=r;
                    sum+=(int)(a[j]-'0')+r;
                }
            }
        }
        fout<<"Case #"<<i<<": "<<y<<endl;
    }
    fin.close();
    fout.close();
    return 0;
}
