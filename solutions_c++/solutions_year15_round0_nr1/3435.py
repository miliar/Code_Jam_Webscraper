    #include <iostream>
    using namespace std;
     
    int main() {
     
    int t;
    cin>>t;
     
    for(int j=1;j<=t;j++)
    {
    int smax;
    int ans=0;
    cin>>smax;
    char s[1005];
    int sum=0;
    cin>>s;
    for(int i=0;i<=smax;i++)
    {
    if((s[i]-48)>0)
    {
    if(sum<i)
      {ans+=i-sum;
      sum+=i-sum+s[i]-48;
      }
    else
     sum+=s[i]-48;
    }
    }
    cout<<"Case #"<<j<<": "<<ans<<"\n";
    }
    }


