#include <bits/stdc++.h>
using namespace std;

int n, t;
vector <pair<int,char> > v;

bool valid(){
	//sort(v.begin(), v.end());
	//int maior = v[v.size()-1].first, cnt = 0;
	int maior = -1, cnt = 0;
	for(int i = 0; i < v.size(); i++){
		if(v[i].first > maior) maior = v[i].first;
		if(v[i].first < 0) return 0;
	}
	for(int i = 0; i < v.size(); i++){
		if(v[i].first == maior) cnt++;
	}

	if(cnt > 1) return 1;
	return 0;
}

void solve(){
	while(v.size() > 0){
		sort(v.begin(), v.end());
		
		/*for(int i = 0; i < v.size(); i++){
			printf("%d -> %c\n", v[i].first, v[i].second);
		}*/

		v[v.size()-1].first -= 2;
		if(valid()){
			printf("%c%c ", v[v.size()-1].second, v[v.size()-1].second);
			if(v[v.size()-1].first == 0) v.erase(v.end()-1);
			continue;
		}
		else{
			v[v.size()-1].first += 2;
		}

		v[v.size()-1].first--;
		v[v.size()-2].first--;
		if(valid()){
			printf("%c%c ", v[v.size()-1].second, v[v.size()-2].second);
			if(v[v.size()-1].first == 0) v.erase(v.end()-1);
			if(v[v.size()-1].first == 0) v.erase(v.end()-1);
			continue;
		}
		else{	
			v[v.size()-1].first++;
			v[v.size()-2].first++;
		}

		v[v.size()-1].first--;
		printf("%c ", v[v.size()-1].second);
		if(v[v.size()-1].first == 0) v.erase(v.end()-1);
	
	}
	//cout << "tamanho = " << v.size() << endl;
}

int main(void){
	scanf("%d", &t);

	for(int k = 1; k <= t; k++){
		v.clear();
		scanf("%d", &n);

		int qnt;
		char letra = 'A';
		for(int i = 0; i < n; i++){
			scanf("%d", &qnt);
			v.push_back(make_pair(qnt, letra));
			letra++;
		}

		printf("Case #%d: ", k);
		solve();
		printf("\n");
	}

	return 0;
}
