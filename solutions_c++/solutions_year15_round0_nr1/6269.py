#include<iostream>
#include<stdio.h>
using namespace std;
#include<string.h>
int main()
{
    #ifndef ONLINE_JUDGE
        freopen("input1.cpp","r",stdin);
        freopen("output1.cpp","w",stdout);
    #endif // ONLINE_JUDGE
    int t;
    cin>>t;
    int j=1;
    while(t--)
    {
        int s;
        cin>>s;
        char str[s+1];
        cin>>str;
        int l=strlen(str);
        int count=0;
        int z=0,i;
        if(str[0]=='0')
        {
            z=1;
            count=1;
        }
        else
        {
            count+=str[0]-48;
        }
      //  cout<<count<<" "<<z<<endl;
        for(i=1;i<l;i++)
        {
            if(str[i]!='0')
            {
                if(i<=count)
                {
                    count+=str[i]-48;
                }
                else
                {
                    z+=i-count;
                    count+=i-count;
                    count+=str[i]-48;
                }
            }
        //    cout<<count<<" "<<z<<endl;
        }
        cout<<"Case #"<<j++<<": "<<z<<endl;
    }
    return 0;
}
