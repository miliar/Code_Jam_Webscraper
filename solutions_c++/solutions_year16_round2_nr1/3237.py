#include<bits/stdc++.h>
#define ll long long int
using namespace std;
 
int main() {
  // your code goes here
ll t,j,flag,i,j1,k,c;
  cin>>t;
  j1=0;
  char digits[10][100]={"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
  while(t--)
  {
      j1++;
      c=0;
      char s[4000];
     cout<<"Case #"<<j1<<": ";
     cin>>s;
     int pos[strlen(s)+5];
     int push1[strlen(s)+5];
      for(j=0;j<strlen(s);j++)
      pos[j]=0;
      int c1=0,c2=0,c3=0,c4=0,c5=0,c6=0,c7=0,c8=0,c9=0,c10=0;
      for(j=0;j<strlen(s);j++)
      {
          if(s[j]=='Z')
          c1++;
          if(s[j]=='X')
          c2++;
          if(s[j]=='G')
          c3++;
          if(s[j]=='H')
          c4++;
          if(s[j]=='U')
          c5++;
          if(s[j]=='W')
          c6++;
          if(s[j]=='F')
          c7++;
          if(s[j]=='V')
          c8++;
          if(s[j]=='I')
          c9++;
          if(s[j]=='O')
          c10++;
      }
      char str2[]="SIX";
      for(i=1;i<=c2;i++)
      {
          for(k=0;k<strlen(str2);k++)
          {
              for(j=0;j<strlen(s);j++){
              if((str2[k]==s[j])&&(pos[j]==0))
              { pos[j]=1;
              // cout<<s[j];
                 break;
              }}
          }
      }
      char str1[]="ZERO";
      for(i=1;i<=c1;i++)
      {
          for(k=0;k<strlen(str1);k++)
          {
              for(j=0;j<strlen(s);j++){
              if((str1[k]==s[j])&&(pos[j]==0))
              { pos[j]=1;
                 break;
              }}
          }
      }
       char str3[]="EIGHT";
      for(i=1;i<=c3;i++)
      {
          for(k=0;k<strlen(str3);k++)
          {
              for(j=0;j<strlen(s);j++){
              if((str3[k]==s[j])&&(pos[j]==0))
              { pos[j]=1;
                 break;
              }}
          }
      }
       char str4[]="THREE";
      for(i=1;i<=c4-c3;i++)
      {
          for(k=0;k<strlen(str4);k++)
          {
              for(j=0;j<strlen(s);j++){
              if((str4[k]==s[j])&&(pos[j]==0))
              { pos[j]=1;
                 break;}
              }
          }
      }
      char str5[]="FOUR";
      for(i=1;i<=c5;i++)
      {
          for(k=0;k<strlen(str5);k++)
          {
              for(j=0;j<strlen(s);j++){
              if((str5[k]==s[j])&&(pos[j]==0))
              { pos[j]=1;
              // cout<<s[j];
                 break;}
              }
          }
      }
       char str6[]="TWO";
      for(i=1;i<=c6;i++)
      {
          for(k=0;k<strlen(str6);k++)
          {
              for(j=0;j<strlen(s);j++){
              if((str6[k]==s[j])&&(pos[j]==0))
              { pos[j]=1;
              // cout<<s[j];
                 break;}
              }
          }
      }
       char str7[]="FIVE";
      for(i=1;i<=c7-c5;i++)
      {
          for(k=0;k<strlen(str7);k++)
          {
              for(j=0;j<strlen(s);j++){
              if((str7[k]==s[j])&&(pos[j]==0))
              { pos[j]=1;
              // cout<<s[j];
                 break;}
              }
          }
      }
      char str8[]="SEVEN";
      for(i=1;i<=c8-c7+c5;i++)
      {
          for(k=0;k<strlen(str8);k++)
          {
              for(j=0;j<strlen(s);j++){
              if((str8[k]==s[j])&&(pos[j]==0))
              { pos[j]=1;
              // cout<<s[j];
                 break;}
              }
          }
      }
       char str9[]="NINE";
      for(i=1;i<=c9-(c2+c3+c7-c5);i++)
      {
          for(k=0;k<strlen(str9);k++)
          {
              for(j=0;j<strlen(s);j++){
              if((str9[k]==s[j])&&(pos[j]==0))
              { pos[j]=1;
              // cout<<s[j];
                 break;}
              }
          }
      }
       char str10[]="ONE";
      for(i=1;i<=c10-(c1+c5+c6);i++)
      {
          for(k=0;k<strlen(str10);k++)
          {
              for(j=0;j<strlen(s);j++){
              if((str10[k]==s[j])&&(pos[j]==0))
              { pos[j]=1;
              // cout<<s[j];
                 break;}
              }
          }
      }
     for(i=0;i<10;i++)
     {
         c=0;
         if(i==0)
         {
             for(j=1;j<=c1;j++)
             cout<<i;
             continue;
         }
         else
          if(i==6)
         {
             for(j=1;j<=c2;j++)
             cout<<i;
             continue;
         }
         else
          if(i==8)
         {
             for(j=1;j<=c3;j++)
             cout<<i;
             continue;
         }
         else
          if(i==3)
         {
             for(j=1;j<=c4-c3;j++)
             cout<<i;
             continue;
         }
         else
         if(i==4)
         {
             for(j=1;j<=c5;j++)
             cout<<i;
             continue;
         }
         else
         if(i==1)
         {
             for(j=1;j<=c10-(c1+c5+c6);j++)
             cout<<i;
             continue;
         }
          else
         if(i==9)
         {
             for(j=1;j<=c9-(c2+c3+c7-c5);j++)
             cout<<i;
             continue;
         }
          else
         if(i==7)
         {
             for(j=1;j<=c8-c7+c5;j++)
             cout<<i;
             continue;
         }
         else
         if(i==5)
         {
             for(j=1;j<=c7-c5;j++)
             cout<<i;
             continue;
         }
          else
         if(i==2)
         {
             for(j=1;j<=c6;j++)
             cout<<i;
             continue;
         }
        
     }
     
      cout<<"\n";
      
  }
  return 0;
}
 