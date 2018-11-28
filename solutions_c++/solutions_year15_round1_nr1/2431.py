#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef unsigned long long llu;
#define loop(i,a,b) for(i=a;i<b;i++)
#define gc getchar  


ll rl()
{
	char c = gc();
	while(c<'0' || c>'9') c = gc();
	ll ret = 0;
	while(c>='0' && c<='9') {
		ret = 10 * ret + c - 48;
		c = gc();
	}
	return ret;		
}

int main()
{
	//ios_base::sync_with_stdio(false);
	//cin.tie(NULL);
	ll T = rl();
	string line;
	ll N,max_diff,first1,m1=0,m2=0,i,prev_mush,curr_mush,t=T;
	vector < ll > mush;
	while(T--) {
		m1 = 0;
		m2 = 0;
		max_diff = 0;
		mush.resize(0);
		N = rl();
		first1 = rl();
		max_diff = 0;
		prev_mush = first1;
		mush.push_back(first1);
		loop(i,1,N)
		{
			curr_mush = rl();
			mush.push_back(curr_mush);
			if(mush[i] < mush[i-1])
			{
				if(max_diff < mush[i-1] - mush[i])
				{
					max_diff = mush[i-1] - mush[i];
				}
			}
		}
		if(mush[0] > max_diff)
			{
				m2 += max_diff;
			}
			else
			{
				m2 += mush[0];
			}
		loop(i,1,N)
		{
			//METHOD 1

			if(mush[i] > mush[i-1])
			{
				m1 += 0;
			}
			else
			{
				m1+=mush[i-1] - mush[i];
			}



			//Method 2
			if(i != N -1)
			if(mush[i] > max_diff)
			{
				m2 += max_diff;
			}
			else
			{
				m2 += mush[i];
			}
		}
		cout<<"Case #"<<t - T<<": "<<m1<<" "<<m2<<endl;

	}
	return 0;
}