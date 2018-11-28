#include <cstdlib>
#include <fstream>
#include <iostream>
#include <string>
#include <string.h>
#include <algorithm>
#include <cmath>
#include <vector>
#include <stack>
#include <set>
#define ll long long
#define vi vector<int>
#define vvi vector<vector <int>>
#define pb push_back
#define mp make_pair
#define inf 100000000
//const double pi=3.14159265359;
using namespace std;
struct point{
	int x,y;
};
struct len{
	double A,B,C;
};
struct okr{
	double x,y,r;
};
double dist(point a,point b){
	return (double)((a.x-b.x)*(a.x-b.x)+(a.y-b.y)*(a.y-b.y));
}
vi  prefix_func(string s){
	int n=s.length();
	vi pi(n);
	for(int i=1;i<n;i++){
		int j=pi[i-1];
		while(j>0 && s[i]!=s[j])
			j=pi[j-1];
		if(s[i]==s[j])j++;
		pi[i]=j;
	}
	return pi;
}

int main(){
	ifstream in("INPUT.TXT");
	ofstream out("OUTPUT.TXT");
	//ifstream in(stdin);
	//ofstream out(stdout);
	double t,c,x,f;
	in>>t;
	out.precision(30);
	for(int i = 0;i < t;i++){
		in >> c >> f >> x;
		double speed=2,time=0,mint=x/2,ct=0;
		for(int i = 0;i < 100000;i++){
			ct =c/speed + ct;
			time = ct + x/(speed + f);
			speed += f;
			mint=min(mint,time);
		}		
		out<<"Case #"<<i+1<<": "<<mint<<endl;;
	}
	in.close();
	out.close();
	return 0;
}	
