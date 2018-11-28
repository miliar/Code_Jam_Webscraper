#include <iostream>
# include<map>
using namespace std;

int main() {
	int t;
	cin>>t;
	int xx=1;
	while(t--)
	{
		int ans1,ans2,ans;
		cin>>ans1;
		map<int,int> m;
		for(int i =1;i<=16;i++ ) m[i] = 0;
		for(int i =1;i<=4;i++)
		{
			for(int j= 1;j<=4;j++)
			{
				int temp;
				cin>>temp;
				if(ans1 == i) m[temp]= 1;
			}
		}
		
		cin>>ans2;
		
		int cnt = 0,flag=0;
		
		for(int i =1;i<=4;i++)
		{
			for(int j= 1;j<=4;j++)
			{
				int temp;
				cin>>temp;
				if(m[temp] == 1 && ans2 == i && cnt > 0) 
				{
					flag = 1;
				}
				if(m[temp] == 1 && ans2 == i && cnt == 0 ) 
				{
					cnt = 1;
					ans = temp;
				}
				
			}
		}
		if(cnt == 0)
		{
			cout<<"Case #"<<xx<<": Volunteer cheated!\n";
		}
		else
		if(flag == 1)
		{
			cout<<"Case #"<<xx<<": Bad magician!\n";
		}
		else
		{
			cout<<"Case #"<<xx<<": "<<ans<<"\n";
		}
		xx++;
	}
	return 0;
}