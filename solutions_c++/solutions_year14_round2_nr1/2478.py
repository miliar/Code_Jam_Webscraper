// GCJ 2014 1B a 
// Template

#include <iostream>
#include <vector>
#include <set>
#include <queue>
#include <map>
#include <algorithm>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
using namespace std;

#define REP(i,a,b) for(int i=a; i <b; i++)

// printf("");
// scanf("",&);


int T;
int cases=0;
int err;

int N;
char c, lastC;
int cnt;
int sum;

typedef pair<char, int> ci;

typedef vector<ci > vci;
typedef vector<vci > vvci;

vvci strings;

int main(){

	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);

	cin >> T;
	cin.ignore();
	while(cases++<T){
		printf("Case #%d: ",cases);

		//input
		err=0;

		cin >> N;
		cin.ignore();
		
		strings.clear();
		
		REP(i,0,N){
			cnt = 0;
			lastC = ' ';
			vci str;
			do{
				c = getchar();

				if(lastC==' ') lastC = c;	// base case

				if(lastC == c){	// smae
					cnt++;
				}else{			//diff
					str.push_back(pair<char,int>(lastC,cnt));
					cnt=1;
					lastC = c;
				}
			}while(c!='\n');
			strings.push_back(str);
		}

		// body
		int steps = 0;
		int I = strings[0].size();
		int center;
		REP(n,0,N){
		if(strings[n].size()!=I){	// not the same config
				err=1;
				break;
			}
		}

		if(!err)
		REP(i,0,I){
			
			sum=0;
			c = ' ';
			REP(n,0,N){
				ci p = strings[n][i];	// the pair

				if(c==' ') c = p.first;
				if(p.first != c){	// not the same config
					err=1;
					break;
				}
				sum+= p.second;
			}
			center = sum/N>1? sum/N: 1;

			REP(n,0,N){
				ci p = strings[n][i];	// the pair
				if(p.second<center)steps += center-p.second;
				if(p.second>center)steps += p.second-center;
			}

		}
		
		if(err){
			printf("Fegla Won\n",steps);
		}else{

			printf("%d\n",steps);
		}
	}


	


return 0;
}