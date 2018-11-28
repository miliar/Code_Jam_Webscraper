#include<iostream>
#include<cstdio>
#include<vector>
#include<algorithm>
#include<set>

using namespace std;

#define in(x,y) ( (x)>=0 && (y)>=0 && (x)<n && (y)<m )
#define F first
#define S second
#define INF 2000999999
int dx[]={1,0,-1,0};
int dy[]={0,1,0,-1};
#define MAX 120

bool seen[10];
void update(int n){
	n=n*10+1;
	while(n>1){
		seen[n%10]=true;
		n/=10;
	}
}
bool allseen(){
	bool allseen=true;
	for(int i=0;i<10;i++)
		allseen=allseen && seen[i];
	return allseen;
}
int main()
{
	freopen("1.in","r",stdin);
	//freopen("1.out","w",stdout);
	
	int n,i;
	

//_______________________________________________
	int test_cases,tesT;

	cin>>test_cases;
	for(tesT=0;tesT<test_cases;tesT++){
		cout<<"Case #"<<tesT+1<<": ";
//_______________________________________________
	cin>>n;
	for(i=0;i<10;i++)seen[i]=0;
	for(i=1;i<=100;i++){
		update(n*i);
		if(allseen()){
			cout<<n*i;
			goto done;
		}
	}
	cout<<"INSOMNIA";

//_______________________________________________
		done:
		cout<<endl;
	}

	cerr<<endl;
	return 0;
}