#include <bits/stdc++.h>
using namespace std;
#define ll long long int

long long int factor(long long int x)
{
    ll i;
    for(i=2;i<=sqrt(x)+1;i++)
    {
        if(x%i==0)
        {
            return i;
        }
    }
    return 0;
    
}


int main() {
    freopen("C-small-attempt0.in","r",stdin);
    freopen("output.out","w",stdout);
	
	int t;
    cin>>t;
    while(t--)
    {
        cout<<"Case #1:"<<endl;
        
        int i,j,n,k;
        cin>>n>>k;
        int p=0;
        for(i=0;i<16384 && p!=50;i++)
        {
            
            int temp=i;
            temp<<=1;
            temp+=1;
            temp=temp | (1<<15);
            
            long long int arr[11]={0};
            for(j=2;j<=10;j++)
            {
                
                
                for(k=0;k<16;k++)
                {
                    if(temp & (1<<k))
                    {
                        arr[j]+=(pow(j,k));
                    }
                }
                if(!factor(arr[j]))
                {
        
                    break;
                }
                
            }
            if(j==11)
            {
                p++;
                for(j=15;j>=0;j--)
                {
                    if(temp & (1<<j))
                    cout<<1;
                    else
                    cout<<0;
                }
                cout<<" ";
                for(j=2;j<=10;j++)
                {
                    cout<<factor(arr[j])<<" ";
                }
                cout<<endl;
            }
        }
    
    }
	return 0;
}

