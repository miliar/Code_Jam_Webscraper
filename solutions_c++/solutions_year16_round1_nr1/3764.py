#include<iostream>
#include<list>
using namespace std;
int main()
{
    int T,x=1;
    cin>>T;
    list <char> y;
    while(T--)
    {
        string inp="";
        cin>>inp;
        y.clear();
        y.push_back(inp[0]);
        for(int i=1;i<inp.length();i++)
        {
            if(inp[i]>=*y.begin())
                y.push_front(inp[i]);
            else
                y.push_back(inp[i]);
        }
        cout<<"Case #"<<x++<<": ";
        list <char> :: iterator it;
        for(it=y.begin();it!=y.end();it++)
            cout<<*it;
        cout<<endl;
    }
    return 0;
}
