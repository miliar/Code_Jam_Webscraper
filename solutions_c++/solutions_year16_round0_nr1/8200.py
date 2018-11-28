#include<fstream>
#include<stdio.h>
#include<iostream>
#include<algorithm>
#include<math.h>

#define ll long long int
using namespace std;
#define INF 99987654321
bool visited[10];
int n;
bool isFinished()
{
	for(int i=0;i<10;i++)
		if(!visited[i])
			return false;
	return true;
}
ll pow(int a, int b)
{
	ll ra = 1;
	for(int i=0;i<b;i++)
		ra = ra*a;
	
	return ra;
}
ll multi(int k)
{

	ll t = n*k;
	ll anst = t;
	bool ok = true;
	for(int i=11;i>=0;i--){
		ll p = pow(10,i);

		if(ok && t/p != 0){
				
			visited[t/p] =true;
			if(isFinished())
				return anst;
			t = t - (t/p)*p;
			ok = false;
		}
		else if(!ok){
			
			visited[t/p] = true;	
			if(isFinished())
				return anst;
			t = t - (t/p)*p;
		}
	}
	if(isFinished())
		return anst;

	return 0;
	
}
int main()
{
	int test;
	cin >> test;

	ofstream fout;
	fout.open("info.txt");
	for(int t=0;t<test;t++){

		cin >> n;
		
		if(n == 0){
			fout << "case #" << t+1 << ": " << "INSOMNIA" << endl;
			continue;
		}

		for(int i=0;i<10;i++) visited[i] = false;
		for(int i=1;i<=10000;i++){
			ll ans = multi(i);

			if(ans != 0){
				fout << "case #" << t+1 << ": " << ans << endl;
				break;
			}
		}
	}
}