#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define ull unsigned long long
#define pb push_back
#define ft first
#define se second
#define mp make_pair
bool eq(int r, int c, int a, int b){
	if((r==a && c==b) || (r==b && c==a)) return true;
	return false;
}
string func(int x, int r, int c){
	string full="GABRIEL", emp="RICHARD";
	if(x==2){
		if(eq(r,c,1,1) || eq(r,c,1,3) || eq(r,c,3,3)) return emp;
	}
	else if(x==3){
		if(eq(r,c,1,1) || eq(r,c,1,2) || eq(r,c,2,2) || eq(r,c,1,3) ||
		   eq(r,c,1,4) || eq(r,c,2,4) || eq(r,c,4,4)) return emp;
	}
	else if(x==4){
		if(eq(r,c,1,1) || eq(r,c,1,2) || eq(r,c,2,2) || eq(r,c,1,3) 
		|| eq(r,c,2,3) || eq(r,c,3,3) || eq(r,c,1,4) || eq(r,c,2,4)) return emp;
	}
	return full;
}
int main(int argc, char const *argv[]){
	int t,p;
	cin>>t;
	p=t;
	while(t--){
		int x,r,c;
		cin>>x>>r>>c;
		cout<<"Case #"<<p-t<<": "<<func(x,r,c)<<endl;
	}
	return 0;
}
