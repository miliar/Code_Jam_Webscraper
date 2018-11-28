#include <iostream>
#include <vector>
#include <cstdio>
#include <string>
#include <set>
#include <cmath>
#include <map>
#include <algorithm>
#include <list>
#include <functional>
using namespace std;

int main(){
	freopen("in.txt" , "r" , stdin);
	freopen("out.txt" , "w" , stdout);
	int T;
	scanf("%d" , &T);
	for (int t = 0; t < T; t++)
	{
		printf("Case #%d: " , t+1);
		int n;
		scanf("%d" , &n);
		string str1 , str2 , tmp1 = "", tmp2 = "";
		cin >> str1 >> str2;
		for (int i = 0; i < str1.size()-1; i++)
		{
			if(str1[i] != str1[i+1])
				tmp1 += str1[i];
		}
		tmp1 += str1[str1.size()-1];
		for (int i = 0; i < str2.size()-1; i++)
		{
			if(str2[i] != str2[i+1])
				tmp2 += str2[i];
		}
		tmp2 += str2[str2.size()-1];
		//cout << endl;
		//cout << tmp1 << endl << tmp2 << endl;
		if(tmp1 != tmp2) printf("Fegla Won\n");
		else{
			int index_i , index_j , ans = 0;
			for (int a = 0 , b=0; a < str1.size(); a++ , b++)
			{
				index_i = index_j = 0;
				char sym = str1[a];
				while (a < str1.size() && sym == str1[a]) a++ , index_i++;
				a--;
				sym = str2[b];
				while (b < str2.size() && sym == str2[b]) b++ , index_j++;
				b--;
				ans += abs(index_i - index_j);
			}
			printf("%d\n" , ans);
		}
	}

	return 0;
}

/*
#include <iostream>
#include <vector>
#include <cstdio>
#include <string>
#include <set>
#include <map>
#include <algorithm>
#include <list>
#include <functional>
using namespace std;

int main(){
freopen("in.txt" , "r" , stdin);
freopen("out.txt" , "w" , stdout);
int T;
vector<string> vec ;
scanf("%d" , &T);
for (int t = 0; t < T; t++)
{
int Calc = 0;
vec.clear();
printf("Case #%d: " , t+1);
int n;
scanf("%d" , &n);
vec.resize(n);
for (int i = 0; i < n; i++)
cin >> vec[i];

bool con = true , con2 = true;;
vector<int> Cont;
while (true)
{
char last = 0;
for (int i = 0; i < n; i++)
{
if(vec[i].empty()) {
con2 = false;
break;
}
char sym = vec[i][0];
if(i > 0){
if(sym != last){
con = false;
break;
}
}
int j = 0;
last = sym;
while (j < vec[i].size() && vec[i][j] == sym)
{
j++;
}
Cont.push_back(j);
vec[i] = vec[i].substr(j);
}
if(!con2) break;
if(!con) break;
sort(Cont.begin() , Cont.end() );
if(Cont.size() % 2 == 1){
int mid = Cont[Cont.size()/2];
for (int k = 0; k < Cont.size(); k++)
{
Calc += abs(mid - Cont[k]);
}
}
else
{
int mid1 = Cont[Cont.size()/2] , mid2 = Cont[Cont.size()/2 - 1];
int c1 = 0 , c2 = 0;
for (int k = 0; k < Cont.size(); k++)
{
c1 += abs(mid1 - Cont[k]);
c2 += abs(mid2 - Cont[k]);
}
Calc += min(c1 , c2);
}
Cont.clear();
} 
if(con){
for (int i = 0; i < vec.size(); i++)
{
if(vec[i].size() > 0){
con = false;
break;
}
}
if(con) printf("%d\n" , Calc);
else {
printf("Fegla Won\n");
}
}
else {
printf("Fegla Won\n");
}
}
return 0;
}
*/

/* B
#include <iostream>
#include<cstdio>
#include<vector>
#include <stack>
#include <list>
#include <algorithm>
#include <set>
using namespace std;

#define VISITED true
#define NOT_VISITED false

vector <bool> visited;
int n , Min = INT_MAX;
vector< vector <int> > AdjList;

int CheckRoot(int root){
visited[root] = VISITED;
int c = 0;
multiset<int> Set;
multiset<int> :: reverse_iterator it;
for (int j = 0; j < AdjList[root].size() ; j++) 
{
if ( AdjList[root][j] != root && visited[ AdjList[root][j] ] == NOT_VISITED )
{
c = (1 + CheckRoot( AdjList[root][j] )); 
Set.insert(c);
}
}
c = 0; 
if(Set.size() < 2) return 0;
it = Set.rbegin();
for (int j = 0; j < 2; j++ , it++)
c += *it;
return c;
}
void rec( ){
int del = 0;
for (int i = 0; i < n; i++)
{
int L = CheckRoot(i);
Min = min(Min , n - L-1);
for (int j = 0; j < (int)visited.size(); j++)
{
visited[j] = NOT_VISITED;
}
}
}

int main( )
{
freopen("in.txt" , "r" , stdin);
freopen("out.txt" , "w" , stdout);
int T;
scanf("%d" , &T);
for (int i = 0; i < T; i++)
{
printf("Case #%d: " ,i+1);
Min = INT_MAX;
for (int j = 0; j < AdjList.size(); j++)
{
AdjList[j].clear();
}
AdjList.clear();
visited.clear();
scanf("%d" , &n);
AdjList.resize(n);
visited.resize(n);
for (int j = 0; j < n-1; j++)
{
int src , dst;
scanf("%d%d" , &src , &dst);
AdjList[src-1].push_back(dst-1);
AdjList[dst-1].push_back(src-1);
}
rec();
printf("%d\n" , Min);
}
return 0;
}

*/