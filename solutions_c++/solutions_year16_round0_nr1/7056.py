#include<bits/stdc++.h>
using namespace std;
bool used[11];
int main()
{
	ios::sync_with_stdio(0);
	cin.tie(0);
	int T;cin>>T;
	for(int ks=1;ks<=T;ks++)
    {
        memset(used,0,sizeof(used));
        long long N;cin>>N;
        long long cur=N;
        cout<<"Case #"<<ks<<": ";
        if(N==0) {cout<<"INSOMNIA\n";continue;}
        while(1)
        {
            long long rec=cur;
            while(rec>0)
            {
                int lst=rec%10;
                used[lst]=1;
                rec/=10;
            }
            bool f=0;
            for(int i=0;i<10;i++)
            {
                if(!used[i]) f=1;
            }
            if(!f) break;
            cur+=N;
        }
        cout<<cur<<'\n';
    }
	return 0;
}
