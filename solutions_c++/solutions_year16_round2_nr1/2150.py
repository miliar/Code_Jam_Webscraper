#include<iostream>
#include<stdio.h>
#include<map>
using namespace std;

map<char, int> a;

int main()
{freopen ("A-large.in", "r", stdin);
   freopen ("A-large.out", "w", stdout);
int i,cnt[1<<10],j,t;
cin>>t;
for(int tt=1;tt<=t;tt++)
{  
   string s;
   cin>>s;
   
 
   
   for(i=0;i<26;i++)
   {
      a[i+'a']=0;
   }
   
   for(i=0;i<s.length();i++)
   {
      s[i]=s[i]-'A';
      s[i]+='a';
      a[s[i]]++;
   }
   //cout<<s<<endl;
   
   cnt[0]=a['z'];
   a['e']-=a['z'];
   a['r']-=a['z'];
   a['o']-=a['z'];
   a['z']-=a['z'];
   
   cnt[2]=a['w'];
   a['t']-=a['w'];
   a['o']-=a['w'];
   a['w']-=a['w'];
     
   cnt[4]=a['u'];
   a['f']-=a['u'];
   a['o']-=a['u'];
   a['r']-=a['u'];
   a['u']-=a['u'];
   
   cnt[5]=a['f'];
   a['i']-=a['f'];
   a['v']-=a['f'];
   a['e']-=a['f'];
   a['f']-=a['f'];
   
   cnt[6]=a['x'];
   a['s']-=a['x'];
   a['i']-=a['x'];
   a['x']-=a['x'];

   cnt[7]=a['s'];
   a['e']-=a['s'];
   a['v']-=a['s'];
   a['e']-=a['s'];
   a['n']-=a['s'];
   a['s']-=a['s'];
   
   cnt[8]=a['g'];
   a['e']-=a['g'];
   a['i']-=a['g'];
   a['h']-=a['g'];
   a['t']-=a['g'];
   a['g']-=a['g'];
   
   cnt[9]=a['i'];
   a['n']-=a['i'];
   a['n']-=a['i'];
   a['e']-=a['i'];
   a['i']-=a['i'];
   
   cnt[1]=a['o'];
   a['n']-=a['o'];
   a['e']-=a['o'];
   a['o']-=a['o'];
   
   cnt[3]=a['t'];
   a['h']-=a['t'];
   a['r']-=a['t'];
   a['e']-=a['t'];
   a['e']-=a['t'];
   a['t']-=a['t'];
   

   cout<<"Case #"<<tt<<": ";
   for(i=0;i<10;i++)
   {
      //cout<<cnt[i]<<endl;
      for(int j=1;j<=cnt[i];j++)
      {
         printf("%d",i);
      }

   }      cout<<endl;
}

  // system("pause");
   return 0;
}