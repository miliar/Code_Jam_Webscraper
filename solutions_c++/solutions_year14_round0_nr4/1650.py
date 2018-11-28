#include<fstream>
#include<vector>
#include<algorithm>

using namespace std;

int main()
{
	ifstream in("G:\\job\\google_jam\\data\\D-large.in");
	ofstream out("G:\\job\\google_jam\\data\\D-l.out");
	int num_cases;
	in >> num_cases;
	for(int i = 1; i <= num_cases; ++i)
	{
		int num_items;
		in >> num_items;
		vector<double> naomi(num_items);
		vector<double> ken(num_items);
		for(int i = 0; i < num_items; ++i)
		{
			in >> naomi[i];
		}
		for(int i = 0; i < num_items; ++i)
		{
			in >> ken[i];
		}
		sort(naomi.begin(),naomi.end());
		sort(ken.begin(),ken.end());
		int point_cheat = num_items, point_normal = num_items;
		// cal point_normal
		vector<double> ken1 = ken;
		for(int i = 0; i < num_items; ++i)
		{
			vector<double>::iterator it = ken1.begin();
			while(it != ken1.end() &&naomi[i] > *it ) ++it;
			if(it != ken1.end())
			{
				ken1.erase(it);
				point_normal--;
			}
		}
		// cal point_cheat
		ken1 = ken;
		for(int i = 0; i < num_items; ++i)
		{
			vector<double>::iterator it = --(ken1.end());
			if(naomi[i] > *ken1.begin())
			{
				ken1.erase(ken1.begin());
			}
			else if(naomi[i] > *it)
			{
				break;
			}
			else
			{
				point_cheat--;
				ken1.erase(it);
			}
		}
		out << "Case #" << i << ": " << point_cheat << " " << point_normal << endl;
	}


	out.close();
	in.close();
}