#include <iostream>
#include <fstream>
using namespace std;
string s;

void swap(int i, int j)
{
    char t;
    while(j>i)
    {
        if(s[i]=='-')s[i]='+';
        else s[i]='-';

        if(s[j]=='-')s[j] = '+';
        else s[j] = '-';

        t = s[i];
        s[i] = s[j];
        s[j] = t;
        i++;
        j--;
    }
    if(i==j)
    {
        if(s[j]=='-')s[j] = '+';
        else s[j] = '-';
    }
}

int main()
{
    ifstream in;
    ofstream out;
    in.open("B-large.in");
    out.open("out.txt");
    long long int T,c,end,start;
    in>>T;
    for(int t=1; t<=T; t++)
    {
        in>>s;
        out<<"Case #"<<t<<": ";
        start = -1;
        end = s.size()-1;
        c=0;
        while(end!=-1)
        {
            for(int i=end; i>=0; i--)
            {
                if(s[i]=='-')
                {
                    end = i;
                    break;
                }
                if(i==0)end=-1;
            }
            for(int i=0; i<s.size(); i++)
            {
                if(s[i]=='-')
                {
                    start = i-1;
                    break;
                }
            }
            if(start>=0)
            {
                swap(0,start);
                c++;
                start = -1;
            }
            if(end!=-1)
            {
                swap(0,end);
                c++;
                end = s.size()-1;
            }
        }
        out<<c<<endl;
    }
    return 0;
}
