#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <string>
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
#include <cstring>
#include <cassert>
#include <fstream>
#include <cctype>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> ii;

#define sz(a) (a).size()
#define pb push_back
#define fill(a, val) (memset(a,val,sizeof(a)))
#define pow2(x) (1 << (x)) 
#define fin(i,a,n) for(int i = a; i < n; i++)
#define fdc(i,n,a) for(int i = n-1; i >= a; i--)
#define scn(t) scanf("%d",&t)
#define scnt(t) int t;scanf("%d",&t)
#define newline printf("\n")
#define all(v) v.begin(),v.end()
#define MAX 1000000007

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	cin >> t;
	int k  = 1;
	while(t--){
		int counto,countx,count3,countt,fc=0,flag=0;
		string str[4];
		fin(i,0,4)cin >> str[i];
		for(int i = 0; i < 4; i++){
			counto = countx = countt = count3 = 0;
			
			for(int j = 0; j < 4; j++){
				if(str[i][j] == 'O'){
					counto++;	
				}
				else if(str[i][j] == 'X'){
					countx++;	
				}
				else if(str[i][j] == '.'){
					count3++;	
				}
				else if(str[i][j] == 'T'){
					countt++;	
				}
			}	
			if(counto == 4 || (counto == 3 && countt == 1) ){
				cout << "Case #"<<k++<<": O won\n";
				//cout << "111\n";
				flag = 1;
				break;
			}
			else if(countx == 4 || (countx == 3 && countt == 1) ){
				cout << "Case #"<<k++<<": X won\n";
				flag = 1;
				break;
			}
			if(count3 > 0){
				fc = 1;			
			}	
			
		}
		if(flag == 0){
		for(int i = 0; i < 4; i++){
			counto = countx = countt = count3 = 0;
			
			for(int j = 0; j < 4; j++){
				if(str[j][i] == 'O'){
					counto++;	
				}
				else if(str[j][i] == 'X'){
					countx++;	
				}
				else if(str[j][i] == '.'){
					count3++;	
				}
				else if(str[j][i] == 'T'){
					countt++;	
				}
			}	
			if(counto == 4 || (counto == 3 && countt == 1) ){
				cout << "Case #"<<k++<<": O won\n";
				//cout << "222\n";
				flag = 1;
				break;
			}
			else if(countx == 4 || (countx == 3 && countt == 1) ){
				cout << "Case #"<<k++<<": X won\n";
				flag = 1;
				break;
			}
			if(count3 > 0){
				fc = 1;			
			}	
			
		}
		if(flag==0){
			counto = countx = countt = count3 = 0;
			
			for(int i = 0; i < 4; i++){
				if(str[i][i] == 'O'){
					counto++;	
				}
				else if(str[i][i] == 'X'){
					countx++;	
				}
				else if(str[i][i] == '.'){
					count3++;	
				}
				else if(str[i][i] == 'T'){
					countt++;	
				}			
			}
			if(counto == 4 || (counto == 3 && countt == 1) ){
				cout << "Case #"<<k++<<": O won\n";
				//cout << "333\n";
				flag = 1;
				//break;
			}
			else if(countx == 4 || (countx == 3 && countt == 1) ){
				cout << "Case #"<<k++<<": X won\n";
				flag = 1;
				//break;
			}
			if(count3 > 0){
				fc = 1;			
			}
			counto = countx = countt = count3 = 0;
			
			for(int j = 0; j < 4; j++){
				if(str[j][3-j] == 'O'){
					counto++;	
				}
				else if(str[j][3-j] == 'X'){
					countx++;	
				}
				else if(str[j][3-j] == '.'){
					count3++;	
				}
				else if(str[j][3-j] == 'T'){
					countt++;	
				}			
			}
			if(counto == 4 || (counto == 3 && countt == 1) ){
				cout << "Case #"<<k++<<": O won\n";
				flag = 1;
				//cout << "444\n";
				//break;
			}
			else if(countx == 4 || (countx == 3 && countt == 1) ){
				cout << "Case #"<<k++<<": X won\n";
				flag = 1;
				//break;
			}
			if(count3 > 0){
				fc = 1;			
			}		
		}	
		}
		if(flag == 0 && fc == 1){
			cout << "Case #"<< k++ << ": Game has not completed\n";		
		} else if(flag == 0)cout << "Case #" << k++ <<": Draw\n";
		
	}
	return 0;
}
