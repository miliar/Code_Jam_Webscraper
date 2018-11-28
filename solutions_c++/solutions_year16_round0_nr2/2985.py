#include <fstream>
#include <iostream>
#include <string.h>
using namespace std;
char strings[101];
int cake(int n)
{
    int ans=0,i;
    char str[n];
    for(i=0;i<n;i++)
        str[i]=strings[i];
    if(str[0]=='+')
        ans=1;
    i=0;
    while(str[i]=='+')
    {
        str[i]='-';
        i++;
    }
    for(i=0;i<n;i++)
    {
        if(str[i]=='+')
            strings[n-i-1]='-';
        else
            strings[n-i-1]='+';
    }

    return ans+1;
}
int main()
{
    int n,t,c,i,answer=0;
    ifstream input;
    input.open("B-large.in");
    ofstream output;
    output.open("output.in");
    input>>t;
    for(c=1;c<=t;c++)
    {
        input >> strings;
        n=strlen(strings);
        answer=0;
        for(i=n-1;i>=0;i--)
        {
            if(strings[i]=='-')
                answer = answer + cake(i+1);
        }
        output<<"Case #"<<c<<": "<<answer<<endl;
    }
    input.close();
    output.close();
    return 0;
}
