// experimental.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

using namespace std;

class last_word
{
    string s;
        public:
    last_word()
    {
        s.clear();
    }
    void push(char c)
    {
        if(s.front()<=c)
        {
            s.insert(0, 1, c);
        }
        else
        {
            s.append(1, c);
        }
    }
    string playshow(char sb[])
    {
        s.clear();
        s.append(1, sb[0]);
        long sl=strlen(sb);
        char *b=sb, *i=sb+1, *e=sb+sl;
        while(i<e)
        {
            //cout<<*i<<"-"<<s<<"-";
            push(*i);
            //cout<<s<<"\n";
            ++i;
        }
        return s;
    }
};

void handle(istream &in, ostream &out)
{
    char buff[2000];
    long i=0, c=0, t1=0, t2=0;
    in.getline(buff, 2000, '\n');
    c=atol(buff);
    last_word lw;
    while(i<c)
    {
        in.getline(buff, 2000, '\n');
        out<<"Case #"<<i+1<<": "<<lw.playshow(buff)<<"\n";
        ++i;
    }
}

int _tmain(int argc, _TCHAR* argv[])
{
	/*if(argc<3)
    {
        cout<<"empty args\n";
        return -1;
    }*/
    /*ifstream in("D:\\in.txt", ios::binary|ios::_Nocreate);
    ofstream out("D:\\out.txt", ios::binary);
    if(in.fail()||out.fail())
    {
        cout<<"IO fail\n";
        return -1;
    }
    handle(in, out);
    in.close();
    out.close();*/
    handle(cin, cout);
    return 1;
}

