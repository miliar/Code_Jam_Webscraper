#include <iostream>
#include <string>
#include <vector>

using namespace std;

int opera(int a,int b)
{
	int sgn = 1;
	if(a<0)
		sgn*=-1,a*=-1;
	if(b<0)
		sgn*=-1,b*=-1;
	if(a==10 && b==10)			//i
		return -1*sgn;
	if(a==100 && b==100)			//j
		return -1*sgn;
	if(a==1000 && b==1000)			//k
		return -1*sgn;
	if(a==10 && b==100)
		return 1000*sgn;
	if(a==100 && b==1000)
		return 10*sgn;
	if(a==1000 && b==10)
		return 100*sgn;
	if(a==1)
		return b*sgn;
	if(b==1)
		return a*sgn;
	return -opera(b,a)*sgn;
}

int main()
{
	int T;
	cin >> T;
	for(int I=0;I<T;I++)
	{
		int x,l;
		cin >> l >> x;
		string s;
		cin >> s;
		vector<int> nums(x*l);
		for(int i=0;i<x*l;i++)
		{
			if(s[i%l]=='i')
				nums[i] = 10;
			else if(s[i%l]=='j')
				nums[i] = 100;
			else
				nums[i] = 1000;
		}
		int rest = 1;
		int status = 0;
		for(int i=0;i<x*l;i++)
		{
			rest = opera(rest,nums[i]);
			if(status==0 && rest==10)	status++,rest=1;
			if(status==1 && rest==100)	status++,rest=1;
		}
		if(status==2 && rest==1000)	status++;
		cout << "Case #" << I+1 << ": ";
		if(status==3)
			cout << "YES" << endl;
		else
			cout << "NO" << endl;
	}
}
