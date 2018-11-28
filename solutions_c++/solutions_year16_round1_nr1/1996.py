#include<bits/stdc++.h>
#include<fstream>
using namespace std;
main()
{
        unsigned long long T;
        ifstream in("in.in");
        ofstream out("output.out");
        in>>T;
        string tt;
        std::getline(in,tt);
        for(int z=0;z<T;z++)
        {
                string str;
                std::getline(in,str);
                for(int i=1;i<str.length();i++)
                {
                        if(str[i]<str[i-1])
                                continue;
                        else if(str[i]<str[0])
                                continue;
                        else
                        {
                                char tmp=str[i];
                                for(int j=i;j>0;j--)
                                {
                                        str[j]=str[j-1];
                                }
                                str[0]=tmp;
                        }
                }
                out<<"Case #"<<z+1<<": "<<str<<"\n";
        }
}
