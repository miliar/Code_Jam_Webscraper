#include <bits/stdc++.h>
#define pp pair<char,bool>


using namespace std;

std::vector<pair<char,bool> > all;

pair<char,bool> cross(pair<char,bool> p1, pair<char,bool> p2) {
	pair<char,bool> ret;

	if(p1.first == 'i') {
		if(p2.first == 'j') ret = make_pair('k',true);
		if(p2.first == '1') ret= make_pair('i',true);
		if(p2.first == 'k') ret= make_pair('j',false);
		if(p2.first == 'i') ret= make_pair('1',false);
		if((p1.second || p2.second) && !(p1.second && p2.second)) {
			ret.second = !ret.second;
		}
	}
	if(p1.first == 'j') {
		if(p2.first == 'i') ret = make_pair('k', false);
		if(p2.first == 'j') ret= make_pair('1', false);
		if(p2.first == 'k') ret= make_pair('i', true);
		if(p2.first == '1') ret= make_pair('j', true);
		if((p1.second || p2.second) && !(p1.second && p2.second)) {
			ret.second = !ret.second;
		}
	}
	if(p1.first == 'k') {
		if(p2.first == 'i') ret = make_pair('j',true);
		if(p2.first == 'j') ret= make_pair('i', false);
		if(p2.first == 'k') ret= make_pair('1', false);
		if(p2.first == '1') ret= make_pair('k', true);
		if((p1.second || p2.second) && !(p1.second && p2.second)) {
			ret.second = !ret.second;
		}
	}
	if(p1.first == '1') {
		if(p2.first == 'i') ret = make_pair('i',true);
		if(p2.first == 'j') ret= make_pair('j', true);
		if(p2.first == 'k') ret= make_pair('k', true);
		if(p2.first == '1') ret= make_pair('1', true);
		if((p1.second || p2.second) && !(p1.second && p2.second)) {
			ret.second = !ret.second;
		}
	}

	return ret;
}

void print1(pair<char, bool> p) {
	if(!p.second) {
		cout << "-" << p.first << endl;
	}
	else {
		cout << p.first << endl;
	}
}

int main() {
	all.push_back(make_pair('i',false));
	all.push_back(make_pair('i',true));
	all.push_back(make_pair('j',false));
	all.push_back(make_pair('j',true));
	all.push_back(make_pair('k',false));
	all.push_back(make_pair('k',true));
	all.push_back(make_pair('1',false));
	all.push_back(make_pair('1',true));

	long long int T;
	cin >> T;
	long long int total = T;
	while(T>0) {
		T--;
		long long int L,X;
		cin >> L >> X;
		string str;
		cin >> str;

		vector<std::vector<pp> > prefix;
		vector<std::vector<pp> > suffix;

		pp prev, curr;
		for (long long int group = 0; group < 4 && group<X; ++group)
		{
			std::vector<pp> tmp;
			for (long long int index = 0; index < str.size(); ++index)
			{
				if(index == 0 && group == 0) {
					tmp.push_back(make_pair(str[index],true));
					prev = make_pair(str[index],true);
					continue;
				}
				else {
					curr = make_pair(str[index],true);
					//cout << "prev" << endl;
					//prlong long int1(prev);
					//prlong long int1(curr);
					curr = cross(prev,curr);
					prev = curr;
					tmp.push_back(curr);
				}
			}
			prefix.push_back(tmp);
		}

		for (long long int group = X-1; group > X-5 && group>=0; --group)
		{
			std::vector<pp> tmp;
			for (long long int index = str.size()-1; index >= 0; --index)
			{
				if(index == str.size()-1 && group == X-1) {
					tmp.push_back(make_pair(str[index],true));
					prev = make_pair(str[index],true);
					continue;
				}
				else {
					curr = make_pair(str[index],true);
					curr = cross(curr,prev);
					prev = curr;
					tmp.push_back(curr);
				}
			}
			suffix.push_back(tmp);
		}
		/*for (long long int i = 0; i < suffix.size(); ++i)
		{
			std::vector<pp> tmp = suffix[i];
			cout << "group " << i << endl;
			for (long long int j = 0; j < tmp.size(); ++j)
			{
				prlong long int1(tmp[j]);
			}
		}
		*/
		std::vector<long long int> indexPre;
		for (long long int i = 0; i < prefix.size(); ++i)
		{
			std::vector<pp> tmp = prefix[i];
			//cout << "group " << i << endl;
			for (long long int j = 0; j < tmp.size(); ++j)
			{
				if(j == tmp.size()-1 && i == X-1) continue;
				//cout << "j " << j <<endl;
				//prlong long int1(tmp[j]);
				long long int otherSide;
				long long int nextJ;
				if(j!=tmp.size()-1) {
					otherSide = (X-1)-(i+(((X-1)-i)/4)*4);
					nextJ = j+1;
				}
				else {
					long long int tmpI = i+1;
					nextJ = 0;
					otherSide = (X-1)-(tmpI+(((X-1)-tmpI)/4)*4);
				}
				nextJ = (L-nextJ)-1;
				pp tmpPair = tmp[j];
				//cout << "otherSide " << otherSide << " nextJ " << nextJ << endl;
				if(tmpPair == make_pair('i',true) && 
					suffix[otherSide][nextJ] == make_pair('i',true)) {
					indexPre.push_back(i*L + j);
				}
				//prlong long int1(suffix[otherSide][nextJ]);
				//cout << "end \n";
			}
		}

		/*
		cout << "indexPre \n";
		for (long long int i = 0; i < indexPre.size(); ++i)
		{
			cout << indexPre[i] << endl;
		}
		*/
		std::vector<long long int> indexSuf;
		for (long long int i = 0; i < suffix.size(); ++i)
		{
			std::vector<pp> tmp = suffix[i];
			//cout << "group " << i << endl;
			for (long long int j = 0; j < tmp.size(); ++j)
			{
				pp tmpPair = tmp[j];
				if(tmpPair == make_pair('k',true)) {
					indexSuf.push_back((L*X - 1) - (i*L + j));
				}
				//cout << "end \n";
			}
		}
		/*
		cout << "indexSuf \n";
		for (long long int i = 0; i < indexSuf.size(); ++i)
		{
			cout << indexSuf[i] << endl;
		}
		*/
		bool ans = false;

		long long int minVal = -1;
		for (long long int i = 0; i < indexPre.size(); ++i)
		{
			if(minVal < indexPre[i] || i==0) minVal = indexPre[i]; 
		}

		long long int maxVal = -1;
		for (long long int i = 0; i < indexSuf.size(); ++i)
		{
			if(maxVal > indexSuf[i]) maxVal = indexSuf[i]; 
		}
		if(indexPre < indexSuf) ans = true;

		if(indexSuf.size() == 0 || indexPre.size() == 0) ans = false;
		string ansVal = ans ? "YES" : "NO";		
		cout << "Case #" << total-T << ": " << ansVal << endl;
	}

}