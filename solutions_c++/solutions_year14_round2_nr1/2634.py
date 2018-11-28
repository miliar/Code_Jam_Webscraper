#include <vector>
#include <string>
#include <iostream>
#include <algorithm>
using namespace std;

int T, N, y,
	data[100];
vector<string> str;
string ptrn, tmpstr;

bool Check(string &s){
	int p = 0, i, oi;

	for(i=0 ; i<s.size() && p<ptrn.size() ; i++, p++){
		oi = i;
		while(i<s.size() && s[i] == ptrn[p] )
			i++;
		if(i == oi)
			return false;
		i--;
	}
	return p==ptrn.size() && i==s.size();
}

bool CheckAll(){
	ptrn += str[0][0];
	for(int i=1 ; i<str[0].size() ; i++)
		if(str[0][i] != ptrn[ptrn.size()-1])
			ptrn += str[0][i];

	for(int i=1 ; i<str.size() ; i++){
		if(!Check(str[i])){
			return false;
		}
	}

	return true;
}

void MakeData(){
	int n = ptrn.size();
	memset(data, 0, 100*sizeof(int));
	
	for(int i=0 , p=0; i<str.size() ; i++){
		p=0;
		for(int j=0 ; j<str[i].size() ; j++, p++){
			while(j<str[i].size() && str[i][j] == ptrn[p]){
				data[p]++;
				j++;
			}
		}
	}

	for(int i=0 ; i<ptrn.size() ; i++)
		data[i] /= N;
}

int calc(string &s){
	int d[100], res=0;
	memset(d, 0, 100*sizeof(int));
	for(int i=0, p=0 ; i<s.size() ; i++, p++){
		while(i<s.size() && s[i] == ptrn[p]){
			d[p]++;
			i++;
		}
	}

	for(int i=0 ; i<ptrn.size() ; i++)
		res += abs(d[i] - data[i]);

	return res;
}

void main(){
	freopen("ip.in", "r", stdin);
	freopen("op.txt", "w", stdout);


	cin >> T;

	for(int x=1 ; x<=T ; x++){
		ptrn = "";
		str.clear();

		cin >> N;

		for(int i=0 ; i<N ; i++){
			cin >> tmpstr;
			str.push_back(tmpstr);
		}

		if(!CheckAll()){
			printf("Case #%d: Fegla Won\n", x);
			continue;
		}

		MakeData();

		y=0;
		for(int i=0 ; i<str.size() ; i++){
			y += calc(str[i]);
		}

		printf("Case #%d: %d\n", x, y);
	}
}