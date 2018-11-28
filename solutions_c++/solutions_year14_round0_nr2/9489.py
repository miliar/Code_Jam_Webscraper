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

	char g[100][100];




int main() {

	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int t;
	cin>>t;
	
	double c,f,x;
	double mintime = 1<<30;
	double cur=0;
	forn (i1, t) {
		
		cin>>c>>f>>x;		
		cur = 0;
		mintime = 1<<30;
		for (int i = 0; i < 10123; i++) {
			
				
			mintime = min (mintime,cur + x/(i*f + 2));
			cur += c/(i*f + 2);
		}
		
		cout << "Case #" << i1+1<<": ";
		printf("%.7f\n",mintime);
		
	}

	
	fclose(stdin);
	fclose(stdout);
}
