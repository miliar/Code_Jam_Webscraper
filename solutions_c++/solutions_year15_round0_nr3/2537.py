#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cstring>
#include <cmath>
#include <map>

using namespace std;

map<int, map<int, int> > xx;

bool solve_zero(char * com, int start , int end) {
	if(start > end) return false;
	int cur;
        if(com[start]=='1')cur = 1;
        else if(com[start]=='i') cur = 2;
        else if(com[start]=='j') cur = 3;
        else cur = 4;
	while(start != end) {
		int abscur = abs(cur);
                int i;
		start++;
                if(com[start]=='1')i = 1;
                else if(com[start]=='i') i = 2;
                else if(com[start]=='j') i = 3;
                else i = 4;
                int final = xx[abscur][i];
                if(cur<0)cur=-final;
		else cur = final;
	}
	if(cur == 4) return true;
	else return false;
}

bool solve_one(char * com, int start , int end) {
	if(start >= end)return false;
	int cur;
	if(com[start]=='1')cur = 1;
        else if(com[start]=='i') cur = 2;
        else if(com[start]=='j') cur = 3;
       	else cur = 4;
	while(start<end) {
                if(cur==3) {
                        if(solve_zero(com, start+1,end))return true;
                }
                int abscur = abs(cur);
                int i;
                start++;
                if(com[start]=='1')i = 1;
                else if(com[start]=='i') i = 2;
                else if(com[start]=='j') i = 3;
                else i = 4;
                int final = xx[abscur][i];
                if(cur<0)cur=-final;
		else cur = final;
	}
	return false;
}

bool solve_two(char * com, int start , int end) {
	start = 0;
	int cur;
	if(com[0]=='1')cur = 1;
	else if(com[0]=='i') cur = 2;
	else if(com[0]=='j') cur = 3;
	else cur = 4;
	int flag = 0;
	while(start<end) {
		//if(cur==2) {		
			//printf("i at length %d\n", start);
		//	if(solve_one(com, start+1,end))return true;
		//}
		if(flag==0) {
			if(cur==2)flag=1;
		}
		else if(flag == 1) {
			if(cur==4)flag=2;
		}
		int abscur = abs(cur);
		int i;
		start++;
		if(com[start]=='1')i = 1;
	        else if(com[start]=='i') i = 2;
        	else if(com[start]=='j') i = 3;
	        else i = 4;
		int final = xx[abscur][i];
		if(cur<0)cur=-final;
		else cur = final;
	}
	if(flag ==2 && cur==-1)return true;
	return false;
}

void solve_problem(int caseno) {
	int l,x;
	cin >> l >> x;
	char * str;
	str = (char *)malloc(10001*sizeof(char));
	scanf("%s", str);
	char * com;
	com = (char *)malloc(10001*sizeof(char));
	strcpy(com,str);
	int i;
	for(i=2;i<=x;i++)strcat(com,str);
	//printf("hello\n");
	if(solve_two(com, 0, l*x-1)) printf("Case #%d: YES\n", caseno);
	else printf("Case #%d: NO\n", caseno);
}

int main() {
	xx[1][1]=1;
	xx[1][2]=2;
	xx[1][3]=3;
	xx[1][4]=4;
	xx[2][1]=2;
	xx[2][2]=-1;
	xx[2][3]=4;
	xx[2][4]=-3;
	xx[3][1]=3;
	xx[3][2]=-4;
	xx[3][3]=-1;
	xx[3][4]=2;
	xx[4][1]=4;
	xx[4][2]=3;
	xx[4][3]=-2;
	xx[4][4]=-1;
	
	int cases;
	scanf("%d",&cases);
	int i;
	for(i=0;i<cases;i++) solve_problem(i+1);
	return 0;
}
