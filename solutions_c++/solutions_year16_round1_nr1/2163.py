#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t;
    cin>>t;
    for(int i=1;i<=t;i++)
    {
        char s[1200];
        scanf("%s",s);
        fflush(stdin);
        deque<char> w;
        w.push_back(s[0]);
        for(int j=1;s[j]!=0;j++)
        {
            if(s[j]>=w.front())
            {
                w.push_front(s[j]);
            }
            else
            {
                w.push_back(s[j]);
            }
        }
        cout<<"Case #"<<i<<": ";
        while(!w.empty())
        {
            cout<<w.front();
            w.pop_front();
        }
        cout<<endl;
    }
}
