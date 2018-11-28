#include <iostream>
#include <vector>
using namespace std;
int main()
{
	int T;
	int counter=0;
	cin>>T;
	while(T--)
	{
		counter++;
		vector <int> val;
		vector <int> val2;
		int r,c,pr,pc;
		r=4;
		c=4;
		cin>>pr;
		for(int i=0;i<r;i++)
		{
			for(int j=0;j<c;j++){
				int temp;
				cin>>temp;
				if(i==pr-1)val.push_back(temp);
			}
		}
		cin>>pc;
		for(int i=0;i<r;i++)
		{
			for(int j=0;j<c;j++){
				int temp;cin>>temp;
				if(i==pc-1)val2.push_back(temp);
			}
		}
		int ans=-1;
		for(int i=0;i<val.size();i++)
		{
			for(int j=0;j<val2.size();j++)
			{
				if(val[i] == val2[j]){
					if(ans==-1) ans = i;
					else ans=-2;
				}
			}
		}
		if(ans==-1) cout<<"case #"<<counter<<": Volunteer cheated!"<<endl;
		else if(ans==-2) cout<<"case #"<<counter<<": Bad Magician!"<<endl;
		else cout<<"case #"<<counter<<": "<<val[ans]<<endl;
	}
}	