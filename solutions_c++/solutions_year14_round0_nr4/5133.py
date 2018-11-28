#include<iostream>
#include<vector>
#include<algorithm>
#include<fstream>
using namespace std;


int game1(vector<float> &nao, vector<float> &ken){
	int len = nao.size();
	int res = 0;
	int idx = 0;
	for(int i = 0;i < len;i ++){
		if(nao[i] <= ken[idx]){
			continue;
		}
		else{
			++ res;
			++ idx;
		}
	}
	return res;
}

int game2(vector<float>& nao, vector<float> &ken){
	int len = nao.size();
	int res = len;
	int idx = 0;
	for(int i = 0;i < len && idx < len; ++ i){
		//cout << nao[i] << ' ' << ken[idx] <<endl;
		while(idx < len && nao[i] > ken[idx]){
			++ idx;
		}
		if(idx == len) break;
		-- res;
		++ idx;
	}
	return res;
}

int main(){
	int T;
	cin >> T;
	int idx = 0;
	ofstream fout;
	fout.open("data.txt", ios::app);
	while(idx < T){
		++ idx;
		int n;
		cin >> n;
		vector<float> nao(n);
		vector<float> ken(n);
		for(int i = 0;i < n;i ++)
			cin >> nao[i];
		for(int i = 0;i < n;i ++)
			cin >> ken[i];
		int res1, res2;
		sort(nao.begin(), nao.end());
		sort(ken.begin(), ken.end());
//		for(int i = 0;i < n;i ++)
//			cout << nao[i] << ' ';
//		cout << endl;
//		for(int i = 0;i < n;i ++)
//			cout << ken[i] << ' ';
//		cout << endl;
		cout << "Case #"<< idx << ": " << game1(nao, ken) << ' ' << game2(nao, ken) <<endl;
		fout << "Case #"<< idx << ": " << game1(nao, ken) << ' ' << game2(nao, ken) <<endl;
	}
	return 0;
}
