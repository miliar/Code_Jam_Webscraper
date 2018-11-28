//	created : 16/04/09
// 	author   : Rp7rf
#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <set>
typedef long long ll;
typedef unsigned long long ull;
using namespace std;
#define rep(i,a) for(int i = 0 ; i < a ; i ++)
#define loop(i,a,b) for(int i = a ; i < b ; i ++)
#define vi vector<int>
#define mp make_pair
#define pb push_back
#define MOD 1000000007
#define INF 1e9


int main(void){
	unsigned long long n,num;
	cin>>n;
	rep(i,n){
		cin>>num;
		cout<<"Case #" <<i + 1 << ": ";
		if(num == 0){
			cout<<"INSOMNIA"<<endl;
			continue;
		}
		unsigned long long cnt = 0;
		vi ary(10,0);
		unsigned long long j = 1; 
		while(cnt <= 55){
			unsigned long long now = num * j++;
			while(now != 0){
				if(!ary[now%10]){
					ary[now%10] = 1;
					cnt += now%10 + 1;
				}
				now /= 10;
			}
			bool judge = true;
			rep(i,ary.size()){
				if(!ary[i])judge = false;
			}
			if(judge){
				cout<<num * --j<<endl;
				break;
			}

		}
	}
}
