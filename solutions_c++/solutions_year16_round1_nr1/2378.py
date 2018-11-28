#include <bits/stdc++.h>
using namespace std;
int main()
{
    int t;
    cin>>t;
    int pp=1;
    while(t--)
    {
        char s[1005];
        cin>>s;
        string str;
        int i;
        int l=strlen(s);
        str.push_back(s[0]);
        for(i=1;i<l;i++)
        {
            if(s[i]<str[0])
            {
                str.push_back(s[i]);
            }
            else
            {
                string temp;
                temp.push_back(s[i]);
                temp.append(str);
                str=temp;
            }
        }
        cout<<"Case #"<<pp<<": "<<str<<"\n";
        pp++;
    }
	return 0;
}
