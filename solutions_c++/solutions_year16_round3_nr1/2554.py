#include <bits/stdc++.h>

using namespace std;

#define FOR(i,a,b) for(int i=a;i<b;++i)
#define FORI(i,b,a) for(int i=b;i>=a;--i)

pair<int,char> counts[30];

void tworemaining(int n)
{
	char a = counts[n-1].second;
	char b = counts[n-2].second;
	FOR(i,0,counts[n-1].first){
		cout<<a<<b<<" ";
	}
}

int main()
{
	int t;
	scanf("%d", &t);
	FOR(cases, 1, t+1){
		cout<<"Case #"<<cases<<": ";
		int n,counttemp;
		cin>>n;
		FOR(i,0,n){
			cin>>counttemp;
			counts[i] = make_pair(counttemp, 'A'+i);
		}
		sort(counts, counts+n);
		if(n==2){
			//both vals must be same
			tworemaining(n);
		} else {
			int& val1 = counts[n-1].first;
			int& val2 = counts[n-2].first;
			char& char1 = counts[n-1].second;
			char& char2 = counts[n-2].second;
			while(val1-val2>=2){
				cout<<char1<<char1<<" ";
				val1 = val1-2;
			}
			if(val1-val2 == 1){
				cout<<char1<<" ";
				--val1;
			}
			//both val1, val2 are now equal
			FOR(i,0,n-2){
				int& val = counts[i].first;
				char chara = counts[i].second;
				while(val>=2){
					cout<<chara<<chara<<" ";
					val = val-2;
				}
				if(val==1){
					cout<<chara<<" ";
					--val;
				}
			}
			tworemaining(n);
		}
		cout<<endl;
	}
}