#include <iostream>
#include <string>
#include<vector>
#include<algorithm>
using std::string;
using std::cin;
using std::cout;
using std::endl;

//using namespace std;

bool ascending (int i,int j) { return (i<j); }
bool descending (int i,int j) { return (i>j); }

int getWar(std::vector<double>naomiBlocks,std::vector<double>kaiBlocks)
{
	
	//cout << "Size " << kaiBlocks.size() << endl;
	std::sort(naomiBlocks.begin(),naomiBlocks.end());
	std::sort(kaiBlocks.begin(),kaiBlocks.end());
	int i;
	i = 0;
	double current1;
	int counter = 0;
	while(naomiBlocks.size()!=0)
	{
		i = 0;
		current1 = naomiBlocks.at(0);
		
		//toRemove = naomiBlocks.at(0);
		
		 
		for (std::vector<double>::iterator it = kaiBlocks.begin(); it != kaiBlocks.end(); ++it)
	{
		if((*it) > current1)
		{
			//count--;
			break;

		}
		i++;
		

	}
		if(i == kaiBlocks.size())		
		{	
			kaiBlocks.erase(kaiBlocks.begin());
			counter++;
		}
		else
			kaiBlocks.erase(kaiBlocks.begin()+i);
			
		naomiBlocks.erase(naomiBlocks.begin());
		
		//cout << "Kai's blocks..." << endl;
		for (std::vector<double>::iterator it = kaiBlocks.begin(); it != kaiBlocks.end(); ++it)
	{
		//cout << (*it) << "\n";
		

	}

		
	}
	naomiBlocks.clear();
	kaiBlocks.clear();
	return counter;

}
int getDeceitfulWar(std::vector<double>naomiBlocks,std::vector<double>kaiBlocks)
{
	
	//cout << "Size " << kaiBlocks.size() << endl;
	std::sort(naomiBlocks.begin(),naomiBlocks.end());
	//std::sort(kaiBlocks.begin(),kaiBlocks.end(),std::greater<int>());
	std::sort(kaiBlocks.begin(), kaiBlocks.end());
	int i,j=0;
	i = 0;
	double current1,current2;
	int counter = 0;
	while(kaiBlocks.size()!=0)
	{




	/*			cout << "Kai's blocks..." << endl;
		for (std::vector<double>::iterator it = kaiBlocks.begin(); it != kaiBlocks.end(); ++it)
	{
		cout << (*it) << " ";
		

	}
		cout << "\n";
		cout << "Naomi's blocks..." << endl;
		for (std::vector<double>::iterator it = naomiBlocks.begin(); it != naomiBlocks.end(); ++it)
	{
		cout << (*it) << " ";
		

	}	
		cout << "\n";*/

		i = 0;
		if(naomiBlocks.at(naomiBlocks.size()-1) > kaiBlocks.at(kaiBlocks.size()-1) )
		
	{	
		current1 = kaiBlocks.at(0);
		//cout << "Entered 1st if" << endl;	
		//toRemove = naomiBlocks.at(0);
		
		 
		for (std::vector<double>::iterator it = naomiBlocks.begin(); it != naomiBlocks.end(); ++it)
		{
		if((*it) > current1)
		{
			//count--;
			break;

		}
		i++;
		

		}	
		//cout << "Entered 2nd if" << endl;
			counter++;
			naomiBlocks.erase(naomiBlocks.begin()+i);	
			kaiBlocks.erase(kaiBlocks.begin());
		//cout << "Entered third if" << endl;
	
	}
	if(kaiBlocks.size()==0)
		return counter;
	if(naomiBlocks.at(naomiBlocks.size()-1) < kaiBlocks.at(kaiBlocks.size()-1))
	{
		current2 = naomiBlocks.at(0); 
		naomiBlocks.erase(naomiBlocks.begin());	
		kaiBlocks.erase(kaiBlocks.begin()+kaiBlocks.size()-1);
	}



	
	}
	//if(naomiBlocks.at(0) > kaiBlocks.at(0))
	//	counter++;
	//naomiBlocks.clear();
	//kaiBlocks.clear();
	return counter;

}

int main()
{

	int T;
	cin >> T;
	std::vector<string> output;
 	string str;
	std::vector<double>naomi,kai;
	double block1,block2;
	int result = 0;
	int n;
	for(int t = 0; t < T; t++)
	{
		naomi.clear();
		kai.clear();
		result = 0;
		n = 0;
		cin >> n;
		//cout << "Size intake = " << n << endl;
		for(int j = 0;j < n;j++)
		{
		
			cin >> block1;
			naomi.push_back(block1);

		}
		for(int k = 0;k < n;k++)
		{
		
			cin >> block2;
			kai.push_back(block2);

		}
		result = 0;
		//cout << "Size before calling" << kai.size() << endl;
		result = getDeceitfulWar(naomi, kai);
		str = "Case #" + std::to_string(t+1) + ": " + std::to_string(result) + " " + std::to_string(getWar(naomi,kai));
		output.push_back(str);	

	}

	for (std::vector<string>::iterator it = output.begin(); it != output.end(); ++it)
	{
		cout << (*it) << "\n";
		

	}





}


/*		cout << "Kai's blocks..." << endl;
		for (std::vector<double>::iterator it = kaiBlocks.begin(); it != kaiBlocks.end(); ++it)
	{
		cout << (*it) << " ";
		

	}
		cout << endl;
		cout << "Naomi's blocks..." << endl;
		for (std::vector<double>::iterator it = naomiBlocks.begin(); it != naomiBlocks.end(); ++it)
	{
		cout << (*it) << " ";
		

	}	
*/
