// experimental.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

using namespace std;

class numsets
{
    int d[10], cd, last;
        public:
    numsets()
    {
        flush();
    }
    int slept()
    {
        if(cd==10)
        {
            return 1;
        }
        return 0;
    }
    void flush()
    {
        int i=0;
        while(i<10)
        {
            d[i]=0;
            ++i;
        }
        cd=0;
        last=-1;
    }
    int push(long n)
    {
        char nm[16], *p=nm;
        ltoa(n, nm, 10);
        int i=0, l=strlen(nm), tc=0;
        while(i<l)
        {
            if((*p>='0')&&(*p<='9'))
            {
                tc=tc*10+(*p-'0');
                if(d[*p-'0']==0)
                {
                    d[*p-'0']=1;
                    ++cd;
                }
            }
            ++p;
            ++i;
        }
        if(tc!=last)
        {
            last=tc;
            return 1;
        }
        return 0;
    }
    long trytosleep(char nm[]);
};

long numsets::trytosleep(char nm[])
{
    long base=atol(nm), mul=1, n=base, f=1;
    flush();
    while(true)
    {
        n=base*mul;
        f=push(n);
        if(f==0)
        {
            break ;
        }
        else if(slept())
        {
            return n;
        }
        ++mul;
    }
    return -1;
}

void handle(istream &in, ostream &out)
{
    char buff[256];
    long i=0, c=0, t=0;
    in.getline(buff, 255, '\n');
    c=atol(buff);
    numsets ns;
    while(i<c)
    {
        in.getline(buff, 255, '\n');
        out<<"Case #"<<i+1<<": ";
        t=ns.trytosleep(buff);
        if(t<0)
        {
            out<<"INSOMNIA\n";
        }
        else
        {
            out<<t<<"\n";
        }
        ++i;
    }
}

int _tmain(int argc, _TCHAR* argv[])
{
	/*if(argc<3)
    {
        cout<<"empty args\n";
        return -1;
    }
    ifstream in(argv[1], ios::binary|ios::_Nocreate);
    ofstream out(argv[2], ios::binary);
    if(in.fail()||out.fail())
    {
        cout<<"IO fail\n";
    }
    handle(in, out);
    in.close();
    out.close();*/
    handle(cin, cout);
    return 1;
}

