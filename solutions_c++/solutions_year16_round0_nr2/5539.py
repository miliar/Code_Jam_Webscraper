#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("output_large.txt","w",stdout);
    int t,cnt=1;
    cin>>t;
    while(t--)
    {
        string s;
        cin>>s;
        stack<char> s1,s2,s3;
        int len=s.length(),k=-1;
        for(int i=len-1;i>=0;i--)
        {
            if(s[i]=='-')
            {
                k=i;
                break;
            }
        }
        for(int i=k;i>=0;i--)
        {
            s1.push(s[i]);
        }
        int counter=0;
        while(!s1.empty())
        {
            if(s1.top()=='+')
            {
                while(s1.top()!='-')
                {
                    s2.push('-');
                    s1.pop();
                }
                while(!s2.empty())
                {
                    s1.push('-');
                    s2.pop();
                }
                counter++;
            }
            else
            {
                char x;
                while(!s1.empty())
                {
                    x=s1.top();
                    if(x=='+')
                        s2.push('-');
                    else
                        s2.push('+');
                    s1.pop();

                }
                while(!s2.empty())
                {
                    s3.push(s2.top());
                    s2.pop();
                }
                while(!s3.empty()&&s3.top()!='-')
                {
                    s3.pop();
                }
                while(!s3.empty())
                {
                    s1.push(s3.top());
                    s3.pop();
                }
                counter++;
            }
        }
        cout<<"Case #"<<cnt<<": "<<counter<<endl;
        cnt++;
    }
}
