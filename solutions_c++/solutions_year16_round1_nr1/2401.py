#include <bits/stdc++.h>
using namespace std;
deque<char >q1;
int main()
{
    int a,b,c,d,i,j,p,q;
    char s[1003],x;
    scanf("%d",&p);
    for(j=1;j<=p;j++)
    {

    scanf("%s",&s);
    a=strlen(s);
    q1.push_back(s[0]);
    x=s[0];
    for(i=1;i<a;i++)
    {
        if(s[i]>=x)
        {q1.push_front(s[i]);
         x=s[i];
        }
        else
            q1.push_back(s[i]);
    }
    cout<<"Case #"<<j<<": ";
    while(!q1.empty())
    {
        x=q1.front();
        cout<<x;
        q1.pop_front();
    }
    cout<<endl;
    }
    return 0;
}
