#include<iostream>
#include<vector>
#include<stack>
#include<queue>
#include<list>
#include<map>
#include<set>
#include<cstdio>
#include<cmath>
#include<cstring>
#include<algorithm>
#define U unsigned long long int
#define INF 9999999
#define NIL -1
using namespace std;
bool check(char c)
{
    if(c=='a' || c=='e' ||c=='i' || c=='o' || c=='u')
    return 1;
    else
    return 0;
}
bool match(string str,int n)
{
    bool f;
    int i,j;
    int l=str.length();
    //cout<<str<<" ";
    for(i=0;i<=l-n;i++)
    {
            f=1;
            for(j=0;j<n;j++)
            {
                if(check(str[i+j]))
                {
                    f=0;
                    break;
                }
            }
        if(f)
        return 1;
        else
        continue;
    }
return 0;
}
main()
{
    int tc,n,i,j;
    cin>>tc;
    string str,s1;
    int casen=0;
    while(tc--)
    {
        casen++;
        cin>>str>>n;
        int count=0;
        int l=str.length();
        for(i=0;i<=l-n;i++)
        {
            for(j=n;j<=l-i;j++)
            {
                s1=str.substr(i,j);
                bool res=match(s1,n);
                if(res)
                count++;
            }
        }
        cout<<"Case #"<<casen<<": "<<count<<endl;
    }

//system("pause");
}
