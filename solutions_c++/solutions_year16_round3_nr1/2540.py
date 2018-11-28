#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <math.h>
#include <list>
#include <map>
#include <set>
using namespace std;
typedef long long LL;
#define F(i,n) for (int i = 0; i < (int)(n); i++)



main(){

	FILE *fin = freopen("A-large.in", "r", stdin);
	assert (fin != NULL);
	//cout << "A open ";
	FILE *fout = freopen("A-large.out", "w", stdout);
	//cout << "A created";
	int T, n, x, y, sum;
	vector<int> p;
        set <pair <int,int> > q;	
	vector<string> res, tmp;
	string s;
	cin >> T;

	//cout << "Test cases: " << T;
	for(int t = 1; t <= T; t++){
		p.clear();
		res.clear();
		q.clear();
		sum = 0;
		cin >> n;
		F(i,n){
			cin>>x;
			p.push_back(x);
			q.insert({x,i});
			sum+=x;
		}
		while (!q.empty()){
			x = q.rbegin()->second;
			q.erase({q.rbegin()->first, q.rbegin()->second});
			s = "";
			y = -1;
			if (!q.empty()){
				y = q.rbegin()->second;
				q.erase({q.rbegin()->first, q.rbegin()->second});
			}
			p[x]--;
			
			if (p[x]>0)
				q.insert({p[x],x});
			s = 'A'+x;
			if (y > -1){
				if ( !(q.size()==1 && p[y]-1==0) && !(q.size()==0&&p[y]-1>0) ){
					p[y]--;
					s.push_back('A'+ y);		
				}
				if (p[y]>0)
					q.insert({p[y],y});	
				
			}
			res.push_back(s);

		}



		cout << "Case #" << t << ": ";
		F(i,res.size())
			cout << res[i] << " ";
		cout << endl;
			


	}
	exit(0);
}
