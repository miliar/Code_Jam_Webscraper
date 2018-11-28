#include <bits/stdc++.h>
using namespace std;
long long range  = (1<<16);
long long a[20];
vector<long long> v[17];
vector<long long>::iterator it;

void precompute()
{
  for(long long i = 1;i<=range ; i++)
    { 
       long long temp = i,j=0, a[20];

       while(temp)
       {
         a[j++]  = temp%2;
         temp/=2;
       }

       if(a[0]==1&&a[j-1]==1)
        v[j].push_back(i);

    }
}

bool check(long long n)
{
  if(n==1||n==0)
    return false;

  for(long long i=2;i*i<=n;i++)
  {
    if(n%i==0)
      return false;
  }
  return true;
}

int main()
{  
  precompute();
  long long t;
  #ifndef ONLINE_JUDGE
      freopen("input.txt","r",stdin);
      // freopen("output.txt","w",stdout);
    #endif
  cin>>t;
  cout<<"Case #1:"<<endl;

  while(t--)
  {
     long long n,k,p=0; long long ans[20];
     cin>>n>>k;

     for( it=v[n].begin();it!=v[n].end();it++)
      {
          long long d = *it;long long a[20],i=0;

          while(d)
          {
            a[i++] = d%2;
            d/=2;
          }

          long long count=0;

          for(long long base=2;base<=10;base++)
          {  
               
            long long number =0,pro=1;

            for(long long j = i-1 ;j>=0;j--)
              {
                    number+=a[j]*(base-1)*pro;
                    pro = base*pro;
              }

             // cout<<number<<" ";


            if(check(number)==false)
            {
              ans[base] = number;
              count++;
            }
            else
              break;
          }

          //cout<<count<<" ";

          if(count==9)
          {
            for(long long j =0;j<i;j++)
              cout<<a[j];
              cout<<" ";

            for(long long j=2;j<=10;j++)
            {  //cout<<ans[j]<<" ";
                for(long long o=2;o*o<=ans[j];o++)
                {
                  if(ans[j]%o==0)
                    { cout<<o<<" ";
                       break;
                     }
                }
            }

            cout<<endl;
            k--;
            
          }

          if(k==0)
            break;

  }

  
 }

  return 0;
}