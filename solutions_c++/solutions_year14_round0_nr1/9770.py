#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main()
{
	int cnt,r1,r2,temp;
	int arr1[4],arr2[4];
	std::vector<int>::iterator it;
	std::vector<int> v(4);
	int t;
	cin>>t;
	for(int i=1;i<=t;i++)
	{

		cnt=0;
		cin>>r1;
		r1--;
		for(int p=0;p<4;p++)
			for(int q=0;q<4;q++)
			{
				cin>>temp;
				if(p==r1)
					arr1[q]=temp;
			}
		cin>>r2;
		r2--;
		for(int p=0;p<4;p++)
			for(int q=0;q<4;q++)
			{
				cin>>temp;
				if(p==r2)
					arr2[q]=temp;
			}
		sort(arr1,arr1+4);
		sort(arr2,arr2+4);
		it=set_intersection (arr1, arr1+4, arr2, arr2+4,v.begin());
		cnt = it-v.begin();
		if(cnt==1)
			cout<<"Case #"<<i<<": "<<v[0]<<endl;
		else if(cnt>0)
			cout<<"Case #"<<i<<": Bad magician!"<<endl;
		else if(cnt==0)
			cout<<"Case #"<<i<<": Volunteer cheated!"<<endl;
	}
}