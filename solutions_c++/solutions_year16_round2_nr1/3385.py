#include <bits/stdc++.h>
#define pb push_back
using namespace std;
int main()
{
    int t,ans,ca,i,j;
    vector<int >v;
    cin>>t;
    for(ca=1;ca<=t;ca++)
    {
      v.clear();
      string s;
      cin>>s;
      int freq[26];
      memset(freq,0,sizeof(freq));
      for(i=0;i<s.size();i++)
      {
        freq[(int)(s[i]-'A')]++;
      }
      //for(i=0;i<26;i++)cout<<freq[i];
      for(i=0;i<freq[25];i++)v.pb(0);
      int a=freq[25];freq[25]-=a;freq[4]-=a;freq[17]-=a;freq[14]-=a;
      for(i=0;i<freq[22];i++)v.pb(2);
      a=freq[22];freq[19]-=a;freq[22]-=a;freq[14]-=a;
      for(i=0;i<freq[20];i++)v.pb(4);
      a=freq[20];freq[5]-=a;freq[14]-=a;freq[20]-=a;freq[17]-=a;
      for(i=0;i<freq[14];i++)v.pb(1);
      a=freq[14];freq[14]-=a;freq[13]-=a;freq[4]-=a;
      for(i=0;i<freq[5];i++)v.pb(5);
      a=freq[5];freq[5]-=a;freq[8]-=a;freq[21]-=a;freq[4]-=a;
      for(i=0;i<freq[21];i++)v.pb(7);
      a=freq[21];freq[18]-=a;freq[4]-=(2*a);freq[21]-=a;freq[13]-=a;
      for(i=0;i<freq[23];i++)v.pb(6);
      a=freq[23];freq[18]-=a;freq[8]-=a;freq[23]-=a;
      for(i=0;i<freq[6];i++)v.pb(8);
      a=freq[6];freq[4]-=a;freq[8]-=a;freq[6]-=a;freq[7]-=a;freq[19]-=a;
      for(i=0;i<freq[8];i++)v.pb(9);
      a=freq[8];freq[14]-=(2*a);freq[8]-=a;freq[4]-=a;
      for(i=0;i<freq[19];i++)v.pb(3);
      sort(v.begin(),v.end());
      cout<<"Case #"<<ca<<": ";
      for(i=0;i<v.size();i++)
      cout<<v[i];
      cout<<"\n";
    }
	return 0;
}