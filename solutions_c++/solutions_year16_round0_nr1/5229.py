#include<bits/stdc++.h>
using namespace std;

int main() 
{
    int x;
    cin>>x;
    for(int no=1;no<=x;no++)
    {
        long int n;
        cin>>n;
        if(n==0)
        {cout<<"Case #"<<no<<": INSOMNIA"<<endl; continue;}
        
        int a[10];
        for(int i=0;i<10;i++)
        a[i]=i;
        
        long long int z=1,zo=1;;
        int flag=0;
        for(long long int i=1;flag!=1;i++)
        {
            z=n*i;
            zo=z;
            while(z!=0)
            {
                int u=z%10;
                z=z/10;
                for(int j=0;j<10;j++)
                {
                    if(u==a[j])
                    a[j]=100;
                }
            }
            int sum=0;
            for(int l=0;l<10;l++)
            sum=sum+a[l];
            if(sum==1000)
            flag=1;
        }
        cout<<"Case #"<<no<<": "<<zo<<endl;
    }
	return 0;
}
