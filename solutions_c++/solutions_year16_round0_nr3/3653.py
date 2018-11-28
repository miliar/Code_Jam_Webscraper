#include<bits/stdc++.h>
using namespace std;
inline long long int base(int n,string s)
{
    long long int num=0,mul=1;
    for(int j=s.length()-1;j>=0;j--)
    {
        num+=(s[j]-'0')*mul;
        mul*=n;
        
    }
    return num;
}
inline long long int isprime(long long int n)
{
    long long int x=-1;
    for(int i=2;i*i<=n;i++)
    {
        if(n%i==0)
        {
            x=i;
            break;
        }
    }
    return x;

}
int check(string s,long long int arr[11])
{
    for(int i=2;i<=10;i++)
    {
        long long int x,y;
        x=base(i,s);
        y=isprime(x);
        if(y==-1)
            return -1;
        else
        {
            arr[i]=y;
        }
    }
    return 1;
}
int main()
{
    int t,n,j;
    cin>>t>>n>>j;
    int count=0;
    bool flag=false;
    cout<<"Case #1:"<<endl;
    while(count<=j)
    {
        for(long long int i=0;i< pow(2,n-2);i++)
        {
            bitset<14> a(i);
            string x=a.to_string();
            string s="1"+x+"1";
            long long int arr[11];
            memset(arr,0,sizeof(arr));
            int m=check(s,arr);
            if(m!=-1)
            {
                count++;
                cout<<s<<" ";
                for(int i=2;i<=10;i++)
                {
                    cout<<arr[i]<<" ";
                }
                cout<<endl;
                if(count==j)
                {
                    flag=true;
                    break;
                }
            }
            
        }
        if(flag)
        {
            break;
        }
       
    }
    
    
    
}

