#include<iostream>
#include<vector>
using namespace std;
int main()
{
	int T; cin >> T;
	for(int p=1;p<=T;p++)
	{
		long long blackRings =0;
		long long r, t; cin >> r >> t;
		long long usedColor =0;
		bool canColor=true;
		long long start=1;
		long long end = 707500000;
		int count=0;
		//long long sum =0;
		long long k;
		for(long long i=1;canColor==true;i++)
		{
			if(count <= 25)
			{
				long long sum = start*(2*r+1+(start-1)*2);
				if(sum <= t && sum >0)
				{
					blackRings = start;
					usedColor = sum;
					k=start;
					start = (start+end)/2;
				}
				else
					end = (start+end)/2;
			}
			//blackRings = start;
			else
			{
				long long currentReq = 2*r + (k*4 +1);
				start++;
				if(currentReq <= t-usedColor)
				{
					blackRings++;
					usedColor += currentReq;
				}
				else
					canColor = false;
				k++;
			}
			count++;
		}
		cout<<"Case #"<<p<<": "<<blackRings<<endl;
	}
	return 0;
}