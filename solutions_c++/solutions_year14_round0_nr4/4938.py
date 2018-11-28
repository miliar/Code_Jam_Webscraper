#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
std::vector<double> v1,v2,v3,v4;
int main() {
	// your code goes here
	int t;
	scanf("%d",&t);
	int caseno=1;
	while(t--)
	{
		v1.clear();
		v2.clear();
		v3.clear();
		v4.clear();
		int n;
		scanf("%d",&n);
		double temp;
		for(int i=0;i<n;i++)
		{
			cin>>temp;
			v1.push_back(temp);
		}
		
		for(int i=0;i<n;i++)
		{
			cin>>temp;
			v2.push_back(temp);
		}
		sort(v1.begin(),v1.end());
		sort(v2.begin(),v2.end());
	/*	for(int i=0;i<n;i++)
		{
			cout<<v1[i]<<" ";
		}
		cout<<endl;
		for(int i=0;i<n;i++)
		{
			cout<<v2[i]<<" ";
		}
		cout<<endl;*/
		
		if(v1.back()>v2.front())
		{
			v3 = v1;
		v4 = v2;
	
		while( !v1.empty() && !v2.empty() && (v1.front() <= v2.back()) )
		{
		//	cout<<"v1 "<<v1.size()<<endl;
		
			while(!v1.empty() && !v2.empty() && (v1.front() <= v2.front()))
			{
				v1.erase(v1.begin());
				v2.erase(v2.begin());
			}
			
			if(v2.empty() || !(v1.front() <= v2.back()))
				break;
			
			int ul,ll,mid;
			ul=v2.size();
			ul--;
			ll=0;
			mid = 0;
		//	cout<<ul<<ll<<endl;
			while(ll<ul)
			{
				mid = (ul+ll)/2;
				if(v2[mid]==v1[0])
					break;
				else if(v2[mid] < v1[0])
					ll=mid+1;
				else
					ul=mid-1;
			}
			if(mid!=0)
			mid = (ul+ll)/2;
			
			//cout<<"ll "<<ll<<" "<<ul<<endl;
			//cout<<"v mid "<<v2[mid]<<endl;
			int len=v2.size();
		//	cout<<"v2 "<<len<<endl;
			if(v2[mid]<v2.back())
			{
				while(mid<len && v2[mid]<=v1[0])
			{
				mid++;
			}
				
			
			}
			
			//	cout<<v1[0]<<" asdasd "<<v2[mid]<<endl;
				v1.erase(v1.begin());
				v2.erase(v2.begin()+mid);
			//	cout<<v1.size()<<" ";
			/*while(!v2.empty() && (v2.front()<=v1.front()))
			{
				v2.erase(v2.begin());
				
			}
			
			v1.erase(v1.begin());
			if(v2.empty())
				break;
			else
				v2.erase(v2.begin());*/
		}
		
		int d_score=0;
		while(!v3.empty())
		{
			/*while(!v3.empty() && v3.front() < v4.back())
			{
				v3.erase(v3.begin());
				v4.pop_back();
			}*/
			
			while(!v3.empty()&& (v3.front() < v4.front()))
			{
				v3.erase(v3.begin());
				v4.pop_back();	
			}
			while(!v3.empty()&& (v3.front() == v4.front()))
			{
				v3.erase(v3.begin());
				v4.erase(v4.begin());
			}
			
			if(!v3.empty() && (v3.front() > v4.front()))
			{
				v3.erase(v3.begin());
			v4.erase(v4.begin());
			//	v4.pop_back();	
				d_score++;
			}
		
		}
		printf("Case #%d: %d %d\n",caseno++,d_score,v1.size());
		}else
		{
			printf("Case #%d: %d %d\n",caseno++,0,0);
		}
		
		
	//	cout<<"Case #"<<caseno++<<": "<<d_score<<" "<<v1.size()<<endl;
		
	}
	return 0;
}