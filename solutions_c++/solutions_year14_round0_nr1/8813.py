#include <iostream>
#include<algorithm>
#include<vector>
using namespace std;

int main() {
    freopen("a.in","r",stdin);
    freopen("bit2.out","w",stdout);
	int ar[4][4];
	int ar1[4][4];
	vector<int> row,finder;
	vector<int>::iterator iter;
	int x,y,c,t,r,r1,jk;
	cin>>t;
	for(jk=1;jk<=t;jk++)
	{
		finder=vector<int>();
		c=0;
		cin>>r;
		r--;
		for(x=0;x<4;x++)
		{
			for(y=0;y<4;y++)
			{
				cin>>ar[x][y];
			}
		}
		cin>>r1;
		r1--;
		for(x=0;x<4;x++)
		{
			for(y=0;y<4;y++)
			{
				cin>>ar1[x][y];
			}
		}
		row=vector<int>(ar[r],ar[r]+4);
		/*for(iter=row.begin();iter!=row.end();iter++)
			cout<<*iter<<"\t";
		cout<<endl;*/	
		for(y=0;y<4;y++)
		{
			iter=find(row.begin(),row.end(),ar1[r1][y]);
			if(iter!=row.end())
			{
				finder.push_back(*iter);
				c=*iter;
				//cout<<c<<endl;
			}
		}
		if(finder.size()==1)
		{
			cout<<"Case #"<<jk<<": "<<c<<endl;
		}
		else if(finder.size()==0)
		{
			cout<<"Case #"<<jk<<": Volunteer cheated!"<<endl;
		}
		else
		{
			cout<<"Case #"<<jk<<": Bad magician!"<<endl;
		}
	}
	// your code goes here
	return 0;
}
