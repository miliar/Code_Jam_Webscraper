    #include <bits/stdc++.h>
    using namespace std;
    #ifndef ONLINE_JUDGE
    #define gc getchar
    #else
    #define gc getchar_unlocked
    #endif
    inline long long int read_int()
    {
        char c = gc();
        while(c<'0' || c>'9')
        c = gc();
        long long int ret = 0;
        while(c>='0' && c<='9')
        {
        ret = (ret<<3) + (ret<<1) + c - 48;
        c = gc();
        }
        return ret;
    }
     
    int main() {
        long long int n,j,t,num,x,i,y,flag,k,m,ans;
    	cin>>t;
    	for(j=1;j<=t;j++)
    	{
			int a[12]={0};k=1;
			cin>>n;
			flag=0;ans=n;
			if(n==0)
				cout<<"Case #"<<j<<": INSOMNIA"<<"\n";
			else
			{
				m=n;
				while(m!=0)
				{
					a[m%10]++;
					m=m/10;
					
					if(m==0)
					{
						/*
						for(i=0;i<=9;i++)
						{
							cout<<a[i]<<",";
						}
						cout<<"\n";
						*/
						for(i=0;i<=9;i++)
						{
							if(a[i]>=1)
							{
								flag=1;
							}
							else
							{
								flag=0;
								break;
							}
						}
						if(flag==1)
						{
							ans=k*n;
							break;
						}
						else
						{
							k++;
							m=k*n;
						}
					}
					
				}
				
				cout<<"Case #"<<j<<": "<<ans<<"\n";
			
			}
		
    	}
     
        return 0;
    } 