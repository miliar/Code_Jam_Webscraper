// Created by alex_mat21. And it works!

#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <queue>
#include <cstring>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <sstream>
#include <stdio.h>
#include <math.h>
#include <bitset>
#include <string> 
#include <iomanip>
#include <cmath>
#include <utility>
 
#define FOR(i,n) for(int i=0,_n=n;i<_n;i++)
#define FORR(i,s,n) for(int i=s,_n=n;i<_n;i++)
#define mp make_pair
#define vi vector<int>
#define fs first
#define sd second
#define pii pair<int,int>

using namespace std;

int main (){
int t111;
cin >> t111;
int r,c;
int a[101][101];
int b[101][101];
string s;
vector < vector <int> > x;
int i1,j1,d1,m,t,t1;
for (int i111=0 ; i111<t111; i111++){
	cin >> r >> c;
	FOR(i,r){
		cin >> s;
		FOR(j,c){
			b[i][j]=0;
			if (s[j]=='.')
				a[i][j]=0;
			else if (s[j]=='^'){
				a[i][j]=1;
				vector <int> v;
				v.push_back(i);
				v.push_back(j);
				v.push_back(1);
				x.push_back(v);
				}
			else if (s[j]=='>'){
				a[i][j]=2;
				vector <int> v;
				v.push_back(i);
				v.push_back(j);
				v.push_back(2);
				x.push_back(v);
				}
			else if (s[j]=='v'){
				a[i][j]=3;
				vector <int> v;
				v.push_back(i);
				v.push_back(j);
				v.push_back(3);
				x.push_back(v);
				}
			else{
				a[i][j]=4;
				vector <int> v;
				v.push_back(i);
				v.push_back(j);
				v.push_back(4);
				x.push_back(v);
				}
			}
		}
	t=1;
	m=0;
	sort(x.begin(),x.end());
	FOR(i,x.size()){
		//cout << x[i][0] << ' ' << x[i][1] << ' ' << t<< endl;
		i1=x[i][0];
		j1=x[i][1];
		d1=a[i1][j1];
		while (i1>=0 && i1<r && j1>=0 && j1<c && (a[i1][j1]==0 || (i1==x[i][0] && j1==x[i][1]))){
			if (d1==1)
				i1--;
			else if (d1==2)
				j1++;
			else if (d1==3)
				i1++;
			else
				j1--;
			}
		if (not (i1>=0 && i1<r && j1>=0 && j1<c)){
			m++;
			t1=0;
			i1=x[i][0];
			FOR(l,c){
				if (a[i1][l]>0 and l!=x[i][1]){
					t1=1;
					break;
					}
				}
			//cout << t1 << endl;
			j1=x[i][1];
			FOR(l,r){
				if (a[l][j1]>0 and l!=x[i][0]){
					t1=1;
					break;
					}
				}
			//cout << t1 << endl;
			if (t1==0){
				t=0;
				break;
				}
			}
		}
	if (t==0)
		cout << "Case #"<< i111 +1 << ": IMPOSSIBLE"<< endl;
	else
		cout << "Case #"<< i111 +1 << ": "<< m<< endl;
	x.clear();
	}
return 0;
}
