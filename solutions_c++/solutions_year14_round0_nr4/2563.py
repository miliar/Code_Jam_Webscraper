#include <fstream>
#include <iomanip>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
	ifstream cin("D-large.in",ios::in);
	ofstream cout("output.txt", ios::out);

	int T;
	cin >> T;
	

	for(int i = 1 ; i<= T;i++)
	{
		vector<float> naomi;
		vector<float> ken;
		int N;
		cin >> N;
		for(int a = 0;a<N;a++)
		{
			float temp;
			cin >> temp;
			naomi.push_back(temp);
		}
		for(int a = 0;a<N;a++)
		{
			float temp;
			cin >> temp;
			ken.push_back(temp);
		}


		sort(naomi.begin(), naomi.end());
		sort(ken.begin(), ken.end());
		cout << "Case #" << i << ": ";
		int ans  = 0 ;
		int pos1 = 0 , pos2 = 0;
		for(int j = 0 ;j <N;j++)
		{
			if(naomi[pos1] > ken[pos2])
			{
				ans++;
				pos1++;
				pos2++;
			}
			else
			{
				pos1++;
			}
		}
		cout << ans << " ";

		ans = 0;
		for(int j = 0 ;j <N;j++)
		{
			float n = naomi[j];
			if(ken[ken.size()-1] < n)
			{
				ans++;
				ken[ken.size()-1] = 1;
				sort(ken.begin(),ken.end());
				ken.pop_back();
			}
			else
			{
				for(int a = 0;a<ken.size();a++)
				{
					if(ken[a]>n)
					{
						ken[a] = 1;
						sort(ken.begin(),ken.end());
						ken.pop_back();
						break;
					}
				}
			}
			
		}
		cout << ans << endl;
	}



	cin.close();
	cout.close();
	return 0;
}