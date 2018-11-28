#include<bits/stdc++.h>
#define f_in(st) freopen(st,"r",stdin);
#define f_out(st) freopen(st,"w",stdout);
using namespace std;

int main()
{
    f_in("in3.txt");
    f_out("out.txt");
    int T;
    cin>>T;
     for(int t=0;t<T;t++){
      int N;
      cin>>N;
      char s[1004];
      cin>>s;
      int sum=s[0]-'0';
      int ans=0;
      int len=strlen(s);
      for(int i=1;i<len;i++)
      {
          if(sum < i && s[i]-'0'>0)
          {
                 ans+=(i-sum);
                 sum+=(i-sum);
          }
          sum+=s[i]-'0';
      }
      cout<<"Case #"<<t+1<<": "<<ans<<endl;
    }
    //fclose(stdout);
    return 0;
}
