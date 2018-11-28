#include <stdlib.h>
#include <cstdio>
#include <algorithm>
#include <string>
#include <vector>
#include <cmath>
#include <deque>
#include <iostream>
#include <list>
#define FOR(x,z) for(int x=0;x<(z);++x)
#define DS(i) fprintf(stderr, "DEBUG: %s\n",i);
#define DI(i) fprintf(stderr, "DEBUG: %d\n",i);
#define DF(i) fprintf(stderr, "DEBUG: %f\n",i);
using namespace std;
list<char>c1, c2;
int N;
void wczytaj()
{
    scanf("%d",&N);
    string s;
    cin >> s;
    FOR(i,s.length())
        c1.push_back(s[i]);
    cin >> s;
    FOR(i,s.length())
        c2.push_back(s[i]);
}
void wykonaj()
{
    int wynik=0;
    int l1=c1.size(),l2=c2.size();
    list<char> c11(c1.begin(),c1.end()),c22(c2.begin(),c2.end());
    c1.unique();
    c2.unique();
    bool felgawon=false;
    if(c1.size()!=c2.size())
    {
        felgawon=true;
    }
    else
    {
        list<char>::iterator it11=c1.begin();
        list<char>::iterator it22=c2.begin();
        for(;it22!=c2.end();it22++,it11++)
            if((*it11)!=(*it22))
            {
                felgawon=true;
                break;
            }
        if(!felgawon)
        {

            list<char>::iterator it1=c11.begin();
            list<char>::iterator it2=c22.begin();
            char p=' ';
            for(;it1!=c11.end()&&it2!=c22.end();)
            {
                if((*it1)==(*it2))
                {
                    p=(*it1);
                    it1++;
                    it2++;
                }
                else
                {
                    if(*it1!=p)
                    {
                        p=(*it1);
                        while((*it2)!=p)
                        {
                            it2++;
                            wynik++;
                        }

                    }
                    else if(*it2!=p)
                    {
                        p=(*it2);
                        while((*it1)!=p)
                        {
                            it1++;
                            wynik++;
                        }
                    }

                }
            }
            while(it1!=c11.end())
            {
                wynik++;
                it1++;
            }
            while(it2!=c22.end())
            {
                wynik++;
                it2++;
            }
        }
    }
    if(felgawon)
        printf("%s\n", "Fegla Won");
    else
        printf("%d\n",wynik);
    c1.clear();
    c2.clear();
}
int main()
{
//    c1.reserve(100);
 //   c2.reserve(100);
    int T;
    scanf("%d",&T);
    for(int t=1;t<=T;t++)
    {
        wczytaj();
        DI(t)
        printf("Case #%d: ",t);
        wykonaj();
    }
    return 0;
}
