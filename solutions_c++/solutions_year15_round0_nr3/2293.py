#include <iostream>
#include <string>
#include <fstream>

using namespace std;

char prods[80000];
string str;
long long l,x,n;

char prod(char a, char b)
{
    bool negative=0;
    if(a>='A' && a<='Z' && b>='a' && b<='z' || b>='A' && b<='Z' && a>='a' && a<='z')
        negative=1;
    if(a>='A' && a<='Z')
        a=a-('A'-'a');
    if(b>='A' && b<='Z')
        b=b-('A'-'a');
    if(a==b)
        if(negative)
            return 'a';
        else
            return 'A';
    if(a=='a')
    {
        if(negative)
            return b+('A'-'a');
        else
            return b;
    }
    else if(b=='a')
    {
        if(negative)
            return a+('A'-'a');
        else
            return a;
    }
    else if(a=='i')
    {
        if(b=='j')
            if(negative)
                return 'k'+('A'-'a');
            else
                return 'k';
        if(b=='k')
            if(negative)
                return 'j';
            else
                return 'j'+('A'-'a');
    }
    else if(a=='j')
    {
        if(b=='i')
            if(negative)
                return 'k';
            else
                return 'k'+('A'-'a');
        if(b=='k')
            if(negative)
                return 'i'+('A'-'a');
            else
                return 'i';

    }
    else if(a=='k')
    {
        if(b=='i')
            if(negative)
                return 'j'+('A'-'a');
            else
                return 'j';
        if(b=='j')
            if(negative)
                return 'i';
            else
                return 'i'+('A'-'a');
    }
}

char div(char a, char b)
{
    if(a=='a')
        return b;
    else if(a=='A')
        if(b>='A' && b<='Z')
            return b-('A'-'a');
        else
            return b+('A'-'a');
    else
    {
        char t=prod(a, b);
        if(t>='A' && t<='Z')
            return t-('A'-'a');
        else
            return t+('A'-'a');
    }
}

void count_prods()
{
    prods[0]=str[0];
    for(int i=1; i<l; i++)
        prods[i]=prod(prods[i-1], str[i]);
}

int next(int &i)
{
    i+=1;
    if(i==l)
        i=0;
    return i;
}

int next0(int i)
{
    i+=1;
    if(i==l)
        i=0;
    return i;
}

int main()
{
    ifstream cin("in.dat");
    ofstream cout("out.dat");
    //*
    int tc;
    cin>>tc;
    for(int t=0;t<tc;t++)
    {
        cin>>l>>x;
        cin>>str;
        n=l*x;
        l*=4;
        str+=str;
        str+=str;
        count_prods();
        bool fl=1;

        char cur1='a';
        bool f1=1;
        long long pos1=0;

        for(int i=0; (i!=0 || f1) && fl && pos1<n ; next(i))
        {
            f1=0;
            cur1=prod(cur1, str[i]);
            if(cur1=='i')
            {
                char cur2='a';
                bool f2=1;
                long long pos2=pos1+1;
                for(int j=next0(i); (j!=next0(i) || f2) && fl && pos2<n; next(j))
                {
                    f2=0;
                    cur2=prod(cur2, str[j]);
                    if(cur2=='j')
                    {
                        long long cs=(n-1)%l;
                        /*
                        char cur3='a';
                        bool f3=1;
                        long long pos3=pos2+1;
                        for(int k=next0(j); (k!=cs || f3) && fl && pos3<n; next(k))
                        {
                            f3=0;
                            cur3=prod(cur3, str[k]);

                            pos3++;
                        }
                        //*/
                        //*
                        char cur3;
                        if(j<cs)
                            cur3=div(prods[j], prods[cs]);
                        else
                            cur3=prod(div(prods[j], prods[l-1]), prods[cs]);
                        //*
                        if(cur3=='k')
                            fl=0;
                    }
                    pos2++;
                }
            }
            pos1++;
        }
        if(!fl)
            cout<<"Case #"<<t+1<<": "<<"YES"<<endl;
        else
            cout<<"Case #"<<t+1<<": "<<"NO"<<endl;
    }
    //*/
    return 0;
}
