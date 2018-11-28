#include<iostream>
#include<deque>
#include<iterator>

using namespace std;

int main()
{
    int t,t1;
    cin>>t;
    t1=t;
    deque<char> d;
    deque<char>::iterator it;
    while(t--)
    {
        string s;
        cin>>s;
        int l=s.length();
        for(int i=0;i<l;i++)
        {
            if(i==0)
            {
                d.push_back(s[i]);
                continue;
            }
            if(s[i]>=d.front())
            {
                d.push_front(s[i]);
            }
            else
            {
                d.push_back(s[i]);
            }
        }
        cout<<"Case #"<<t1-t<<": ";
        for(it=d.begin();it!=d.end();it++)
        {
            cout<<*it;
        }
        cout<<endl;
        d.clear();

    }
        return 0;
}

