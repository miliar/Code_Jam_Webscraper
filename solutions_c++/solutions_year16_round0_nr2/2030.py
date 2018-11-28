#include<iostream>
#include<cstdio>
#include<vector>
#include<algorithm>
#include<set>
#include<string>

using namespace std;

#define in(x,y) ( (x)>=0 && (y)>=0 && (x)<n && (y)<m )
#define F first
#define S second
#define INF 2000999999
int dx[]={1,0,-1,0};
int dy[]={0,1,0,-1};
#define MAX 120


int main()
{
	freopen("b.in","r",stdin);
	//freopen("b.out","w",stdout);
	
	
	string s;
	int i;

//_______________________________________________
	int test_cases,tesT;

	cin>>test_cases;
	for(tesT=0;tesT<test_cases;tesT++){
		cout<<"Case #"<<tesT+1<<": ";
//_______________________________________________
	cin>>s;
	char cur='+';
	int countt=0;
	for(i=s.size()-1;i>=0;i--){
		if(s[i]!=cur){
			countt++;
			cur=s[i];
		}
	}
	cout<<countt;

//_______________________________________________
		done:
		cout<<endl;
	}

	cerr<<endl;
	return 0;
}