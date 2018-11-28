#include <iostream>
#include <cstdio>
#include <map>
#include <cassert>
using namespace std;
int main(int argc, char const *argv[])
{
	int T;
	cin>>T;
	// T = 1000000;
	for(int TT = 1; TT <= T; TT++)
	{
		printf("Case #%d: ",TT);
		int n;
		cin>>n;
		// n=TT;
		int curNumber = n;
		int vis[10] = {0};
		int resident = 10;
		if(curNumber == 0) 
		{
			cout<<"INSOMNIA"<<endl;
			continue;
		}
		int cnt = 0;
		while(resident) 
		{
			cnt++;
			assert(cnt < 90);
			int tmp = curNumber;
			while(tmp)
			{
				if(!vis[tmp%10])
				{
					vis[tmp%10] = 1;
					resident--;
				}
				tmp /= 10;
			}
			if(!resident)
			{
				cout<<curNumber<<endl;
				break;
			}
			curNumber += n;
		}
	}	
	return 0;
}