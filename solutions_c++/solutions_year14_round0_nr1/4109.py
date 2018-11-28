#include<iostream>
#include<fstream>
using namespace std;
int main()
{
    fstream f1,f2;
    int t;
    f1.open("CJsmalltrickf",ios::in);
    f2.open("output",ios::out);
    f1.seekg(0);
    f1>>t;
    for(int i=0;i<t;i++)
    {
        f2<<"Case #"<<i+1<<": ";
        int sol1,sol2;
        int ary1[4][4],ary2[4][4],solu1[4]={0},solu2[4]={0},d=0,count=0,value;
        f1>>sol1;
        for(int j=0;j<4;j++)
            for(int k=0;k<4;k++)
                {f1>>ary1[j][k]; if(j+1==sol1)solu1[d++]=ary1[j][k];}
        d=0;
        f1>>sol2;
        for(int j=0;j<4;j++)
            for(int k=0;k<4;k++)
                {f1>>ary2[j][k]; if(j+1==sol2)solu2[d++]=ary2[j][k];}
        for(int j=0;j<4;j++)
            for(int k=0;k<4;k++)
                if(solu1[j]==solu2[k])
                {
                    count++;
                    value=solu1[j];
                    break;
                }
        if(count==0)f2<<"Volunteer cheated!"<<endl;
        else if(count==1)f2<<value<<endl;
        else f2<<"Bad magician!"<<endl;
    }
    return 0;
}
