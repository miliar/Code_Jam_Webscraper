#include<bits/stdc++.h>
#define ft first
#define sd second
#define pb push_back
#define mp make_pair
#define ll long long
#define rep(i,j,k) for(int i=j;i<k;i++)
#define wez(n) int (n); scanf("%d",&(n));
#define TESTS wez(ltestow)while(ltestow--)
using namespace std;

const int N=1001000;
const ll P=1e9+7, INF=2*1e9;

int t,l,x;
string s,ss;
int table[5][5]={
	{0,0,0,0,0},
	{0,1,2,3,4},
	{0,2,-1,4,-3},
	{0,3,-4,-1,2},
	{0,4,3,-2,-1}};
int znak,a,b,co;

int main(){
	cin>>t;
	for(int test=1;test<=t;test++){
		cin>>l>>x>>ss;
		s="";
		for(int i=0;i<x;i++) s+=ss;
		a=1;
		znak=0;
		co=0;
		for(int i=0;i<s.length();i++){
			if(s[i]=='i') b=2;
			if(s[i]=='j') b=3;
			if(s[i]=='k') b=4;
			a=table[a][b];
			if(a<0){
				a*=-1;
				znak=!znak;
			}
			if(co==0 && znak==0 && a==2){
				co=1;
				a=1;
			}
			if(co==1 && znak==0 && a==3){
				co=2;
				a=1;
			}
		}
		if(co==2 && a==4 && znak==0) cout<<"Case #"<<test<<": YES\n";
		else cout<<"Case #"<<test<<": NO\n";
	}

}

