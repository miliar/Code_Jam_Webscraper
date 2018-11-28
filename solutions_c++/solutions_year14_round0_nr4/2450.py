#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

vector<double> naomi;
vector<double> ken;
int N;

int countDeceitful (int i, int j) {
	if (i>=N) return 0;
	double min = ken[j];
	while (i<N && naomi[i]<min)
		i++;
	if (i==N) return 0;
	return 1+countDeceitful(i+1,j+1);
}

int countWar() {
	if (naomi.size()==0 && ken.size()==0) return 0;
	double naomiChoice = naomi[0];
	double kenChoice=2000000000;
	naomi.erase(naomi.begin());
	int kenIndex=-1;
	for (int i=0; i<ken.size(); i++)
	{
		if (ken[i] > naomiChoice)
			continue;
		kenIndex=i-1;
		break;
	}
	if (kenIndex==-1)
	{
		kenIndex = N-1;
		kenChoice = ken[kenIndex];
	}
	ken.erase(ken.begin()+kenIndex);
	N--;
	if (naomiChoice > kenChoice)
		return 1+countWar();
	return countWar();
}


int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int T;
	cin >> T;
	for (int t=0; t<T; t++)
	{
		cin >> N;
		for (int n=0; n<N; n++) {
			double x;
			cin >> x;
			naomi.push_back(x);
		}
		for (int n=0; n<N; n++) {
			double x;
			cin >> x;
			ken.push_back(x);
		}

		sort (naomi.begin(), naomi.end());
		sort (ken.begin(), ken.end());

		int d = countDeceitful(0,0);

		reverse(naomi.begin(),naomi.end());
		reverse(ken.begin(), ken.end());

		int w = countWar();

		cout << "Case #" << t+1 << ": " << d << " " << w << endl;

		naomi.clear();
		ken.clear();
		
	}
}