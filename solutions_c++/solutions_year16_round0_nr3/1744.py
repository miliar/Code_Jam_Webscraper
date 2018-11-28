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

long long divisor(long long n){
	long long sq,i;
	sq=sqrt(n);
	for(i=2;i<=sq;i++)if(n%i==0)return i;
	return 0;
}
int main()
{
	freopen("c.in","r",stdin);
	//freopen("c.out","w",stdout);
	
	long long n,j,b,i,num,temp,multiplier;
	long long div[20];
	

//_______________________________________________
	int test_cases,tesT;

	cin>>test_cases;
	for(tesT=0;tesT<test_cases;tesT++){
		cout<<"Case #"<<tesT+1<<": ";
//_______________________________________________
	
	cin>>n>>j;
	cout<<endl;
	i=(1<<(n-2));
	while(j>0){
		bool iscomposite=true;
		for(b=2;b<=10;b++){
			num=1;
			temp=i;
			multiplier=b;
			while(temp){
				num+=(temp&1)*multiplier;
				temp>>=1;
				multiplier*=b;
			}
			iscomposite=iscomposite && (div[b]=divisor(num));
		}
		if(iscomposite){
			cout<<num<<' ';
			for(b=2;b<=10;b++)cout<<div[b]<<' ';
			cout<<endl;
			j--;
		}
		i+=1;
	}


//_______________________________________________
		done:
		cout<<endl;
	}

	cerr<<endl;
	return 0;
}