//#pragma comment(linker, "/stack:16777216")
#include <iostream>
#include <set>
#include <queue>
#include <stack>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <math.h>
#include <string>
#include <map>
#include <stdlib.h>
#include <sstream>
#include <memory.h>
#include <ctime>
//#include <fstream>
using namespace std;
 
using namespace std;

#define INF 1000000000
#define MP make_pair
#define FILL(a,value) memset(a,value,sizeof(a))
#define MOD 1000000009
double const PI = acos(-1.0);
double const EPS=1e-7;

double C[3000][3000];

void init(){
	C[0][0]=1;
	for (int i=1; i<3000; i++){
		C[i][0]=1;
		for (int j=1; j<3000; j++){
			C[i][j]=C[i-1][j-1]+C[i-1][j];
		}
	}
}

double d[2000][2000];
double d2[2000][2000];

void solve()
{
	int cnt,x,y;
	cin>>cnt>>x>>y;

	int n=(abs(x)+y)/2;

	int c=1;
	int one=1;

	for (int i=0; i<n; i++){
		cnt-=c;
		c=c+4;
		one+=2;
	}

	if (cnt<=0){
		cout<<"0.0"<<endl;
		return ;
	}

	if (cnt-(c)>=0){
		cout<<"1.0"<<endl;
		return;
	}


	if (x==0){
		cout<<"0.0"<<endl;
		return;
	}

	y++;
	one--;

	FILL(d,0);

	d[0][0]=1;
	for (int i=0; i<cnt; i++){
		for (int j=0; j<=one; j++){
			for (int k=0; k<=one; k++){
				if (j==one) d2[j][k+1]+=d[j][k];
				else if (k==one) d2[j+1][k]+=d[j][k];
				else{
					d2[j+1][k]+=0.5*d[j][k];
					d2[j][k+1]+=0.5*d[j][k];
				}
			}
		}

		for (int j=0; j<=one; j++){
			for (int k=0; k<=one; k++){
				d[j][k]=d2[j][k];
				d2[j][k]=0;
			}
		}
	}


	double res=0;
	for (int i=0; i<=one; i++){
		for (int j=0; j<=one; j++){
			if (i>=y) res+=d[i][j];
		}
	}

	printf("%.9f\n",res);
	return ;/*


	double res=0;
	one--;

	for (int i=y; i<=min(cnt,one); i++){

		if (cnt-i>one) continue;


		if (cnt-i==one){
			for (int j=0; j<=i; j++){
				res+=C[one-1+j][j]*pow(0.5,one-1+j) * 0.5;

			}
		} else

		if (i==one){
			for (int j=0; j<=cnt-i; j++){
				res+=C[one-1+j][one-1]*pow(0.5,one-1+j) * 0.5;
			}
		} else

		res+=C[cnt][i]*pow(0.5,cnt);
	}

	printf("%.9f\n",res);*/


}

int main()
{

	freopen("in.txt","r",stdin);
	freopen("OUTPUT.txt","w",stdout);

	int tt;
	cin>>tt;

	//string str;
	//getline(cin,str);

	init();

	for (int t=1; t<=tt; t++){
		cout<<"Case #"<<t<<": ";
		int time=clock();
		solve();
		cerr<<"\t\tCase #"<<t<<"\t time="<<clock()-time<<endl;
	}

}