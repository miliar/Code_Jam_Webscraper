#include <iostream>
using namespace std;

int main()
{
	int n;
	
	cin>>n;
	for(int ca=1;ca<=n;ca++)
	{
		int k,cnt=0,tmp;
		bool chk[10]={0};
		
		cin>>k;
		if(!k)
		{
			cout<<"Case #"<<ca<<": INSOMNIA\n";
			continue;
		}
		for(int i=1;;i++)
		{
			tmp = k	* i;
			while(tmp)
			{
				int nxt = tmp % 10;
				if(!chk[nxt]) cnt++,chk[nxt]=true;
				tmp /= 10;
			}
			if(cnt == 10)
			{
				cout<<"Case #"<<ca<<": "<<k*i<<"\n";
				break;
			}
		}
	}
}