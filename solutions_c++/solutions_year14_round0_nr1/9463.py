#include <iostream>
#include <sstream>
#include <vector>
#include <string>
#include <set>
#include <map>

#define forn(i,n) for (int i = 0; i < n; i++) 
#define forN(i,n) for (i = 0; i < n; i++) 
#define forr(i,n) for (int i = n-1; i >= 0; i--) 
#define ford(i,n,d) for (int i = 0; i < n; i+=d)
#define forv(i,a) for (int i = 0; i < (a).size(); i++)
using namespace std;

int main() {

	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int t;
	cin>>t;
		int x,a,b,c,d;
		vector <int> q;
		int ans = -1;
		
		int j;
	for (int i1 = 0; i1 < t; i1++) {
		q.clear();
		ans = -1;
		cin>>x;
		
		for (int i = 1; i <= 4; i++) {
		
			cin >>a>>b>>c>>d;
			if (x==i) {q.push_back(a);q.push_back(b);q.push_back(c);q.push_back(d);}
			
		}
		
		cin>>x;
		for (int i = 1; i <= 4; i++) {
		
			cin >>a>>b>>c>>d;
			if (x==i) {
				forN(j,4) { if (a==q[j]) {if (ans!=-1) { ans = -2;goto end;} ans = a;}}
				forN(j,4) { if (b==q[j]) {if (ans!=-1) { ans = -2;goto end;} ans = b;}}
				forN(j,4) { if (c==q[j]) {if (ans!=-1) { ans = -2;goto end;} ans = c;}}
				forN(j,4) { if (d==q[j]) {if (ans!=-1) { ans = -2;goto end;} ans = d;}}
				 
			}
			end:;
		}
		
		
		
		cout << "Case #" << i1+1<<": ";
		if (ans == -2) cout << "Bad magician!"<<endl; else 
		if (ans == -1) cout << "Volunteer cheated!"<<endl; else 
		cout << ans << endl;
	}
	
	fclose(stdin);
	fclose(stdout);
}
