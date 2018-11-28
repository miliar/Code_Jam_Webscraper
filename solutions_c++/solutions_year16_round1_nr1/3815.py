#include <iostream>
#include<string>
#include<vector>
#include<list>
#include<algorithm>
using namespace std;
bool myfunction (char i,char j) { return (i<j); }


string create_words(string s)
{
    list<char> v;
    for(int i=0;i<s.size();i++)
    {
        if(s[i]>= v.front())v.push_front(s[i]);
        else
        v.push_back(s[i]);
    }



    std::string str(v.begin(),v.end());

    return str;
}

int main()
{
    int t;
    cin>>t;
    for(int l=1;l<=t;l++)
    {
        string s;
        cin>>s;
        cout<<"Case #"<<l<<": "<<create_words(s)<<endl;

    }
    return 0;
}
