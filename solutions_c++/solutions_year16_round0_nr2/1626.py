
//g++ -o test tesr.cpp

//#include <bits/stdc++.h>
//using namespace std;

#include <iostream>
using std::cin;
using std::cout;
using std::string;
using std::endl;

#include <algorithm> 
using std::sort;
using std::min;
using std::max;
using std::pair;
//pair <int,int> data[100];sort(data,data+100);

#include <math.h>
//sqrt(123.123)
//ceil(0.12)=1
//pow(x,2)=x^2

#include<cstdio>
//printf()

#include <map>
using std::map;
//map <string,int> x;

#include <stdlib.h>
//abs(-123);

#include <vector>
using std::vector;
//vector<int> x;
//x.push_back(0);x.push_back(1);cout<<x[0]<<' '<<x[1];
//x[0]=100;
//x.pop_back();
//vector<int> x(10);     ==>   x[0]==x[1]==...=x[9]==0 default
//x.push_back(100);      ==>   x[10]=100; 
//vector<int> x(10,3);   ==>   x[0]==x[1]==...==x[9]==3;
//vector<int> y(x);      ==>   y[0]==y[1]==...==y[9]==3;
//cout<<x.size();        ==>   10
//x.reserve(4)           ==>   (memory alloc 4) && !(size+=4 don't change size) 

#include <queue>
using std::queue;

#include <deque>
using std::deque;

/*
int gcd(int a, int b)
{ 
    \\O(log(max(a,b)))
    int t;
    while(b!=0)
    {
        t=a%b;
        a=b;
        b=t;
    }
    return a;
    
}
*/

/*
long long C(int x,int y)
{
    long long answer=1;
    int i;
    if(y>x-y)
    {
        y=x-y;
    }
    for(i=1;i<=y;i++)
    {
        answer*=(x+1-i);
        answer/=i;
    }
    return answer;
}

*/

int main() {
  freopen("in", "r", stdin);
  freopen("out", "w", stdout);
  int tt;
  scanf("%d", &tt);
  for (int qq = 1; qq <= tt; qq++) {
    printf("Case #%d: ", qq);
	string s;cin>>s;
	int data[100]={0,};
	int len = s.size();
	int sum=0;
	for(int i=0;i<len;i++){
		if(s[i]=='+')data[i]=1;
		else data[i]=0;
		
		sum+=data[i];
	}
	if(sum==0){
		printf("%d",1);
	}
	else if(sum==len){
		printf("%d",0);
	}
	else{
		int answer=0;
		if(data[0]==0)answer++;
		for(int i=1;i<len;i++){
			if(data[i]==0 && data[i-1]==1)answer+=2;
		}
		printf("%d",answer);
	}	
	printf("\n");
  }
  return 0;
}
