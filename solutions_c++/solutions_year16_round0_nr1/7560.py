#include<iostream>
using namespace std;
int solve(int *arr,int r,int p)
{
    int count=0;
    for(int i=0;i<p;i++)
    {
        if(arr[i]==r)
            count++;
    }
    if(count>0)
        return 0;
    
    else
        return 1;
}

int main()
{
    long long int n,m,t,u;
    cin>>t;
    u=t;
    while(t>0){
        long long int kl;
        int arr[20];
        cin>>n;
        m=n;
        kl=n;
        int j=1,r,k=0,p=0;
        
        while(1 && n!=0)
        {
            while(n>0)
            {
                r=n%10;
                n=n/10;
                if(solve(arr,r,p)==1)
                {
                    arr[p]=r;
                    p++;
                }
                
            }
            
            
            if(p==10)
            {
                k=1;
                break;
            }
            
            else
            {  j++;
                n=(j)*m;
                kl = n;
                
            }
            
        }
        
        if(k==1)
            cout<<"Case #"<<u-t+1<<": "<<kl<<endl;
        
        else
            cout<<"Case #"<<u-t+1<<": "<<"INSOMNIA"<<endl;
        t--;
    }
    
    return 0;
}