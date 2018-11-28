#include <bits/stdc++.h>
using namespace std;
#define f_in(st) freopen(st,"r",stdin);
#define f_out(st) freopen(st,"w",stdout);
int time_taken[1001]={0};
int cal_time(int n)
{
	//cout<<n<<" ";
	if(n<=2)
		return 0;
	if(time_taken[n])
		return time_taken[n];
	if(n&1)
		return 1+(cal_time(n/2)+cal_time(n/2+1));
	else
		return 1+2*cal_time(n/2);
}
void pre_cal()
{
	time_taken[1]=1;
	time_taken[2]=2;
	for(int i=3;i<=10;i++)
	{
		time_taken[i]=cal_time(i);
	}
}
int count_turn(int n)
{
	int power=2,c=0;
	while(power<=n)
	{
		c++;
		power=power*2;
	}
//	cout<<c<<endl;
	if(power/2==n)
	{
		int ans=0,powr=1;
		for(int i=1;i<=c;i++)
		{
			ans+=powr;
			powr=powr*2;
		}
		return ans;
	}
	else
	{
		int ans=0,powr=1;
		for(int i=1;i<=c;i++)
		{
			ans+=powr;
			powr=powr*2;
		}
		int extra = n-power/2;
		return ans+extra;
	}
	return c;
}

int main()
{
	//pre_cal();
	/*cout<<endl;
	for(int i=1;i<=10;i++)
		cout<<time_taken[i]<<" ";
	cout<<endl;
	//*/	
	f_in("input2.txt");
	f_out("output2.txt");
	int test;
	cin>>test;
	for(int t=1;t<=test;t++)
	{
		int D;
		cin>>D;
		int hash[1001]={0};
		int a[D],max=-1;
		for(int i=0;i<D;i++)
		{
			cin>>a[i];
			if(a[i]>max)
				max=a[i];
		}
		int min_time = max, local_time = 0, previous_time = 0;
		for(int i=2;i<=max;i++)
		{
			int local_min=0;
			for(int j=0;j<D;j++)
			{
				local_min += ((a[j]+i-1)/i-1);
			}
			//cout<<i<<" "<<local_min+i;
			//cout<<endl;
			min_time=min(min_time,local_min+i);
		}
		cout<<"Case #"<<t<<": "<<min_time<<endl;
	}
	return 0;
}