#include<bits/stdc++.h>
#define read(tag) freopen(tag,"r",stdin)
#define rite(tag) freopen(tag,"w",stdout)
using namespace std;

int main()
{
    //read("read.in");
    //rite("Ans.out");
    int right=0,left=0,ans=0,T;
    cin>>T; string str;

    for(int i=1;i<=T;i++)
    {
        cin>>str;
        right=0,left=0,ans=0;

        while(!str.empty())
        {
            while(str[str.length()-1]=='+') str.erase(str.begin()+str.length()-1);
            if(str.empty()) break;
            for(int i=0;i<str.length();i++)
            {
                if(str[i]=='+') str[i]='-';
                else str[i]='+';
            }
            ans++; right=0; left=0;
            for(int i=str.length()-1;i>=0;i--)
            {
                if(str[i]=='+') right++;
                else break;
            }
            for(int i=0;i<str.length();i++)
            {
                if(str[i]=='+') left++;
                else break;
            }
            if(left>right)
            {
                string temp=str;
                for(int i=str.length()-1,j=0;i>=0;i--,j++) str[j]=temp[i];
            }
        }
        cout<<"Case #"<<i<<": "<<ans<<endl;
    }
    return 0;
}
