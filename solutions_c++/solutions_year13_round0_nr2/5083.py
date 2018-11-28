#include<iostream>
#include<vector>
#include<algorithm>
#include<climits>
#include<map>
#include<queue>
#include<utility>
#include<string>
#include<sstream>

using namespace std;

#define tr(c, it) \
        for(typeof((c).begin()) it = (c).begin(); it != (c).end(); it++)

//bool myfn(pair<int, int> a1, pair<int, int> a2){
//	return ((a1.first) < (a2.first));
//}

string check_feasibility(vector< vector< pair<int,int> > >& gard, int n, int m){

	// check rows
	for(int i = 0; i < n; i++){
		//int max_val = *(max_element(gard[i].begin(), gard[i].end(), myfn));
		int max_val = -1;
		for(int j = 0; j < m; j++){
			if(max_val < gard[i][j].first){
				max_val = gard[i][j].first;
			}
		}
		for(int j = 0; j < m; j++){
		
			if(gard[i][j].first == max_val){
				gard[i][j].second = 1;
			}	
	
		}
	}

	// check columns
	for(int i = 0; i < m; i++){
		
		int max_val = -1;
		for(int j = 0; j < n; j++){
			if(max_val < gard[j][i].first){
				max_val = gard[j][i].first;
			}
		}

		for(int j = 0; j < n; j++){
		
			if(gard[j][i].first == max_val){
				gard[j][i].second = 1;
			}		
		}
	}

	
	// scan grid for inconsistencies
	for(int i = 0; i < n; i++){
		for(int j = 0; j < m; j++){
			if(gard[i][j].second == 0)
			{
				//output.assign("NO");
				string output("NO");
				//cout << output << endl;
				return output;
			}
		}
	}		
	string output("YES");
	//cout << output << "outside" << endl;
	return output;
}

int main()
{	
	int N;
	cin >> N;

	for(int i = 0; i < N; i++){

		int n,m;
		cin >> n >> m;

		vector< vector< pair<int,int> > >gard(n, vector< pair<int,int> >(m,make_pair(0,0)));

		for(int h = 0; h < n; h++){
			for(int k = 0; k < m; k++){
				cin >> gard[h][k].first; 
			}
		}

		string output = check_feasibility(gard, n, m);
	
		cout << "Case #" << i+1 << ": " << output << endl;
	}
	return 0;
}
