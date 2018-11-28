
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
	printf("\n");
	int N,J;
	scanf("%d%d",&N,&J);
	
	
	//big input	
	//output "1000 0mkh gfmk hgf1 1000 0edc baed cba1"  all of them can be divided by  x^5+1
	//(X^31+x^16+x^15+1)=(x^15+1)(x^16+1)=(x^5+1)(x^10-2x^10+1)
	string answer=" 33 244 1025 3126 7777 16808 32769 59050 100001 \n";
	int a=0,b=0,c=0,d=0,e=0,f=0,g=0,h=0,k=0,m=0;
	int cur;
	for(int i=0;i<500;i++){
		cur=i;
		a=cur%2;cur/=2;
		b=cur%2;cur/=2;
		c=cur%2;cur/=2;
		d=cur%2;cur/=2;
		e=cur%2;cur/=2;
		f=cur%2;cur/=2;
		g=cur%2;cur/=2;
		h=cur%2;cur/=2;
		k=cur%2;cur/=2;
		m=cur%2;cur/=2;
		printf("%d%d%d%d%d%d%d%d%d%d%d%d%d%d%d%d%d%d%d%d%d%d%d%d%d%d%d%d%d%d%d%d",
			1,0,0,0,
			0,m,k,h,
			g,f,m,k,
			h,g,f,1,
			
			1,0,0,0,
			0,e,d,c,
			b,a,e,d,
			c,b,a,1);
		cout<<answer;
	}
	
	//small input
	/*
	string answer=" 33 244 1025 3126 7777 16808 32769 59050 100001 \n";	
	int a=0,b=0,c=0,d=0,e=0;
	int cur;
	//32 of 50(1-32)
	for(int i=0;i<32;i++){
		cur=i;
		printf("10000");
		a=cur%2;cur/=2;
		b=cur%2;cur/=2;
		c=cur%2;cur/=2;
		d=cur%2;cur/=2;
		e=cur%2;cur/=2;
		printf("%d%d%d%d%d%d%d%d%d%d",e,d,c,b,a,e,d,c,b,a);
		printf("1");
		cout<<answer;
	}	
	//15 of 50(33-47)
	for(int i=1;i<16;i++){
		cur=i;
		printf("1");
		a=cur%2;cur/=2;
		b=cur%2;cur/=2;
		c=cur%2;cur/=2;
		d=cur%2;cur/=2;
		e=cur%2;cur/=2;
		printf("%d%d%d%d%d%d%d%d%d%d",d,c,b,a,e,d,c,b,a,e);
		printf("00001");
		cout<<answer;
	}
	//48-50
	printf("1100001001000011");cout<<answer;
	printf("1010000101000011");cout<<answer;
	printf("1001000011000011");cout<<answer;
	*/
  }
  return 0;
}
