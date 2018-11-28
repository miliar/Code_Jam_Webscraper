// experimental.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

using namespace std;

class pancakes
{
    char sb[101];
    int sl, cp, cn;
    void rolling_xor(char *c)
    {
        if(*c=='+')
        {
            *c='-';
        }
        else
        {
            *c='+';
        }
    }
        public:
    pancakes(char *buff=NULL)
    {
        if(buff!=NULL)
        {
            strcpy(sb, buff);
            sl=strlen(sb);
        }
        cp=0;
        cn=0;
    }
    int happy()
    {
        char *b=sb, *e=sb+sl;
        cp=0;
        cn=0;
        while(b<e)
        {
            if(*b=='-')
            {
                ++cn;
            }
            else if(*b=='+')
            {
                ++cp;
            }
            ++b;
        }
        if(cp==sl)
        {
            return 1;
        }
        else if(cn==sl)
        {
            return 0;
        }
        return -1;
    }
    long countsmiles()
    {
        long c=0;
        char *b=sb, *i=sb+1, *e=sb+sl;
        while((b<e)&&(happy()<0))
        {
            b=sb;
            i=b+1;
            while(i<e)
            {
                rolling_xor(b);
                if(*i==*b)
                {
                    break ;
                }
                ++b;
                ++i;
            }
            ++c;
        }
        if(happy()==0)
        {
            ++c;
        }
        return c;
    }
};

void handle(istream &in, ostream &out)
{
    char buff[256];
    long i=0, c=0, t1=0, t2=0;
    in.getline(buff, 255, '\n');
    c=atol(buff);
    pancakes panc;
    while(i<c)
    {
        in.getline(buff, 255, '\n');
        panc.pancakes::pancakes(buff);
        out<<"Case #"<<i+1<<" "<<panc.countsmiles()<<"\n";
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

