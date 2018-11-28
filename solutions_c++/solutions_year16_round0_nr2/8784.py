#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main()
{
    ifstream f1("B-small-attempt1.in");
    ofstream f2("small2.out");
    int T;
    int y;
    f1>>T;
    //cin>>T;
    string s;
    int m[100];
    int count;
    int flag,flag1;
    int w;
    for(int i=0;i<T;i++)
    {
        y=0;
        count=0;
        flag=1;
        f1>>s;
        //cin>>s;
        count=s.size();
        for(int j=0;j<100;j++)
        {
            m[j]=1;   //1±íÊ¾+
        }
        for(int j=0;j<count;j++)
        {
            if(s[j]=='-')m[j]=0;
        }

        while(flag)
        {
            for(w=99;w>=0;w--)
            {
                if(m[w]==0)
                {
                    if(m[0]==0)
                    {
                        y++;
                        int n[w+1];
                        for(int k=0;k<=w;k++)
                        {
                            n[w-k]=1-m[k];
                        }
                        for(int k=0;k<=w;k++)
                        {
                            m[k]=n[k];
                        }
                    }
                    else
                    {
                        flag1=1;
                        y++;
                        for(int k=0;k<=w&&flag1;k++)
                        {
                            if(m[k]==1)
                            {
                                m[k]=0;
                            }
                            else
                            {
                                flag1=0;
                            }
                        }
                    }
                }
            }
            if(w<0)
            {
                flag=0;
            }
        }


        f2<<"Case #"<<i+1<<": "<<y<<endl;
        //cout<<"Case #"<<i+1<<": "<<y<<endl;
    }

    return 0;
}
