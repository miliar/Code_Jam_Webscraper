#include<bits/stdc++.h>

using namespace std;

string s;

int main()
{
    #ifdef akid
    freopen("input.txt","r",stdin);
    freopen("out.txt","w",stdout);
    #endif // akid

    int t,cas=1;
    scanf("%d",&t);
    while(t--)
    {
        cin>>s;

        int len=s.size();

        string s1="";
        s1+=s[0];
        for(int i=1;i<len;i++)
        {
            if(s[i]>=s1[0])
            {
                string ss="";
                ss+=s[i];
                //cout<<ss<<endl;
                ss+=s1;
                s1=ss;
                //cout<<s<<endl;
            }
            else{
                string ss="";
                ss+=s[i];
                s1+=ss;
            }
        }
        printf("Case #%d: ",cas++);
        cout<<s1<<endl;
    }
    return 0;
}
