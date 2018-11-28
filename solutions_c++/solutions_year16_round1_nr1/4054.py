#include <iostream>
#include<string>
#include<stdio.h>
#include<algorithm>
#include<deque>
using namespace std;

int main()
{
    int t;
    string s;
    char ch[2000];
    FILE *f;
    cin>>t;
    f=fopen("gg.txt","w");
    for(int i=0;i<t;i++)
    {
        deque<char>ob;
        cin>>s;
        //cout<<s[0];
        ob.push_front(s[0]);

        for(int j=1;j<s.length();j++)
        {
            char ch=ob.front();
            if(ch<=s[j])
            {

                ob.push_front(s[j]);
            }
            else
            {
                //cout<<"*";
                ob.push_back(s[j]);
            }
        }
        fprintf(f,"Case #%d: ",i+1);
        cout<<"Case #"<<i+1<<": ";
        deque<char>::iterator in;

        //in=ob.begin();
        for (in = ob.begin(); in != ob.end(); ++in)
            fprintf(f,"%c",*in);
    fprintf(f,"\n");
    }
    return 0;
}
