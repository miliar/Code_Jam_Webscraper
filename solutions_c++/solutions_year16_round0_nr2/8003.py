#include<bits/stdc++.h>
using namespace std;

int main()
{
        int t,ca=1;
        cin>>t;
        while(t--)
        {
            string s;
            cin>>s;
            int ans=0;
            int flip=0;
            for(int i=s.size()-1;i>=0;i--)
            {
                if(flip==0)
                {
                    if(s[i]=='-')
                    {
                        ans++;
                        flip=1;
                    }

                }
                else
                {

                    if(s[i]=='+')
                    {
                        ans++;
                        flip=0;
                    }
                }
            }
            cout<<"Case #"<<ca++<<": "<<ans<<endl;

        }


    return 0;
}
