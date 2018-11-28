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
	vvi mas(4, vi(4)),asd(4, vi(4));
	int ans1,ans2;
	int n;
	in>>n;
	for(int i=0;i<n;i++){
		in>> ans1;
		for(int j=0;j<4;j++)
			for(int k=0;k<4;k++)
				in>>mas[j][k];
		in>> ans2;
		for(int j=0;j<4;j++)
			for(int k=0;k<4;k++)
				in>>asd[j][k];
		int c=0,g=-1;
		for(int j=0;j<4;j++)
			for(int k=0;k<4;k++)
				if(mas[ans1-1][j]==asd[ans2-1][k]){
					c++;
					g=j;
				}
		if(c==1)
			out<<"Case #"<<i+1<<": "<<mas[ans1-1][g];
		else if(c==0)
			out<<"Case #"<<i+1<<": Volunteer cheated!";
		else 
			out<<"Case #"<<i+1<<": Bad magician!";
		out<<endl;
	}
	in.close();
	out.close();
	return 0;
}	
