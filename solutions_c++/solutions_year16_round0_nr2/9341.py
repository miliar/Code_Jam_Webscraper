#include<iostream>
using namespace std;
#include<cstdio>
#include<string.h>
int main()
{
    int t;
    	freopen("B-large (1).in","rt",stdin);
	freopen("abhinavOutput.cpp","wt",stdout);
    cin>>t;
    int tc=1;
    while(t--)
    {
        char ch[100];
        scanf("%s",ch);
        int c=strlen(ch);
        int cnt=0;
        int ans=0;
        int j=0;
        char ch1[2]={'+','-'};
        for(int i=0;i<c;)
        {
           cnt=0;
              while(ch[i]==ch1[j])
              {
                  i++;
                  j++;
                  cnt++;
              }
            if (j == 2)
            {
                j = 0;
                ans++;
                i--;
            }
              else
                i++;

        }
         //cout<<ans<<endl;
         if(ch[0]=='+')
         {
             cout<<"Case #"<<tc<<": "<<ans*2<<endl;
         }
         else if(ch[0]=='-')
         {   ans=ans*2;
             ans++;
             cout<<"Case #"<<tc<<": "<<ans<<endl;
         }
      tc++;
    }
}

