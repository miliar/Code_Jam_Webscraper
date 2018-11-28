#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
vector <pair<int,int> > partai;
int input,tc,n,t=0;
long long total;
bool besar(pair<int,int> a,pair<int,int> b)
{
	if(a.first>b.first)
		return true;
	else
		return false;
}
int main()
{
	freopen("input.in","r",stdin);
	freopen("output.out","w",stdout);	
	scanf("%d",&tc);
	while(tc--)
	{
		//cout<<"tc"<<endl;
		scanf("%d",&n);
		total=0;
		for(int i=0;i<n;i++)
		{
			scanf("%d",&input);
			total+=input;
			partai.push_back(make_pair(input,i));
		}
		for(int i=0;i<3;i++)
			partai.push_back(make_pair(0,0));
		sort(partai.begin(),partai.end(),besar);
		printf("Case #%d:",++t);
		while(total!=0)
		{
			//cout<<endl<<partai[0].first<<" "<<partai[0].second<<endl;
			//cout<<total<<endl;
			//system("PAUSE");
			if(partai[0].first>=2&&partai[1].first<=(total-2)/2)
			{
				//cout<<"masuk1"<<endl;
				partai[0].first-=2;
				total-=2;
				char a=(partai[0].second+'A');
				cout<<" "<<a<<a;
			}
			else if(partai[0].first>=1&&partai[1].first<=(total-1)/2)
			{
				//cout<<"masuk2"<<endl;
				partai[0].first--;
				total--;
				char a=(partai[0].second+'A');
				cout<<" "<<a;
			}
			else if(partai[0].first>=1&&((partai[1].first-1)<=(total-2)/2)&&(partai[2].first<=(total-2)/2))
			{
				//cout<<"masuk3"<<endl;
				total-=2;
				partai[0].first--;
				partai[1].first--;
				char a=(partai[0].second+'A');
				char b=(partai[1].second+'A');
				cout<<" "<<a<<b;
				sort(partai.begin(),partai.end(),besar);
			}
			else
			{
				//cout<<"masuk4"<<endl;
				sort(partai.begin(),partai.end(),besar);
			}
		}
		printf("\n");
	}
}
