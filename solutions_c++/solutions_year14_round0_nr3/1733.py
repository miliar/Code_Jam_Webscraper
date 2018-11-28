#include <iostream>
#include <fstream>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <iomanip>
#include <queue>
using namespace std;
#define MAX 2600
int t, r, c, m, cnt(0), b[MAX], visit[MAX];
int dr[] = {-1, 1, 0, 0, -1, -1, 1, 1};
int dc[] = {0, 0, -1, 1, -1, 1, -1, 1};
bool flag = false;
ifstream fin("C-small-attempt0.in");
bool notsat();
bool allvisit();
int idxback(int row, int col);
int colnum(int idx);
int rownum(int idx);
bool isc(int index);
int findc();
void bfs(int index);
void perm(int prev);
int main()
{
	cin.rdbuf(fin.rdbuf());
	cin >> t;
	while(t --){
		flag = false;
		cin >> r >> c >> m;
		memset(b, 0, MAX * sizeof(int));
		perm(0);
		if(!flag)
			cout << "Case #" << ++ cnt << ":" << endl << "Impossible" << endl;
	}
}
void perm(int prev)
{
	if(prev == r * c){
		if(notsat())
			return;
		int index = findc();
		if(index == -1){
			if(m + 1 == r * c){
				cout << "Case #" << ++ cnt << ":" << endl;
				for(int i = 0; i < r; ++ i){
					for(int j = 0; j < c; ++ j){
						if(i == 0 && j == 0)
							cout << 'c';
						else
							cout << '*';
					}
					cout << endl;
				}
				flag = true;
			}
			return;
		}
		bfs(index);
		return;
	}
	for(int i = 0; i < 2; ++ i){
		if(flag)
			return;
		b[prev] = i;
		perm(prev + 1);
	}
}
bool notsat()
{
	int bcnt(0);
	for(int i = 0; i < r * c; ++ i)
		if(b[i])
			++ bcnt;
	if(bcnt != m)
		return(true);
	else
		return(false);
}
void bfs(int index)
{
	memset(visit, 0, MAX * sizeof(int));
	queue<int> q;
	q.push(index);
	visit[index] = 1;
	while(!q.empty()){
		int p = q.front(); q.pop();
		int row = rownum(p), col = colnum(p);
		for(int i = 0; i < 8; ++ i){
			int rr = row + dr[i], cc = col + dc[i];
			if(rr >= 0 && rr < r && cc >= 0 && cc < c){
				int tidx = idxback(rr, cc);
				if(isc(tidx) && !visit[tidx])
					q.push(tidx);
				visit[tidx] = 1;
			}
		}
	}//while(!q.empty())
	if(allvisit()){
		cout << "Case #" << ++ cnt << ":" << endl;
		for(int i = 0; i < r; ++ i){
			for(int j = 0; j < c; ++ j){
				int uidx = idxback(i, j);
				if(b[uidx])
					cout << '*';
				else if(uidx == index)
					cout << 'c';
				else
					cout << '.';
			}
			cout << endl;
		}
		flag = true;
	}
}
int findc()
{
	for(int i = 0; i < r * c; ++ i){
		if(isc(i))
			return(i);
	}	
	return(-1);
}
bool isc(int index)
{
	if(b[index])
		return(false);
	int row = rownum(index), col = colnum(index);
	for(int i = 0; i < 8; ++ i){
		int rr = row + dr[i], cc = col + dc[i];
		int tidx = idxback(rr, cc);
		if(rr >= 0 && rr < r && cc >= 0 && cc < c &&
				b[tidx] == 1)
			return(false);
	}
	return(true);
}
int rownum(int idx)
{
	return(idx / c);
}
int colnum(int idx)
{
	return(idx % c);
}
int idxback(int row, int col)
{
	return(row * c + col);
}
bool allvisit()
{
	for(int i = 0; i < r * c; ++ i)
		if(b[i] == 0 && visit[i] == 0)
			return(false);
	return(true);
}
