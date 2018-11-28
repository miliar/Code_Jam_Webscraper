#include<iostream>
#include<cstdio>
#include<vector>
#include<algorithm>
#include<set>
#include<string>
#include<cmath>

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
	freopen("d.in","r",stdin);
	//freopen("d.out","w",stdout);
	
	long long k,c,s,t,num,mult,j,req;
	

//_______________________________________________
	int test_cases,tesT;

	cin>>test_cases;
	for(tesT=0;tesT<test_cases;tesT++){
		cout<<"Case #"<<tesT+1<<": ";
//_______________________________________________
	cin>>k>>c>>s;
	req=(k+c-1)/c;
	if(req>s){
		cout<<"IMPOSSIBLE";
		goto done;
	}
	for(t=1;t<=req;t++){
		num=0;
		mult=1;
		for(j=1;j<c;j++)mult*=k;
		for(j=((t-1)*c);j<=min(k-1,t*c-1);j++){

			num+=mult*j;
			cerr<<num<<' ' ;
			mult/=k;
		}
		cerr<<">>>";
		cout<<num+1<<' ';
	}
	

//_______________________________________________
		done:
		cout<<endl;
	}

	cerr<<endl;
	return 0;
}