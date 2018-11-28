#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;
class deceitful
{
public:
	void clean()
	{
		numberOfBlocks=0;
		war=0;
		dwar=0;
		naomi.clear();
		ken.clear();
	}
	void input()
	{
		cin>>numberOfBlocks;
		int counter1;
		double temp=0.0;
		for(counter1=0;counter1<numberOfBlocks;counter1++)
		{
			cin>>temp;
			naomi.push_back(temp);
		}
		for(counter1=0;counter1<numberOfBlocks;counter1++)
		{
			cin>>temp;
			ken.push_back(temp);
		}
	}
	void workflow()
	{
		sort(naomi.rbegin(),naomi.rend());
		sort(ken.rbegin(),ken.rend());
		int counter2=0;
		for(int counter1=0;counter1<numberOfBlocks;counter1++)
		{
			if(naomi[counter1]>ken[counter2])
			{
				war++;
			}
			else if(naomi[counter1]<ken[counter2])
			{
				counter2++;
			}			
		}
		counter2=0;
		int counter1=0;
		int numberOfBlocks_2=numberOfBlocks;
		while((counter1<numberOfBlocks)&&(counter2<numberOfBlocks_2))
		{
			if(naomi[counter1]>ken[counter2])
			{
				dwar++;
				counter1++;
				counter2++;
			}
			else
			{
				numberOfBlocks--;
				counter2++;
			}
		}				
		cout<<dwar<<" "<<war<<"\n";
	}
private:
	int numberOfBlocks,war,dwar;
	vector <double> naomi,ken;
};
int main()
{
	int t;
	cin>>t;
	int c=1;
	deceitful obj;
	while(t!=0)
	{
		t--;
		cout<<"Case #"<<c<<": ";
		c++;
		obj.clean();
		obj.input();
		obj.workflow();
	}
	return 0;
}
	
