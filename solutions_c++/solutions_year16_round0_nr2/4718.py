#include <iostream>
#include <fstream>
#include <cstring>
using namespace std;
int findlast(char *s)
{
    int l=strlen(s);
    for(int i=l;i>=0;i--)
    {
        if(s[i]=='-')
            return i+1;
    }
    return 0;
}
bool check(char *s,int count)
{
    for(int i=0;i<count;i++)
    {
        if(s[i]=='-')
            return false;
    }
    return true;
}
int main()
{
    ofstream out("out.txt");
    ifstream in("in.txt");
    int test;
    in>>test;
    for(int t=1;t<=test;t++)
    {
        int sum=0;
        char s[103];
        in>>s;
        int count=strlen(s);
        if(check(s,count))
        {
            out<< "Case #"<<t<< ": "<<sum<<endl;
            continue;
        }
        count=findlast(s);
        sum=1;
        for(int i=1;i<count;i++)
        {
            if(s[i]!=s[i-1])
                sum++;
        }
        out<< "Case #"<<t<< ": "<<sum<<endl;
    }
    return 0;
}
