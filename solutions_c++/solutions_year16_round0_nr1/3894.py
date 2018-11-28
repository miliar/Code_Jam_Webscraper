#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<cstring>

using namespace std;

int t;
long long n;
int used[11]={0};

int pending(int x)
{
	int res=0;
	while(x)
	{
		int xx=x%10;
		if(used[xx]==0){
			used[xx]=1;
			res++;
		}
		x/=10;
	}
	return res;
}

int main()
{
	int i,j,k;
	int tcase=1;
	int counter=0;
	freopen("in2","r",stdin);
	freopen("out2","w",stdout);

	cin>>t;
	for(i=1;i<=t;i++)
	{
		counter=0;
		fill(used,used+10,0);
		cin>>n;
		if(n==0)
		{
			cout<<"Case #"<<tcase++<<": INSOMNIA"<<endl;
		}
		else
		{
			for(j=1;j<=1000000;j++)
			{
				counter+=pending(n*j);
				if(counter==10)break;
			}
			cout<<"Case #"<<tcase++<<": "<<j*n<<endl;
		}
		
	}
	
	fclose(stdin);
	fclose(stdout);
	return 0;
}
