#include<iostream>
#include<stdio.h>
#include<algorithm>
#include<vector>
#include<iomanip>
using namespace std;



int main()
{
    freopen("output.txt","w",stdout);
    freopen("input.txt","r",stdin);

    int ts,t;
    cin>>t;
    
    for(ts=1;ts<=t;ts++){
         int n,i,j;
         cin>>n;
         int arr[n][205];
         for(i=0;i<n;i++)for(j=0;j<205;j++)arr[i][j]=0;
         int chars[n];
         char str[205];
         int k;
         getchar();
         for(i=0;i<n;i++)
         {
             cin.getline(str,105,'\n');
             //cout<<str<<'\n';
             k=1;
             arr[i][1]=str[0];arr[i][2]=1;
             for(j=1;str[j]!='\0';j++)
             {if(str[j]==str[j-1])arr[i][k*2]++;
              else {k++;arr[i][2*k-1]=str[j];arr[i][2*k]=1;}
             } 
             chars[i]=k;
         }
         //cout<<arr[0];
         //cout<<arr[1];
         int flag=1;
         for(i=1;i<n;i++)if(chars[0]!=chars[i]){cout<<"Case #"<<ts<<": Fegla Won\n";flag=0;break;}
         if(flag==0)continue;
         int ans=0;
         for(i=1;i<=k;i++){
                            int x=arr[0][2*i];
                            int lm=0;
                            for(j=1;j<n;j++){ if(arr[j][2*i-1]!=arr[0][2*i-1]){cout<<"Case #"<<ts<<": Fegla Won\n";flag=0;break;}
                                              else x+=arr[j][2*i];
                                              }
                            if(flag==0)break;
                            x/=n;
                            for(j=0;j<n;j++){ if(arr[j][2*i]>x)lm+=arr[j][2*i]-x;else lm+=x-arr[j][2*i];
                                              }
                            ans+=lm;
                          }
         if(flag==0)continue;
         cout<<"Case #"<<ts<<": "<<ans<<'\n';
    }
    
    

}
