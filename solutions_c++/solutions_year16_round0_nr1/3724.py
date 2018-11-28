#include<bits/stdc++.h>
using namespace std;
int arr[10000000]={0};
int main()
{
      long long int t,n;
      
      int hash[100]={0},o=0;
      
      scanf("%lld",&t);
      
      while(t--)
      {
            o++;
            
            int pos=0;
            
            scanf("%lld",&n);
            
            for(int i=0;i<=10;i++)
            hash[i]=0;
            
            if(n==0)
            {
                  printf("Case #%d: INSOMNIA\n",o);
                  continue;
                  
            }
            
            long long int tmp=n,flg=0;
            
            while(tmp)
            {
                  arr[pos++]=tmp%10;
                  hash[tmp%10]=1;
                  tmp/=10;
            }
            while(1)
            {
                  
            flg=0;
            
            for(int i=0;i<10;i++)
            if(hash[i]==0)
            flg=1;
            
            if(flg==0)
            break;
            
            tmp=n;
            int carry=0;
            for(int i=0;i<pos;i++)
            {
                  arr[i]+=tmp%10;
                  arr[i]+=carry;
                  tmp/=10;
                  carry=arr[i]/10;
                  arr[i]%=10;
            }
            while(carry)
            {
                  arr[pos++]=carry%10;
                  carry/=10;
            }
            for(int i=0;i<pos;i++)
            if(hash[arr[i]]==0)
            hash[arr[i]]++;
            }
            printf("Case #%d: ",o);
            for(int i=pos-1;i>=0;i--)
            printf("%d",arr[i]);
            printf("\n");
      }
}