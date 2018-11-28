#include <bits/stdc++.h>
using namespace std;
//ios_base::sync_with_stdio(false);
#ifdef CORLEONE
  #define d(b) cerr<< #b << " " << b << endl
  #else
  #define d(b)
#endif

int main()
{
   freopen("one.in","r",stdin);
   freopen("one.txt","w",stdout);
  int test;
  cin>>test;
  for(int rr=1;rr<=test;rr++)
  {
    int n; 
    string s;
    cin>>n>>s;
    // cout<<s<<"\t\t\t\t\t\t\t\t\t ";
    int l = s.size();
    int a[l];
    long long count=0, sum=0;
    for(int i=0;i<l;i++){
      a[i] = s[i]-'0';
    }
    sum+=a[0];
    for(int i=1;i<l;i++){
      if(i>sum && a[i]>0) 
        {
          count += (i-sum);
          sum+=count+a[i];
          // sum += a[i]-sum ;
        }
      else
        sum+=a[i];
       // cout<<sum<<" ";

    }
    cout<<"Case #"<<rr<<": "<<count<<endl;
  }

}