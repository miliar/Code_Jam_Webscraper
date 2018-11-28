
#include <bits/stdc++.h>
using namespace std;

int call(vector<int> &v) {
	auto temp = v;
	
	int f = 0;
	for(int &x: v) if(x) { f = 1; x--; }
	int ret = INT_MAX;
	
	if(f) ret = call(v) + 1;
	
	v = temp;
	
	if(!f) return 0;
	
	for( int i =0; i < int(temp.size()); i++) {
		if( temp[i] < 2 ) continue;
		
		v[i] = temp[i] / 2;
		v.push_back( temp[i] - (temp[i]/2) );
		ret = min( ret, call(v) + 1 );
		
		v.pop_back();
		v[i] = temp[i];
	}
	return ret;
}

map<int,int> ase;

int main(){
    time_t start=clock();
    freopen("bin","r",stdin);
    freopen("bout","w",stdout);
    ios_base::sync_with_stdio(0);
    int test, kas=0;
    cin>>test;
    while( test-- ){
		int n;
		cin >> n;
		
		ase.clear();
		
		vector<int> ttt;
		long long answer = 0;
		
		for(int i =0; i<n; i++ ) {
			int temp;
			cin >> temp;
			ase[temp]++;
			
			answer = max( answer, (long long)temp );
			
			ttt.push_back( temp );
		}
		

		long long special = 0;
		
		while( true ) {
			if( ase.crbegin()->second > ase.crbegin()->first ) break;
			answer = min( answer, (long long)ase.crbegin()->first + special );
			int top = ase.crbegin()->first;
			
			if(top<2) break;
			
			ase[top]--;
			if(!ase[top]) ase.erase(top);
			
			ase[ (top+1)/2 ]++;
			ase[ top - ((top+1)/2) ]++;
			special++;
		}
		
		answer = min( answer, ase.crbegin()->first + special );
		
		//if( answer != call(ttt) ) {
		//	cout << "here" << endl;
			//return 0;
		//}
		
        cout<<"Case #"<<++kas<<": ";
        cout << answer << endl;
    }
    cerr << " Program has run "<< ( clock()-start ) / CLOCKS_PER_SEC << " s " << endl;
    return 0;
}

