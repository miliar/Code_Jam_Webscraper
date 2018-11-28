#include <iostream>
#include <algorithm>
#include <math.h>
#include <vector>
#include <stdio.h>
#include <stdlib.h>
#include <map>
#include <utility>

using namespace std;

#define INF 200

int givenMat[104][104];
vector<pair<int, pair<int, int> > >rowMin;

int main(void){
	int T,N,M;
	freopen("B-small-attempt.in", "r", stdin);
	freopen("output.out", "w", stdout);
	//freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);

	scanf("%d",&T);

	for(int t = 0; t < T; t++){
		scanf("%d %d", &N, &M);

		int minEle = INF;
		int x = INF;
		int y = INF;
		rowMin.clear();
		for(int i = 0; i < N; i++){
			minEle = INF;
			for(int j = 0; j < M; j++){
				scanf("%d", &givenMat[i][j]);
				if(givenMat[i][j] < minEle){
					minEle = givenMat[i][j];
					x = i;
					y = j;
				}
			}
			rowMin.push_back(make_pair(minEle,make_pair(x,y)));
		}

		sort(rowMin.begin(), rowMin.end());

		bool possible = true;
		// Algo starts

		for(int j = 0; j < rowMin.size(); j++){
			int minEle = rowMin.at(j).first;
			int x = rowMin.at(j).second.first;
			
			
			int y = rowMin.at(j).second.second;

			for(int p = y; p < M; p++){
				if(minEle != givenMat[x][p])
					continue;

				bool flag = false;

				for(int k = 0; k < M; k++){
					if(givenMat[x][k] > minEle){
						flag = true;
						break;
					}
				}

				if(flag == true){
					for(int k = 0; k <N; k++){
						if(givenMat[k][p] > minEle){
							//cout<<"NO"<<endl;
							possible = false;
							break;
						}
					}
					if(possible == false)
						break;
				}
			}
		}
		if(possible == true)
			cout<<"Case #"<<t+1<<": "<<"YES"<<endl;
		else
			cout<<"Case #"<<t+1<<": "<<"NO"<<endl;
	}

	return 0;
}