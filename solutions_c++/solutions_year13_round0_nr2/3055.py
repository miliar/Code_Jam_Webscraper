#include <vector>
#include <list>
#include <limits.h>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string.h>
#include <stdlib.h>
using namespace std;

struct Node{
	int x, y;
	int value;
};
Node node[10005];

int cmp(const void *ele1, const void *ele2){
	Node *p=(Node *)ele1, *q=(Node *)ele2;
	return (p->value)-(q->value);
}

int main(){	
	freopen("in.txt","r", stdin);
	freopen("out.txt","w", stdout);
	int t;
	int row, col;
	int arr[101][101];
	bool used[101][101];
	cin>>t;
	for(int k=1; k<=t; k++){
		int counter=0;
		cin>>row>>col;
		memset(used, false, sizeof(used));
		for(int i=0; i<row; i++)
		for(int j=0; j<col; j++){
			cin>>arr[i][j];
			node[counter].x = i;
			node[counter].y = j;
			node[counter].value = arr[i][j];
			counter++;
		}
		qsort(node, row*col, sizeof(Node), cmp);
		bool solution = true;
		for(int i=0; i<counter; i++){
			int x=node[i].x;
			int y=node[i].y;		
			if(solution == false)	
				break;
			if(used[x][y]==true)
				continue;
			bool check = true;
			// in row
			for(int j=0; j<col; j++){
				if(used[x][j]==false && arr[x][j]>arr[x][y]){
					check = false;
					break;
				}
			}
			if(check == true){
				for(int j=0; j<col; j++)
					used[x][j] = true;
				continue;
			}
			check = true;
			// in col
			for(int j=0; j<row; j++){
				if(used[j][y]==false && arr[j][y]>arr[x][y]){
					check = false;
					break;
				}
			}
			if(check==true){
				for(int j=0; j<row; j++)
					used[j][y] = true;
				continue;
			}
			if(check == false)	
				solution = false;		
		}
		if(solution == true)
			cout<<"Case #"<<k<<": YES"<<endl;
		else cout<<"Case #"<<k<<": NO"<<endl;
	}
	//system("pause");
	return 0;
}
