#include<cstdio>
#include<cstring>
#include<cmath>
#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int arr[10];

int isNotPrime(long long int num)
{
	if(num == 1) return 0;
	if(num == 2 || num == 3) return 0;

	for(int i=2;i<=sqrt(num);i++)
	{
		if(num%i == 0) return i;
	}

	return 0;
}
 
long long int powFun(long long int num, int times)
{
	if(times==1) return num;
	long long int ans=1;
	for(int i=1;i<=times;i++)
	{
		ans=ans*num;
	}

	return ans;
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	
	int cases;
	scanf("%d",&cases);
	int count=0;
	while(cases--)
	{
		printf("Case #%d:\n",++count);
		int N,J;
		scanf("%d%d",&N,&J);

		int start=1<<(N-1);
		int end=1<<N;
		int count=0;
		for(int i=start+1;i<=end && count != J ;i++)
		{
			if(i%2 == 0) continue;
			int tmp=i;
			
			//convert to binary
			string s="";
			while(tmp != 0)
			{
				int rem=tmp%2;
				tmp=tmp/2;
				char c='0'+rem;
				s=s+c;
			}
			int count2=0;
			vector<int>ans;
			for(int j=2;j<=10;j++)
			{
				long long int num=0;
				num=s[0]-'0';
				for(int k=1;k<s.size();k++)
				{
					int m=s[k]-'0';
					num=num+powFun(j,k)*m;
				}
				int ret=isNotPrime(num);
				if(ret>0)
				{
					count2++;
					ans.push_back(ret);
				}
				else break;
			}
			if(count2 == 9) {
				count++;
				reverse(s.begin(), s.end());
				cout<<s;
				for(int l=0;l<ans.size();l++)
				{
					cout<<" "<<ans[l];
				}
				cout<<endl;
			}
		}

	}
	

		
	return 0;

}
