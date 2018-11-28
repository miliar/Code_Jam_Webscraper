#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <fstream>    // make obj and use it
#include <utility>
using namespace std;
int main()
{
			
					ifstream input("./testcase files/Infinite House of Pancakes/B-small-attempt2.in");
					ofstream output("./output files/Infinite House of Pancakes/B-small-attempt2.txt");
			
	
	int test_cases,d,count=0,cost=0,x=0;
	
	input>>test_cases;
//	cin>>test_cases;
	for(int tt=1;tt<=test_cases;tt++)
	{
		count=cost=0;
		input>>d;
	
	//	cin>>d;
		
		vector<int > v;
		
		int arr[d];
		
		for(int u=0;u<d;u++)
		{
			input>>x;
		//	cin>>x;
			arr[u]=x;
			v.push_back(x);
		}
		
		make_heap(v.begin(),v.end());
		
		cost= v.front();
		
		
		if(cost<=3)
		{
			output<<"Case #"<<tt<<": "<<cost<<endl;continue;
			
		//	cout<<"Case #"<<tt<<": "<<cost<<endl;continue;
		}
		int M=0;
		
		while(v.front()>3)
		{
			M=v.front();
				
			pop_heap (v.begin(),v.end());
			v.pop_back();
			if(M==4)
			{
				v.push_back((M-2)); push_heap (v.begin(),v.end());
				v.push_back((2));push_heap (v.begin(),v.end());
			}
			else
			{
				v.push_back((M-3));  push_heap (v.begin(),v.end());
				v.push_back((3)); push_heap (v.begin(),v.end());
			}	
			count++;
			cost=min(cost,count+v.front());
		}
		
		v.clear();
		for(int u=0;u<d;u++)
		{
		v.push_back(arr[u]);
		}
		make_heap(v.begin(),v.end());
		M=count=0;
		while(v.front()>4)
		{
			M=v.front();
			pop_heap (v.begin(),v.end());
			v.pop_back();
			v.push_back((M-4));  push_heap (v.begin(),v.end());
			v.push_back((4)); push_heap (v.begin(),v.end());
			count++;
			cost=min(cost,count+v.front());
		}
	
		v.clear();
		for(int u=0;u<d;u++)v.push_back(arr[u]);
		
		make_heap(v.begin(),v.end());
		M=count=0;
		while(v.front()>5)
		{
			M=v.front();
			pop_heap (v.begin(),v.end());
			v.pop_back();
			v.push_back((M-5));  push_heap (v.begin(),v.end());
			v.push_back((5)); push_heap (v.begin(),v.end());
			count++;
			cost=min(cost,count+v.front());
		}
		output<<"Case #"<<tt<<": "<<cost<<endl;
		//cout<<"Case #"<<tt<<": "<<cost<<endl;	
	}
return 0;
}

