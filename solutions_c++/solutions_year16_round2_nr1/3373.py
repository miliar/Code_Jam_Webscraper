
#include<vector>
#include<algorithm>
#include<string>

#include <iostream>
using namespace std;

int main()
{

  
  int t;
  cin>>t;
  for(int k=1;k<=t;k++)
  {
      string s;
  cin>>s;
 // cout<<s<<" ";
 int final[3000];
 int count[3000];
 for(int p=0;p<2000;p++)
 {
     final[p]=0;
     count[p]=0;
     
 }
  
  int i;
  
  
    for(i=0;i<s.length();i++)
    count[s[i]-'A']++;
     
       //for(i=0;i<s.length();i++)
       //cout<<count[i]<<" ";
      for(int j=0;j<2009;j++)
      {
      if(count[25]>0&&count[4]>0&&count[17]>0&&count[14]>0)
      {
          final[0]++;
          count[25]--;
          count[4]--;
          count[17]--;
          count[14]--;
      }
      }
        for(int j=0;j<2009;j++)
      {
       if(count[18]>0&&count[8]>0&&count[23]>0)
      {
          final[6]++;
          
          count[23]--;
          count[8]--;
          count[18]--;
      }}
        for(int j=0;j<2009;j++)
      {
       if(count[19]>0&&count[22]>0&&count[14]>0)
      {
          final[2]++;
          count[19]--;
          count[22]--;
          count[14]--;
         
      }}
        for(int j=0;j<2009;j++)
      {
      if(count[8]>0&&count[4]>0&&count[6]>0&&count[7]>0&&count[19]>0)
      {
          final[8]++;
          count[8]--;
          count[4]--;
          count[6]--;
          count[7]--;
          count[19]--;
      }}
        for(int j=0;j<2009;j++)
      {
      if(count[19]>0&&count[7]>0&&count[17]>0&&count[4]>1)
      {
          final[3]++;
          count[19]--;
          count[7]--;
          count[17]--;
          count[4]--;
           count[4]--;
          
      }}
        for(int j=0;j<2009;j++)
      {
      if(count[5]>0&&count[14]>0&&count[20]>0&&count[17]>0)
      {
          final[4]++;
          count[14]--;
          count[20]--;
          count[17]--;
          count[5]--;
      }}
        for(int j=0;j<2009;j++)
      {
      if(count[14]>0&&count[13]>0&&count[4]>0)
      {
          final[1]++;
          
          count[4]--;
          count[13]--;
          count[14]--;
      }
      }
     
        for(int j=0;j<2009;j++)
      {
      
      if(count[5]>0&&count[8]>0&&count[21]>0&&count[4]>0)
      {
          final[5]++;
          count[5]--;
          count[8]--;
          count[21]--;
          count[4]--;
      }}
        for(int j=0;j<2009;j++)
      {if(count[18]>0&&count[4]>1&&count[21]>0&&count[13]>0)
      {
          final[7]++;
          count[18]--;
          count[4]--;
           count[4]--;
          count[21]--;
          count[13]--;
      }}
        for(int j=0;j<2009;j++)
      {
       if(count[13]>1&&count[8]>0&&count[4]>0)
      {
          final[9]++;
          count[13]--;
          count[4]--;
          count[13]--;
          count[8]--;
      }
      }
      cout<<"Case #"<<k<<":"<< " ";
      for(i=0;i<11;i++)
      {
          
          for(int l=0;l<final[i];l++)
          cout<<i;
          
          
      }
      
      
      cout<<"\n";
      
  }
  
  
  
  
  
  
    return 0;
}
