#include <map>
#include <iostream>

using namespace std;

int arr1[4][4], arr2[4][4], s1, s2;

int main(void)
{
#ifdef _CONSOLE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w+", stdout);
#endif

	int t;
	cin>>t;
	for(int k=1 ; k<=t ; k++)
	{
		cin>>s1;
		for(int i=0 ; i<4 ; i++)
			for(int j=0 ; j<4 ; j++)
				cin>>arr1[i][j];
		cin>>s2;
		for(int i=0 ; i<4 ; i++)
			for(int j=0 ; j<4 ; j++)
				cin>>arr2[i][j];

		map<int, int> sol;
		for(int i=0 ; i<4 ; i++) sol[arr1[s1-1][i]]++;
		for(int i=0 ; i<4 ; i++) sol[arr2[s2-1][i]]++;

		if(sol.size()==8) cout<<"Case #"<<k<<": Volunteer cheated!"<<endl;
		else if(sol.size()==7)
		{
			map<int, int>::iterator it=sol.begin();
			int ssol;
			for( ; it!=sol.end() ; it++)
				if(it->second==2) ssol=it->first;

			cout<<"Case #"<<k<<": "<<ssol<<endl;
		}
		else cout<<"Case #"<<k<<": Bad magician!"<<endl;
	}
}