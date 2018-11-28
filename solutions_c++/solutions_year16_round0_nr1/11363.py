#include <bits/stdc++.h>
using namespace std;
bool arr[10]={false};
bool detect()
{
	for (int i = 0; i < 10; ++i)
	{
		if(!arr[i])
			return false;
	}
	return true;
}
void split(int x)
{
	while(x)
		arr[x%10]=true,
		x/=10;

}
int main(int argc, char const *argv[])
{
	int t;
	cin>>t;
	for(int i=1;i<=t;i++){
		int n;
		cin>>n;
		if(!n)
			cout<<"Case #"<<i<<": INSOMNIA\n";
		else
		{
			int cunt=1;
			while(!detect())
				split(n*cunt),
				cunt++;
			cout<<"Case #"<<i<<": "<<n*(cunt-1)<<"\n";
			for(int j=0;j<10;j++)
				arr[j]=false;
		}

	}
	return 0;
}