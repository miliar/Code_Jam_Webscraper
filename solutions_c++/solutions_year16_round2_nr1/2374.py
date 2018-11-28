#include<bits/stdc++.h>
using namespace std;
int main()
{
  int t;
  cin>>t;
  char str[2005];
   int arr[26];
   int cnt[10];  
   for(int k=1;k<=t;k++)
  {
    scanf("%s",str);
    int l=strlen(str);
    memset(arr,0,sizeof(arr));
   int i;  
  for(i=0;i<l;i++)
     {
        arr[str[i]-'A']++;
     }
    memset(cnt,0,sizeof(cnt));
    cnt[0]=arr[25];
    arr['E'-'A']-=arr[25];
    arr['R'-'A']-=arr[25];
    arr['O'-'A']-=arr[25];
    arr[25]=0;
    cnt[2]=arr[22];
    arr['T'-'A']-=arr[22];
    arr['O'-'A']-=arr[22];
    arr[22]=0;
    cnt[8]=arr[6];
    arr['E'-'A']-=arr[6];
    arr['I'-'A']-=arr[6];
    arr['H'-'A']-=arr[6];
    arr['T'-'A']-=arr[6];
    arr[6]=0;
    cnt[6]=arr[23];
    arr['S'-'A']-=arr[23];
    arr['I'-'A']-=arr[23];
    arr[23]=0;
    cnt[3]=arr[7];
    arr['T'-'A']-=arr[7];
    arr['R'-'A']-=arr[7];
    arr['E'-'A']-=2*arr[7];
    arr[7]=0;
    cnt[4]=arr['R'-'A'];
    arr['F'-'A']-=cnt[4];
    arr['O'-'A']-=cnt[4];
    arr['U'-'A']-=cnt[4];
    arr['R'-'A']=0;
    cnt[5]=arr['F'-'A'];
    arr['I'-'A']-=cnt[5];
    arr['V'-'A']-=cnt[5];
    arr['E'-'A']-=cnt[5];
    arr['F'-'A']=0;
    cnt[7]=arr['S'-'A'];
    arr['E'-'A']-=2*cnt[7];
    arr['V'-'A']-=cnt[7];
    arr['N'-'A']-=cnt[7];
    arr['S'-'A']=0;
    cnt[1]=arr['O'-'A'];
    cnt[9]=arr['I'-'A'];
      cout<<"Case #"<<k<<": ";
     for(i=0;i<=9;i++)
      {
         for(int j=1;j<=cnt[i];j++)
            cout<<i;
      }
      cout<<endl;
  }
  return 0;
}