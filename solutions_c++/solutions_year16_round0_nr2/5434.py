#include<bits/stdc++.h>
using namespace std;

main()
{
    int t,n;
    cin>>t;
    string s[t];
    char s1;
    for(int i = 0; i < t; ++i)
    {
        cin>>s[i];
    }
    for(int i = 0; i < t; ++i)
    {
        s1 = '-';n=0;
        for(int j = 0; j < s[i].length(); j++)
        {
            if(s[i][j]=='-'&&s1=='-'&&j!=0)
                continue;
            else if(s[i][j]=='-'&&s1=='+')
                n+=2;
            else if(s[i][j]=='-')
                n++;
            s1 = s[i][j];
        }
        cout<<"Case #"<<i+1<<": "<<n<<endl;
    }
}
