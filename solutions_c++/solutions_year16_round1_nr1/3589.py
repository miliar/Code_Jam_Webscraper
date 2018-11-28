#include<iostream>
#include<list>
using namespace std;
int main()
{
    int T;
    string s;
    cin>>T;
    for(int i=0;i<T;i++)
    {
        list<char> ans;
        cin>>s;
        ans.push_back(s[0]);
        for(string::iterator it=s.begin()+1;it!=s.end();it++)
        {
            if(*it<ans.front())ans.push_back(char(*it));
            else ans.push_front(char(*it));
        }
        cout<<"Case #"<<i+1<<": ";
        for(list<char> :: iterator it=ans.begin();it!=ans.end();it++)
        {
            cout<<(*it);
        }
        cout<<endl;
    }
}
