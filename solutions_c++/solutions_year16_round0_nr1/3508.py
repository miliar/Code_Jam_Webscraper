#include <iostream>
using namespace std;

typedef long long ll;
int digit;
int cnt[10];
ll sum=0,temp=0;

int main()
{
    ios_base::sync_with_stdio(false);
    
    int t,T;
    cin>>T;
    
    for(t=1;t<=T;++t)
    {
        int n;
        cin>>n;
        
        for(int i=0;i<10;++i) cnt[i]=0;
        
        sum=0;
        int idx=1;
        while(true)
        {
            if(n == 0) break;
            
            temp=(ll)idx*n;
            while(temp > 0)
            {
                digit=temp%10;
                if(cnt[digit] == 0)
                {
                    cnt[digit]=1;
                    sum++;
                }
                
                else cnt[digit]=1;
                
                temp/=10;
                
                //cout<<digit<<' ';
            }
            
            if(sum == 10) break;

            idx++;
        }
        
        cout<<"Case #"<<t<<": ";
        
        if(sum == 10) cout<<(ll)idx*n<<'\n';
                
        else cout<<"INSOMNIA\n";
    }
    
    return 0;
}