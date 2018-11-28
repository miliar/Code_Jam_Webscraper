#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
        int t,r=1;
        string s;
        cin>>t;
        while(t--)
        {
            int c=0;
                cin>>s;
                int l=s.length();
                for(int i=l-1;i>=0;i--)
                {
                    if(s[i]=='-')
                    {
                        c++;
                        for(int j=i;j>=0;j--)
                        {
                            if(s[j]=='-')
                                s[j]='+';
                            else
                                s[j]='-';
                        }
                    }
                }
                cout<<"Case #"<<r<<": "<<c<<endl;
                r++;
        }
    return 0;
}
