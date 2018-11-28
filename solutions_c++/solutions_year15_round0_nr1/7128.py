#include<iostream>
using namespace std;


int main()
{
     freopen("standingin.txt", "rt", stdin);
    freopen("standingout.txt", "wt", stdout);

    int t,ca=0;
    scanf("%d",&t);
    
    while(t--)
    {
              int n,i,sum=0,ans=0,count[10001]={0};
              string str;
              cin>>n;
              cin>>str;
              for(i=0;i<str.size();i++)
              {
                                       count[i]=str[i]-'0';
              }  
            
            
              for(i=0;i<str.size();i++)
              {
                                       if(sum<i)
                                       {
                                                count[i]=count[i]+(i-sum);
                                                ans=ans+(i-sum);
                                       }
                                       sum=sum+count[i];
                                  
              }
              printf("Case #%d: %d\n",++ca,ans);
    }
    return 0;
}
