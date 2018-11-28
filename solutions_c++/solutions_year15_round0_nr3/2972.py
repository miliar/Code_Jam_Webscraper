#include <iostream>
#include <string>

using namespace std;

int qm[][5] = { {0, 0, 0, 0, 0},
                {0, 1, 2, 3, 4},
                {0, 2,-1, 4,-3},
                {0, 3,-4,-1, 2},
								{0, 4, 3,-2,-1} };

int val(char c){
	return c - 'g';
}

bool *tried;
bool *tried_j;


bool find_k(int l, int x, string& s, int start)
{
	int ix = start;
	int v = val(s[ix%l]);

	ix++;	
	while (ix < l*x)
	{
		if (v > 0) 
			v = qm[v][ val( s[ix % l] ) ];
		else if (v < 0)
			v = -( qm[-v][ val( s[ix % l] ) ] );
		else
			cerr << "kError, v is " << v << endl;
			
		ix++;
	}
	if (v == val('k')){
		cerr << "Found k at the end " << ix << endl;
		return true;
	}
	return false;
}


bool find_j(int l, int x, string& s, int start)
{
	int ix = start;
	int v = val(s[ix%l]);
	
	//cerr << "j from" << ix << " v = " << v << endl;
	
	while (ix < l*x-1)
	{
		if (v == val('j')){
			//cerr << "Found j at " << ix << endl;
			if ( tried_j[ ix%l ] == false )
			{
				tried_j[ ix%l ] = true;
				bool ty;
				ty = find_k(l,x,s,ix+1);
				if (ty) return true;
			}
		}
		ix++;
		if (v > 0) 
			v = qm[v][ val( s[ix % l] ) ];
		else if (v < 0)
			v = -( qm[-v][ val( s[ix % l] ) ] );
		else
			cerr << "jError, v is " << v << endl;
	}
	return false;
}


bool find_i(int l, int x, string& s)
{
	int ix = 0;
	int v = val(s[0]);
	
	while (ix < (l*x)-2)
	{
		if (v == val('i')){
			//cerr << "Found i at " << ix << endl;
			
			if ( tried[ ix%l ] == false )
			{
				tried[ ix%l ] = true;
				bool ty;
				ty = find_j(l,x,s,ix+1);
				if (ty) return true;
			}
			//cerr << "i cont.." << endl;
		}
		
		ix++;
		if (v > 0) 
			v = qm[v][ val( s[ix % l] ) ];
		else if (v < 0)
			v = -( qm[-v][ val( s[ix % l] ) ] );
		else
			cerr << "Error, v is " << v << endl;
	}
	//cerr << "Done with i" << endl;

	return false;
}


int main ()
{
	int T;
	string s;
	
	cerr << "Hello ijk!!" << endl;

/*
	cerr << val('i') << endl;
	cerr << val('j') << endl;
	cerr << val('k') << endl;
*/

	cin >> T;
	cerr << T << " test cases" << endl;
	
	for (int i=1; i<=T; i++){
		
		int l, x;
		bool sol;
		
		cin >> l >> x >> s;
		
		
		
		cerr << "#" << i << endl;
		cerr << l << " " << x << " s = " << s << endl;

		if ( l*x < 3 ) 
		{
			sol = false;
		}
		else {
			
			tried = new bool[l];
			for (int k=0; k<l; k++) tried[k] = false;
			tried_j = new bool[l];
			for (int k=0; k<l; k++) tried_j[k] = false;
			
			sol = find_i(l, x, s);
			
			delete [] tried;
			delete [] tried_j;
		}
		
		cout << "Case #" << i << ": ";
		sol ? cout << "YES" : cout << "NO";
		cout << endl;
	}
	

	return 0;
}
