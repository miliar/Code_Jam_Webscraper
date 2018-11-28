#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main()
{
    //cout << "Hello world!" << endl;
    freopen("B-large.in","rt",stdin);
	freopen("outlarge.out","wt",stdout);
    int t;
    cin>>t;
    for(int i=1;i<=t;i++)
    {
        string s;
        cin>>s;
        int len=s.length();int cnt=0,top=0;;
        for(int j=len-1;j>=0;j--)
        {
            if(cnt%2==0)
            {
                if(s[j]=='-')
                {
                    top++;cnt++;
                }
            }
            else
            {
                if(s[j]=='+')
                {
                    top++;
                    cnt++;
                }
            }
        }
        cout<<"Case #"<<i<<": "<<top<<"\n";
    }
    return 0;
}
