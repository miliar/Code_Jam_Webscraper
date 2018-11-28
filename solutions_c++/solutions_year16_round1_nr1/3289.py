#include<iostream>
#include<cstdio>
#include<deque>
#include<string>
using namespace std;


int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);

    int T;
    cin>>T;
    for (int k = 1; k <= T; k++)
    {
        deque <char> que;
        string str;
        cin>>str;
        int l = str.length();
        for (int j = 0; j < l; j++)
        {
            char c = str[j];
            if (que.size() == 0)
                que.push_back(c);
            else if (c >= que.front())
                que.push_front(c);
            else
                que.push_back(c);
        }

        cout<<"Case #"<<k<<": ";
        while(que.size()!=0)
        {
            cout<<que.front();
            que.pop_front();
        }
        cout<<endl;
    }


    fclose(stdin);
    fclose(stdout);
}
