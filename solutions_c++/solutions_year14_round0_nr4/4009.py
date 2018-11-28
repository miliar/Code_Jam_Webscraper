#include<fstream>
#include<vector>
#include<algorithm>
using namespace std;

struct myclass {
  bool operator() (float i,float j) 
  { 
	return (i<j);
  }
} increasing;


int main(int argc, char* argv[])
{
	int t;
	
	ifstream ip;
	ip.open(argv[1]);
	
	ofstream op;
	op.open("C-output.txt");
	
	ip>>t;
	
	for(int iter=1; iter<=t; iter++)
	{
		op<<"Case #"<<iter<<": ";
		
		int n;
		ip>>n;
		
		vector<float> naomi;
		vector<float> ken;
		
		float temp;
		for(int i=0; i<n; i++)
		{
			ip>>temp;
			naomi.push_back(temp);
		}
		
		for(int i=0; i<n; i++)
		{
			ip>>temp;
			ken.push_back(temp);
		}
		
		int size = naomi.size();
		
		sort(naomi.begin(), naomi.end(), increasing);
		sort(ken.begin(), ken.end(), increasing);
		
		
			
		vector<float> naomi_temp;
		vector<float> ken_temp;
		
		naomi_temp.resize(n);
		ken_temp.resize(n);
		
		naomi_temp = naomi;
		ken_temp = ken;
	
		//Legal game
		int naomi_log;
		int ken_log;
		
		int naomi_points_legal = 0;
		for(int i=0; i<n; i++)
		{
			naomi_log = i;
			int j;
			for(j=0; ken_temp[j] < naomi_temp[naomi_log] && j < ken_temp.size(); j++);
			if(j<ken_temp.size())
			{
				ken_log = j;
				ken_temp.erase(ken_temp.begin()+ken_log);
			}
			else
			{
				naomi_points_legal++;
			}
		}
		
		
		int naomi_points_illegal = 0;
		
		int count = 0;
		while(count<n)
		{
			if(naomi[0] < ken[0])
			{
				int size = ken.size()-1;
				ken.erase(ken.begin()+size);
			}
			else
			{
				ken.erase(ken.begin());
				naomi_points_illegal++;
			}
			
			naomi.erase(naomi.begin());
			count++;	
		}
		op<<naomi_points_illegal<<" "<<naomi_points_legal<<endl;

	}
	
	return 0;
}
			
				
			
		