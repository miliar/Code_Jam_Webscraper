#include<iostream>
#include<vector>
#include<algorithm>
#define f first
#define s second
#define mp make_pair
using namespace std;



template<int N>
struct graph {
	vector<int> conn[N];
	int root, parent[N];
	
	void reset() {
		for(int i=0;i<N;i++)
			conn[i].clear();
	}
	
	void addEdge(int a, int b) {
		conn[a].push_back(b);
		conn[b].push_back(a);
		
		parent[b] = a;
	}
	
	
	
	
	//Finally the problem relevant stuff
	
	int value[N];
	bool used[N], avail[N];
	int nused;
	
	
	void init(int n) {
		
		fill(used, used + n, true);
		fill(avail, avail + n, true);
		
		nused = n;
	}
	
	
	
	inline void setValue(int ind, int newvalue) {
		value[ind] = newvalue;
	}
	
	
	
	void remove(int ind) {
		if(!used[ind])
			return;
	
		nused--;
		used[ind] = false;
	
		for(int i=0;i<conn[ind].size();i++)
			if(conn[ind][i] != parent[ind])
				remove(conn[ind][i]);
	}
	
	
	void fire(int ind) {
		
		avail[ind] = false;
		
		remove(ind);
		
	}
	
	
	
	void hire(int ind) {
		if(used[ind] || !avail[ind])
			return;
		
		nused++;
		used[ind] = true;
		
		for(int i=0;i<conn[ind].size();i++)
			if(conn[ind][i] != parent[ind])
				hire(conn[ind][i]);
		
	}
	
	
	
	void consider(int ind) {
		
		avail[ind] = true;
		
		if(used[parent[ind]] )
			hire(ind);
		
	}
};




//--------------------------------------------------------
//Main algorithm begins here





int T, n, d, As, Cs, Rs;
int Am, Cm, Rm;
int S[1000000], M[1000000];
graph<1000000> g;


int main() {
	
	cin >> T;
	
	
	for(int TCASE = 1; TCASE <= T; TCASE++) {
		g.reset();
		
		cin >> n >> d;
		
		cin >> S[0] >> As >> Cs >> Rs;
		cin >> M[0] >> Am >> Cm >> Rm;
		
		for(int i=1;i<n;i++) {
			S[i] = (1LL * As * S[i-1] + Cs ) % Rs;
			M[i] = (1LL * Am * M[i-1] + Cm ) % Rm;
		}
		
		
		
		g.init(n);
		
		for(int i=0;i<n;i++) {
			g.setValue(i, S[i]);
			
			if(i > 0)
				g.addEdge(M[i] % i, i);
		}
		
		
		//Finally we add the employees to the sorted array
		
		vector<pair<int, int> > sorted;
		
		for(int i=0;i<n;i++)
			sorted.push_back( mp(S[i], i) );
		
		
		sort(sorted.begin(), sorted.end() );
		
		
		//Here we fire the bound employees
		
		int lb, ub;
		
		for(lb=0;lb<sorted.size() && sorted[lb].f < S[0] - d;lb++)
			g.fire(sorted[lb].s);
		
		
		for(ub=sorted.size() - 1;  ub>=0 && sorted[ub].f > S[0]; ub--)
			g.fire(sorted[ub].s);
			
		ub++;	
		
		
		
		//Next we keep the result and start moving the window
		
		int result = g.nused;
		
		for(int start = S[0] - d + 1; start <= S[0]; start++) {
			
			while(sorted[lb].f < start)
				g.fire(sorted[lb++].s);
			
			while(ub < sorted.size() && sorted[ub].f <= start + d)
				g.consider(sorted[ub++].s);
			
			
			result = max(result, g.nused);
		}
		
		cout << "Case #" << TCASE << ": " << result << '\n';
	}
	
	
	return 0;
}













































