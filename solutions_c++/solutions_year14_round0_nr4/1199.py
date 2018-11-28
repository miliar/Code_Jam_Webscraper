#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
int War(vector<double>& noami,vector<double>& ken)
{
	int toRet=0;
	sort(noami.begin(),noami.end());
	sort(ken.begin(),ken.end());
	vector<bool> used(noami.size(),false);
	for(int i=0;i<noami.size();i++)
	{
		double x=noami[i];
		int y=0;
		for(int j=0;j<ken.size();j++)
		{
			if(!used[j])
			{
				y=j;
			}
			if((x<ken[y] && !used[y]) || j==ken.size()-1)
			{
				used[y]=true;
				break;
			}
		}
		if(x>ken[y])
		{
			toRet++;
		}
	}
	return toRet;
}
int Deceipt(vector<double>& noami,vector<double>& ken)
{
	int toRet=0;
	sort(noami.begin(),noami.end());
	sort(ken.begin(),ken.end());
	vector<bool> used(noami.size(),false);
	for(int i=ken.size()-1;i>=0;i--)
	{
		double y=-1;
		for(int j=0;j<noami.size();j++)
		{
			if(noami[j]>ken[i] && !used[j])
			{
				y=noami[j];
				used[j]=true;
				break;
			}
		}
		if(y<ken[i]){
			for(int j=0;j<noami.size();j++)
			{
				if(!used[j])
				{
					used[j]=true;
					break;
				}
			}
		}
		if(y>ken[i])
		{
			toRet++;
		}
	}
	return toRet;
}
int main()
{
	int  T;
	cin>>T;
	for(int t=1;t<=T;t++)
	{
		int n;
		cin>>n;
		int war=0,dwar=0;
		vector<double> a_naomi(n),a_ken(n),b_naomi,b_ken;
		for(int i=0;i<n;i++)
		{
			cin>>a_naomi[i];
		}
		for(int i=0;i<n;i++)
		{
			cin>>a_ken[i];
		}
		b_naomi=a_naomi;
		b_ken=a_ken;
		cout<<"Case #"<<t<<": "<<Deceipt(b_naomi,b_ken)<<" "<<War(a_naomi,a_ken)<<endl;
	}
	return 0;
}