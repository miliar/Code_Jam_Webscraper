#include<iostream>
#include<string>
#include<algorithm>
using namespace std;
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int tc;
    cin>>tc;
    for(int mindol=1;mindol<=tc;mindol++)
    {
        string str;
        cin>>str;
        int len = str.length(), cnt=0;
        string dest;
        for(int i=0;i<len;i++) dest.push_back('+');
        while(str!=dest)
        {
            int now=0;
            for(int i=1;i<len;i++)
            {
                if(str[i]==str[now]) now=i;
                else break;
            }
            for(int i=0;i<=now;i++)
                str[i] = ((str[i]=='+')?'-':'+');
            for(int s=0,e=now;s<e;s++,e--)
                swap(str[s],str[e]);
            cnt++;
        }
        cout<<"Case #"<<mindol<<": "<<cnt<<endl;
    }
    return 0;
}
