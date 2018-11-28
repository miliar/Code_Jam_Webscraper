#include<iostream>
#include<algorithm>
#include<iomanip>
#include<cstdio>
#include<map>
#include<set>
#include<stack>
#include<queue>
#include<vector>
#define For(i,a,b) for(long i = a;i<=b;i++)
#define mp make_pair
#define pb push_back
#define nd second
#define fs first
#define M 2000000002
#define ll long long
using namespace std;
double C,F,time,A,X;
void nhap(){
	cin>>C>>F>>X;
}
void proce(){
	time = X/2; A = 2;
	double sum = C/A;
	while(sum < time){
		A += F; time = min(time,sum + X/A); sum += C/A;
	}
}
int main(){
//	freopen("A.in","r",stdin);
//	freopen("A.out","w",stdout);
	int test; scanf("%d",&test);
	For(i,1,test){		
		nhap(); proce();
		printf("Case #%d: ",i);
		cout<<setprecision(7)<<fixed<<time<<endl;
	}
	
	
	return 0;
}
