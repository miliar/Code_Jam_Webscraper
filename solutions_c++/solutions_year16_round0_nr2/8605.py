#include <iostream>
#include <algorithm>
#include<set>
#include<cstring>
#include<stdio.h>
#include<vector>
#include<cstdio>
#include<map>
//priyansh chutiya h
//priyansh chutiya h
//priyansh chutiya h
//priyansh chutiya h
//pjfdbkgdklg;ldfkg;ldriyansh chutiya h
//priyansh chutiy.gjdfhkgjdfa h
//priyansh chutiyfnkjghkjdfngkldfsa h
//priyansh chutiya h
//priyansh chutiya h
//priyansh chutikhfuifgjdgijdfsklguidshfgfdslya h
//priyansh chutiya h
//priyansh chhgrkhgjksdfhkutiya h

using namespace std;

string reverser(string ass,long long int i,long long int k)
{
    for(long long int prr=i,yrr=k;yrr>=prr;prr++,yrr--)
    {
        if(prr!=yrr)
        {
            if(ass[prr]=='+')
                ass[prr]='-';
            else
                ass[prr]='+';
        }
         if(ass[yrr]=='+')
                ass[yrr]='-';
            else
                ass[yrr]='+';
        swap(ass[prr],ass[yrr]);
    }
    return ass;
}

int main()
{
    freopen("input.in","r",stdin);
	freopen("outerr.in","w",stdout);
    long long int test;
    cin>>test;
    long long int c= test;
    while(test--)
    {
        string str;
        cin>>str;
        long long int lenth=str.size()-1;
        long long int counter=0;
        while(lenth>=0)
        {
            long long int k=lenth;
            while(str[k]=='+')
            {
                k--;
            }
            lenth=k;
            if(lenth>=0)
            {
                long long int i=0;
                while(str[i]=='+')
                {
                    i++;
                }
                if(i)
                {
                    str=reverser(str,0,i-1);
                    counter++;
                }
                str=reverser(str,0,lenth);
                counter++;
            }
        }
    cout<<"Case #"<<c-test<<": "<<counter<<endl;
    }
return 0;
}
