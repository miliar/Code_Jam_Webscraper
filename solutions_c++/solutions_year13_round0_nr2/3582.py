#include<iostream>
#include<vector>
#include<list>
using namespace std;
const int size = 120;
int map[size][size];
bool check[size][size];
int main(void)
{
	vector < list < pair <int, int> > > graph;

	int t;
	int n, m, max = 0, temp;
	bool flag = false, ans = true;
	//freopen("input.txt","r",stdin);
	//freopen("output.txt","w",stdout);

	cin>>t;
	graph.resize(110);
	for(int i = 0; i<t; i++){
		cin>>n>>m;
		ans = true;
		memset(map, 0, sizeof(int) * size * size);
		for(int j = 1; j<=n; j++){
			for(int k = 1; k<=m; k++){
				cin>>temp;
				if(temp > max)max = temp;
				graph[temp].push_back(make_pair(j, k));
			}
		}

		for(int j = max; j>=1 && ans; j--){
			memset(check, false, sizeof(bool) * size * size);
			for(int k = j; k>=1; k--){
				for(list < pair<int, int> > ::iterator it1 = graph[k].begin(); it1 != graph[k].end(); it1++){
					map[(*it1).first][(*it1).second] = j;
				}
			}

			for(int k = j; k>=1 && ans; k--){
				for(list < pair<int, int> > ::iterator it1 = graph[k].begin(); it1 != graph[k].end(); it1++)
				{
					flag = false;
					if(check[(*it1).first][(*it1).second])continue;
					int count = 0;
					for(int l = 1; l<=m; l++){
						if(map[(*it1).first][l] == j){
							count++;
						}
					}
					if(count == m){
						for(int l = 1; l<=m; l++){
							check[(*it1).first][l] = true;
						}
						flag = true;
					}
					count = 0;
					for(int l = 1; l<=n; l++){
						if(map[l][(*it1).second] == j){
							count++;
						}
					}
					if(count == n){
						for(int l = 1; l<=n; l++){
							check[l][(*it1).second] = true;
						}
						flag = true;
					}
					if(!flag)ans = false;
				}
			}
		}

		if(ans)cout<<"Case #"<<i + 1<<": YES"<<endl;
		else cout<<"Case #"<<i + 1<<": NO"<<endl;
		for(int j = 1; j<=max; j++)while(!graph[j].empty())graph[j].pop_back();
	}


	return 0;
}