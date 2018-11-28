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
        long long int n,j,t,num,x,i,y,flag,k,m,ans,s,len;
    	cin>>t;
    	for(j=1;j<=t;j++)
    	{
			char str[105]={'\0'};
			string s;ans=0;
			cin>>s;
			len=s.size();
			//cout<<s<<","<<len<<" \n";
				for(i=len-1;i>=0;i--)
				{
					if(s[i]=='-' && (ans%2)==0)
					{
							ans++;
					}
					else if(s[i]=='+' && (ans%2)!=0)
					{
							ans++;
					}
					
				}
			
			
			cout<<"Case #"<<j<<": "<<ans<<"\n";	
		}
        return 0;
    } 