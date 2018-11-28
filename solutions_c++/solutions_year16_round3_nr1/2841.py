#include<bits/stdc++.h>
using namespace std;

void open()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
}
int main()
{
    //open();
    long long int T,N;
    scanf("%lld",&T);
    for(int t=1;t<=T;t++)
    {
       scanf("%lld",&N);
       long long int arr[N],sum=0;
       for(int i=0;i<N;i++)
       {
           scanf("%lld",&arr[i]);
           sum+=arr[i];
       }
       string str="";
       while(sum>0)
       {
           long long int flag=0,fmax=-999,smax=-999,fpos,spos;
           for(int i=0;i<N;i++)
           {
               if(arr[i]>fmax)
               {
                   fpos=i;
                   fmax=arr[i];
               }
           }
           for(int i=0;i<N;i++)
           {
               if(arr[i]>smax && i!=fpos)
               {
                   spos=i;
                   smax=arr[i];
               }
           }
           if(fmax-smax>=2)
            {
              char ch=fpos+65;
              str+=ch;
              str+=ch;
              str+=" ";
              arr[fpos]--;arr[fpos]--;
              }
              else if(fmax==1 && smax==1 && sum>2)
              {
                  char ch1=fpos+65;
                  str+=ch1;
                  str+=" ";
                  flag=1;
                  arr[fpos]--;
              }
          else{
                char ch1=fpos+65;
                char ch2=spos+65;
                str+=ch1;
                if(smax!=0)
                str+=ch2;
                str+=" ";
                arr[fpos]--;
                arr[spos]--;
          }
          sum-=2;
          if(flag==1)
            sum++;

       }
       printf("Case #%d: ",t);
       cout<<str<<endl;
    }
    return 0;
}
