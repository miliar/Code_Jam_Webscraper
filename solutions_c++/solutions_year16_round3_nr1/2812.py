#include <iostream>
#include <fstream>
using namespace std;
int num(int *a)
{
    int sum=0;
    for(int i=0;i<26;i++)
    {
        if(a[i])
            sum++;
    }
    return sum;
}
int max(int *a)
{
    int pos=0;
    for(int i=0;i<26;i++)
    {
        if(a[i]>a[pos])
            pos=i;
    }
    return pos;
}
int main()
{
    ofstream out("out.txt");
    ifstream in("in.txt");
    int test;
    in>>test;
    for(int t=1;t<=test;t++)
    {
        out<< "Case #"<<t<< ": ";
        int n;
        in>>n;
        int a[26]={0};
        for(int i=0;i<n;i++)
        {
            in>>a[i];
        }
        while(num(a)>2)
        {
            int pos=max(a);
            char ch='A'+pos;
            out<<ch<< " ";
            a[pos]--;
        }
        int pos1,pos2;
        for(int i=0;i<26;i++)
        {
            if(a[i])
            {
                pos1=i;
                break;
            }
        }
        for(int i=25;i>=0;i--)
        {
            if(a[i])
            {
                pos2=i;
                break;
            }
        }
        while(a[pos1]>a[pos2])
        {
            char ch='A'+pos1;
            out<<ch<< " ";
        }
        while(a[pos2]>a[pos1])
        {
            char ch='A'+pos2;
            out<<ch<< " ";
        }
        char ch1='A'+pos1;
        char ch2='A'+pos2;
        while(a[pos1])
        {
            out<<ch1<<ch2<< " ";
            a[pos1]--;
        }
        out<<endl;
    }
    return 0;
}
