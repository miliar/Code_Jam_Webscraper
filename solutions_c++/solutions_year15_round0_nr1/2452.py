#include <bits/stdc++.h>
using namespace std;


int main()
{
    long long int temp=0,i,ans=0,shy=0,cnt=0;
    char str[1100];
    int t,k=1;
    cin>>t;
    while(t--)
    {
        ans=0;
        cnt=0;
        cin>>shy;
        scanf("%s",str);
       // cout<<"mayank"<<endl;

        cnt=cnt+(str[0]-'0');
       // cout<<cnt<<endl;
        for(i=1;i<strlen(str);i++)
        {
            temp=str[i]-'0';
            if(cnt>=i)
                cnt+=temp;
            else
            {
                ans+=(i-cnt);
                cnt+=(i-cnt);
                cnt+=temp;
            }
        //    cout<<" ans cnt "<<ans<<"    "<<cnt<<endl;
        }
      //  cout<<"bahar nikal"<<endl;
        cout<<"Case #"<<k<<": "<<ans<<"\n";
        k++;
    }

    return 0;
}
