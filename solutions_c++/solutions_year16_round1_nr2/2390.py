#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <string>
#include <algorithm>
using namespace std;

ifstream fin("b.in");
ofstream fout("b.out");

const int MAX_HEIGHT = 2501;

int N;
vector< vector<int> > lists;
vector<int> missing;
int grid[50][50];

pair<int,bool> miss;


void fillzero() {
	for(int i=0; i<N; i++)
		for(int j=0; j<N; j++)
			grid[i][j] = 0;
}
void printgrid() {
	for(int i=0; i<N; i++) {
		for(int j=0; j<N; j++)
			cout << grid[i][j] << " ";
		cout << endl;
	}
	cout << "-----" << endl;
}

bool rowcol(int i, vector<int> &l1, vector<int> &l2) {
	for(int j=0; j<i; j++) {
		if(grid[i][j]!=l1[j] || grid[j][i]!=l2[j])
			return false;
	}
	for(int j=i+1; j<N; j++) {
		if(grid[i-1][j]>l1[j] || grid[j][i-1]>l2[j])
			return false;
	}
	return true;
}

pair<int,int> findsmallest(int i) {
	int min = MAX_HEIGHT;
	vector<int> occur;
	cout << "list size " << (int)lists.size() << endl;
	for(int j=0; j<(int)lists.size(); j++) {
		if((int)lists.size()==2)
			cout << min << " " << lists[j][i] << endl;
		if(lists[j][i]<min) {
			occur.clear();
			min = lists[j][i];
			occur.push_back(j);
		}
		else if(lists[j][i]==min) {
			occur.push_back(j);
		}
	}
	if((int)occur.size()==1)
		occur.push_back(-1);
	return make_pair<int,int>(occur[0],occur[1]);
}

bool fitsrow(int i, vector<int> &list) {
	for(int j=0; j<i; j++) {
		if(grid[i][j]>0 && list[j]!=grid[i][j])
			return false;
	}
	return true;
}

void fillrow(int i, vector<int> &list) {
	if(list.empty()) {
		miss.first = i;
		miss.second = true;
	}
	else {
		for(int j=0; j<N; j++)
			grid[i][j] = list[j];
	}
}
void fillcol(int i, vector<int> &list) {
	if(list.empty()) {
		miss.first = i;
		miss.second = false;
	}
	else {
		for(int j=0; j<N; j++)
			grid[j][i] = list[j];
	}
}

void eraselists(int i, int j) {
	int max = (i>j)?i:j;
	int min = (i>j)?j:i;
	lists.erase(lists.begin()+max);
	lists.erase(lists.begin()+min);
}

void fillgrid(int i, pair<int,int> l) {
	vector<int> first = lists[l.first];
	vector<int> second = lists[l.second];
	bool row = rowcol(i, first, second);
	if(row) {
		fillrow(i,first);
		fillcol(i,second);
	}
	else {
		fillrow(i,second);
		fillcol(i,first);
	}
	eraselists(l.first, l.second);
}

void constructmissing(int i, int l) {
	map<int,int> missingno;
	for(int j=0; j<(int)lists.size(); j++) {
		int el = lists[j][i];
		if(missingno.count(el)==0)
			missingno[el] = 1;
		else
			missingno[el]++;
	}
	for(int j=i; j<N; j++) {
		int el = lists[l][j];
		missingno[el]--;
		if(missingno[el]==0)
			missingno.erase(el);
	}
	vector<int> tail;
	map<int,int>::iterator it;
	for(it=missingno.begin(); it!=missingno.end(); it++) {
		tail.push_back(it->first);
	}
	if(fitsrow(i, lists[l])) {
		for(int j=0; j<i; j++)
			missing.push_back(grid[j][i]);
	}
	else {
		for(int j=0; j<i; j++)
			missing.push_back(grid[i][j]);
	}
	missing.push_back(lists[l][i]);
	missing.insert(missing.end(), tail.begin(), tail.end());
}

void findmissing() {
	for(int i=0; i<N; i++) {
		printgrid();
		pair<int,int> p = findsmallest(i);
		cout << "smallest: " << p.first << " " << p.second << endl;
		if(p.second==-1) {
			constructmissing(i, p.first);
			break;
		}
		fillgrid(i,p);
	}
}

int main() {

	int T;
	fin >> T;
	for(int t=1; t<=T; t++) {
		cout << "CASE " << t << endl;
		lists.clear();
		missing.clear();
		fin >> N;
		fillzero();
		for(int i=0; i<2*N-1; i++) {
			vector<int> list;
			for(int j=0; j<N; j++) {
				int x;
				fin >> x;
				list.push_back(x);
			}
			lists.push_back(list);
		}
		findmissing();
		fout << "Case #" << t << ": ";
		for(int i=0; i<N; i++)
			fout << missing[i] << " ";
		fout << endl;
	}

	return 0;
}

