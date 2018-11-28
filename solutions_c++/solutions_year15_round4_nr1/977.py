#include <bits/stdc++.h>

using namespace std;

int n,m;
char M[110][110];


vector<pair<int,int> > next(pair<int,int> pos){

	vector<pair<int,int> > lol;

	for(int j = pos.second+1;j<m;j++){
		if(M[pos.first][j]!='.'){
			lol.push_back(make_pair(pos.first,j));
			break;
		}
	}
	if(lol.size()!=1)
		lol.push_back(make_pair(-1,-1));

	for(int j = pos.second-1;j>=0;j--){
		if(M[pos.first][j]!='.'){
			lol.push_back(make_pair(pos.first,j));
			break;
		}
	}
	if(lol.size()!=2)
		lol.push_back(make_pair(-1,-1));

	for(int i = pos.first+1;i<n;i++){
		if(M[i][pos.second]!='.'){
			lol.push_back(make_pair(i,pos.second));
			break;
		}
	}
	if(lol.size()!=3)
		lol.push_back(make_pair(-1,-1));

	for(int i = pos.first-1;i>=0;i--){
		if(M[i][pos.second]!='.'){
			lol.push_back(make_pair(i,pos.second));
			break;
		}
	}
	if(lol.size()!=4)
		lol.push_back(make_pair(-1,-1));
	return lol;
}

int main(){

	char mapa[1000];
	mapa['>'] = 0;
	mapa['<'] = 1;
	mapa['^'] = 3;
	mapa['v'] = 2;

	int t,ca = 1;
	scanf("%d",&t);
	while(t--){
		printf("Case #%d: ",ca++);
		scanf("%d %d",&n,&m);
		vector<pair<int,int> > v;
		for(int i = 0;i<n;i++){
			for(int j = 0;j<m;j++)
			{
				scanf(" %c",&M[i][j]);
				if(M[i][j]!='.')
					v.push_back(make_pair(i,j));
			}
		}

		int resp = 0;
		for(int i = 0;i<v.size();i++){
			vector<pair<int,int> > x = next(v[i]);
			for(int j = 0;j<4;j++){
				if(x[j].first !=-1)break;
				if(j == 3)
					resp = -1;
			}
			if(resp == -1)
				break;
			if(x[mapa[M[v[i].first][v[i].second]]].first==-1)
				resp++;

		}
		if(resp == -1)
			printf("IMPOSSIBLE\n");
		else
			printf("%d\n",resp);
	}
	return 0;
}