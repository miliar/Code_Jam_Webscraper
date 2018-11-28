#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<map>
#include<string>
#include<utility>
#include<fstream>
using namespace std;

int change[100003];

int main()
{
    int arr[][5] = {0,0,0,0,0,
                    0,1,2,3,4,
                    0,2,1,4,3,
                    0,3,4,1,2,
                    0,4,3,2,1};
    int sign[][5] = {0,0,0,0,0,
                     0,1,1,1,1,
                     0,1,-1,1,-1,
                     0,1,-1,-1,1,
                     0,1,1,-1,-1};
   /* cout<<"\n donw \n";
    for(int it=0;it<5;it++)
    {
          for(int j=0;j<5;j++)cout<<arr[it][j]<<" ";cout<<endl;
          }
    cout<<"\n donw 22222222\n";
    for(int it=0;it<5;it++)
    {
          for(int j=0;j<5;j++)cout<<sign[it][j]<<" ";cout<<endl;
          }
    */ifstream f1;
    ofstream f2;
    f1.open("C-small-attempt0.in");
    f2.open("output.out");
    int c=1,t,l,x,temp;
    string str;
    string test;
    f1>>t;
    while(c<=t)
    {
               f1>>l>>x;
               f1>>str;
              // cout<<"\n l : "<<l<<" , x : "<<x<<" , wrth str : "<<str<<endl;
               test = "";
               for(int i=0;i<x;i++)test+=str;
               //cout<<"\n full str : "<<test<<endl;
               l = test.size();
               for(int i=0;i<l;i++)
               {
                       if(test[i]=='i')change[i]=2;
                       else if(test[i]=='j')change[i]=3;
                       else change[i]=4;
                       }
               //cout<<"\n change : ";
               //for(int i=0;i<l;i++)cout<<change[i]<<" ";cout<<endl; 
               int ans = 0;
               int i_p = -1;
               int j_p = -1;
               int k_p = -1;
               int fac = 1;
               if(change[0]==2){ans=2;i_p=0;}
               else if(change[0]==3)ans=3;
               else ans= 4;
               
               
               for(int i=0;i<l-1;i++)
               {
                       temp = arr[ans][change[i+1]];
                 //      cout<<"\n temp : arr["<<ans<<"]["<<change[i+1]<<"] = "<<arr[ans][change[i+1]]<<endl;
                       fac = fac * sign[ans][change[i+1]];
                       if(temp*fac==2)i_p = i+1;
                       else if(temp*fac==4)j_p = i+1;
                       ans = temp;
                       }
               if(ans*fac==-1)k_p = l-1;
               //cout<<"\n ans comes ot : "<<ans*fac<<endl;
               //cout<<"\n i-p = "<<i_p<<" , j_p "<<j_p<<" k  "<<k_p<<endl;
               f2<<"Case #"<<c++<<": ";
               
               if(i_p==-1 || j_p==-1 || k_p==-1)f2<<"NO\n";
               else if(i_p>=0 && j_p >= 0 && j_p<l && k_p <l && ans*fac==-1)f2<<"YES"<<endl;
               else f2<<"NO\n";
               }
    f1.close();
    f2.close();
    return 0;
    }
