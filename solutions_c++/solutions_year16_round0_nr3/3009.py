#include<bits/stdc++.h>
using namespace std;
bool sieve[1000001];
vector<int> prime;
vector<int> v;
long long pow(int a, int b)
 {
long long x=1,y=a;
    while(b>0)
        {
        if(b%2==1)
            x=(x*y);
        y=(y*y);
        b/=2;
    }
    return x;
}
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    bool flag,flag2;
    int t,n,j;
    scanf("%d%d%d",&t,&n,&j);
      for(int i=2;i<=1000;i++)
    {
        if(!sieve[i])
        {
            prime.push_back(i);
            for(int j=i*i;j<=1000000;j+=i)
                sieve[j]=true;
        }
    }
    printf("Case #1:");
    int c=0;
    for(int i=pow(2,15);i<pow(2,16);i++)
    {
        if(i%2)
        {
        flag2=false;
        v.clear();
        for(int j=2;j<=10;j++)
        {
            flag=false;
            int tmp=i,count=0;
            long long p=0;
            while(tmp)
            {
                p+=((tmp%2)*pow(j,count));
                tmp/=2;
                count++;
            }
            for(int k=0;k<prime.size();k++)
            {
                if(p%prime[k]==0&&prime[k]<p)
                {
                    v.push_back(prime[k]);
                    flag=true;
                    break;
            }
            }
            if(flag==false)
            {
                flag2=true;
                break;
            }
        }
        if(flag2==false)
        {
        string str="";
        int tmp=i;
        while(tmp)
        {
            str+=((tmp%2)+'0');
            tmp/=2;
        }
        reverse(str.begin(),str.end());
        cout<<"\n"<<str<<" ";
        for(int k=0;k<v.size();k++)
            cout<<v[k]<<" ";
           c++;
        if(c>=50)
           break;
        }
        }
    }
return 0;
}
