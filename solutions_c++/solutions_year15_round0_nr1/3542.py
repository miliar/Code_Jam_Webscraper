#include<iostream>
using namespace std;

int main()
{
    int T;cin>>T;
    for(int t=0;t<T;t++)
    {
	int Smax;cin>>Smax;
	string S;cin>>S;

	int cnt=0;
	int ans=0;

	for(int i=0;i<S.size();i++)
	{
	    if(cnt<i)
	    {
		ans+=i-cnt;
		cnt+=(i-cnt);
	    }
	    cnt+=S[i]-'0';
	}
	cout<<"Case #"<<t+1<<": "<<ans<<endl;
    }
    return 0;
}
