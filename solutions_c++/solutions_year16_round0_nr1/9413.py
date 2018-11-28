#include <iostream>
#include <string.h>
#include <sstream>
#include <fstream>

using namespace std;

ifstream fin;
ofstream fout;
int r[10];
int main()
{
    fin.open("A-large.in");
    fout.open("test1.out");
    int n,x;
    string s;
    long numb;
    fin>>n;
    //cin>>n;
    for(int i=0;i<n;i++)
    {
        bool t=false;int h=0;
        memset (r,0,sizeof r);
        fin>>numb;
        //cin>>numb;
        long long num=numb;
        while(t==false&&(h++<=102))
        {
            stringstream ss;
            ss << num;
            ss>>s;
            for(int o=0;o<s.length();o++)
            {
                int x;
                x=s[o]-'0';
                ++r[x];
            }
            t=true;
            for(int o=0;o<10;o++)
            {
                if(r[o]==0)
                {
                    t=false;
                    num=h*numb;
                    break;
                }
            }
        }
        if(t)
        fout<<"Case #"<<i+1<<": "<<num<<endl;
        else
        fout<<"Case #"<<i+1<<": "<<"INSOMNIA"<<endl;

    }
    return 0;
}
