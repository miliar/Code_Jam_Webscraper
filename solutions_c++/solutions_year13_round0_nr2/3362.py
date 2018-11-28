#include<iostream>
#include<vector>
using namespace std;

int main()
{
	int t;
	cin>>t;
	for(int q=1;q<=t;q++)
	{
		int m,n,ee;
		vector< vector<int> > a;
		vector<int> v;
		cin>>n>>m;
		int min=101,r=0,c=0;
		for(int i=0;i<n;i++)
		{
			v.clear();

			for(int j=0;j<m;j++)
			{
				cin>>ee;
				v.push_back(ee);
			}	
			a.push_back(v);
		}
		do
		{
		
/*		for(int i=0;i<a.size();i++)
		{
			for(int j=0;j<a[i].size();j++)
				cout<<a[i][j]<<" ";
			cout<<endl;
		}
		cout<<endl;
*/	
		min=101;
		for(int i=0;i<a.size();i++)
			for(int j=0;j<a[i].size();j++)
			{	
				if(a[i][j]<min)
				{
					min=a[i][j];
					r=i;
					c=j;
				}
			}
		bool cr=true,cc=true;
		int i;




//		cout<<"Min = "<<min<<" "<<r<<" "<<c<<endl;






		for(i=0;i<m;i++)
		{
//			cout<<a[r][i]<<";; ";
			if(a[r][i]>min)
			{
//				cout<<"False";
				cr=false;
			}
		}
		for(i=0;i<n;i++)
		{
			if(a[i][c]>min)
				cc=false;
		}
//		cout<<"CR = "<<cr<<" CC = "<<cc<<endl; 
		if((cr==false)&&(cc==false))
		{
			cout<<"Case #"<<q<<": NO"<<endl;
			break;
		}
		if(cr)
		{
			a.erase(a.begin()+r);
//			cout<<"Row deleted"<<endl;
			n--;
		}
		else if(cc)
		{
			for(i=0;i<a.size();i++)
			{
				
				a[i].erase(a[i].begin()+c);	
			}
//			cout<<"Column deleted";
			m--;
		}
	        }while(!a.empty());
	if(a.empty())
		cout<<"Case #"<<q<<": YES"<<endl;
	}
	return 0;
}	
	
	
