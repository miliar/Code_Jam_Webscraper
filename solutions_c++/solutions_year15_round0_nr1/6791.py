#define _CRT_SECURE_NO_WARNINGS
#define F(i,s,r) for(int i=s;i<r;i++)
#define FE(i,s,r) for(int i=s;i<=r;i++)
#define R(i,s,r) for(int i=s;i>=r;i--)
#define IsOdd(a) (a&1)?(1):0
#define IsDivByN(a,n) (a%n==0)?1:0
#include<cstdio>
#include<iostream>
#include<vector>
#include<ctime>
#include<string>
#include<stack>
#include<algorithm>
#include<queue>
using namespace std;
int shy[1002];
string s;
int T,s_max;
void min_frnd(int c){
	int  min= 0;
	int alreaady_standing = shy[0];
	FE(i, 1, s_max){
		if (alreaady_standing < i){
			min+= i - alreaady_standing;
			alreaady_standing = i+ shy[i];
		}
		else{
			alreaady_standing += shy[i];
		}
	}
	printf("Case #%d: %d\n",c,min);
}
int main(){
//	freopen("input.txt","r",stdin);
//	freopen("out.out", "w", stdout);
	cin >> T;
	FE(j, 1, T){
		cin >> s_max >> s;
		F(i, 0, s.length()){
			switch (s[i])
			{
			case '0':shy[i] = 0;
				break;
			case '1':shy[i] = 1;
				break;
			case '2':shy[i] = 2;
				break;
			case '3':shy[i] = 3;
				break;
			case '4':shy[i] = 4;
				break;
			case '5':shy[i] = 5;
				break;
			case '6':shy[i] = 6;
				break;
			case '7':shy[i] = 7;
				break;
			case '8':shy[i] = 8;
				break;
			case '9':shy[i] = 9;
				break;
			default:
				break;
			}
		}
		min_frnd(j);
	}
}