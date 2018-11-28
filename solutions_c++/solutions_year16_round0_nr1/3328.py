#include <iostream>

using namespace std;

int main()	{
	long long num,t,n,i,j,temp,val;
	bool sleep,arr[10];
	cin>>t;
	j = 0;
	while(t--)	{
		j++;
		cin>>num;
		if(num!=0)	{
			sleep = false;
			//validate = 0;
			for(i=0;i<10;i++)	arr[i]=false;
			n = num;
			while(!sleep)	{
				temp = n;
				while(temp)	{
					val = temp % 10;
					arr[val]=true;
					temp /= 10;
				}
				for(i=0;i<10 && arr[i]==true;i++);
				if(i==10)	sleep = true;
				else	n += num;
			}
			cout<<"Case #"<<j<<": "<<n<<endl;
		}
		else {
			cout<<"Case #"<<j<<": INSOMNIA"<<endl;
		}
	}
}