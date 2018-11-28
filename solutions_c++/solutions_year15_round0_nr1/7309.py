#include<bits/stdc++.h>
using namespace std;
int n,a,b,c,t;

char ch[10004];

int main()
{
  
  cin >> t;
  for(int k=0;k<t;k++)
  {
    cin >> n;
    cin >> ch;
    long long int sum=0,cnt=0,temp1=0;
    for(int i=0;i<n+1;i++)
    {
       int temp = ch[i]-'0';
       sum+=temp;
       if(sum<i+1)
       {
         cnt=(i+1-sum);
         sum+=cnt;
         temp1+=cnt;
       }
    }

    cout<<"Case #"<<k+1<<": "<<temp1<<endl;

  }
  return 0;
}