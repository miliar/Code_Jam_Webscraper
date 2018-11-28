#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main()
{

	int num;
	cin >> num;
	vector<double> naomi;
	vector<double> ken;
	
	for(int i =1; i <= num;i ++)
	{
		int size;
		cin >> size;
		for(int t=0;t < size;t ++)
		{
			double tmp;
			cin >> tmp;
			naomi.push_back(tmp);
		}

		for(int t =0;t < size;t ++)
		{			
			double tmp;
			cin >> tmp;
			ken.push_back(tmp);
		}

		sort(naomi.begin(), naomi.end());
		sort(ken.begin(), ken.end());
		
		int war =0, dwar = 0;
		
		int indexNaomi = naomi.size()-1;
		int indexKen = ken.size() -1;
		int kenEnd = 0, naomiEnd = 0;
		while(indexKen >= kenEnd && indexNaomi >= naomiEnd)
		{
			if(naomi[indexNaomi] > ken[indexKen]){
				indexNaomi --;
				kenEnd ++;
				war ++;
			}else{
				indexNaomi --;
				indexKen --;
			}
		}

		indexKen = 0;
		indexNaomi = 0;
		while(indexKen < size && indexNaomi < size)
		{
			if(naomi[indexNaomi] > ken[indexKen])
			{
				dwar ++;
				indexNaomi ++;
				indexKen ++;
			}else indexNaomi ++;
		}
		cout<<"Case #"<<i<<": "<<dwar<<" "<<war<<endl;
		naomi.clear();
		ken.clear();

	}
 
	return 0;
}