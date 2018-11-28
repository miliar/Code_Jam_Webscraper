#include <vector>
#include <string>
#include <iostream>
#include <fstream>

#define FILE
#define MAX 101

using namespace std;

bool searchStraight(vector<vector<int> > &list,int posX,int posY)
{
	bool isStraight = false;
	int width = (int)list[posY].size();
	for (int x=0; x<width; ++x) {
		if (list[posY][x] == MAX) {
			if (x == width-1) {
				isStraight = true;
			}
		}
		else{
			break;
		}
	}
	
	int height = (int)list.size();
	for (int y=0; y<height; ++y) {
		if (list[y][posX] == MAX) {
			if (y == height-1) {
				isStraight = true;
			}
		}
		else{
			break;
		}
	}
	
	return isStraight;
}

bool check(vector<vector<int> > &list,int width,int height)
{
	for(int x=0;x<width;++x){
		for (int y=0; y<height; ++y) {
			if(list[y][x] == MAX){
				if(!searchStraight(list,x,y)){
					return false;
				}
			}
		}
	}
	return true;
}

int searchMin(vector<vector<int> >&list)
{
	int height = (int)list.size();
	int width = (int)list[0].size();
	int min = 101;
	for (int x=0; x<width; ++x) {
		for (int y=0; y<height; ++y) {
			if (min > list[y][x]) {
				min = list[y][x];
			}
		}
	}
	return min;
}

void fillMin(vector<vector<int> > &list,int min)
{
	int height = (int)list.size();
	int width = (int)list[0].size();
	for (int x=0; x<width; ++x) {
		for (int y=0; y<height; ++y) {
			if (list[y][x] == min) {
				list[y][x] = MAX;
			}
		}
	}
}

bool solve(vector<vector<int> > &list,int width,int height)
{
	int min = searchMin(list);
	while (min != MAX) {
		min = searchMin(list);
		fillMin(list,min);
		if(!check(list,width,height)){
			return false;
		}
	}
	return true;
}

int main()
{
	int num;
	int width,height;
	
#ifdef FILE
	ifstream ifs( "/Users/iseki/Downloads/B-large.in" );
	ifs >> num;
#endif
#ifndef FILE
	cin >> num;
#endif
	ofstream ofs("/Users/iseki/Downloads/ans.dat");
	vector<vector<int> > list;
	for (int i=0; i<num; ++i) {
#ifndef FILE
		cin >> height;
		cin >> width;
#endif
#ifdef FILE
		ifs >> height;
		ifs >> width;
#endif
		
		
		vector<int> work;
		int tmp;
		for (int y=0; y<height; ++y) {
			for (int x=0; x<width; ++x) {
#ifndef FILE
				cin >> tmp;
#endif
#ifdef FILE
				ifs >> tmp;
#endif
				work.push_back(tmp);
			}
			list.push_back(work);
			work.clear();
		}
		
		string result;
		if(solve(list,width,height)){
			result = "YES";
		}
		else {
			result = "NO";
		}
		cout << "Case #" << i+1 << ": " ;
		ofs << "Case #" << i+1 << ": " ;
		cout << result << endl;
		ofs << result << endl;
		
		list.clear();
	}
	
	return 0;
}