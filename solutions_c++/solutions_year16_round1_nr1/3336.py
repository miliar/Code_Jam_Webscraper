
#include<string>
#include<vector>
#include<iostream>
#include<algorithm>
#include<set>

using namespace std;

#if 0 
void solve1( int casenum )
{
	cout << "Case #" << casenum << ": ";
	int n, l;
	cin >> n >> l;
	vector<string> iavl(n), ireq(n);
	for ( int i = 0 ; i < n ; i++ )
		cin >> iavl[i];	
	for ( int i = 0 ; i < n ; i++ )
		cin >> ireq[i];	
	sort( ireq.begin(), ireq.end() );
	sort ( iavl.begin(), iavl.end() );
	int to_flip = 0;
	vector<bool> normal_tried(l, false);
	for ( int i = 1 ; i <= l; i++ )
	{
		multiset<string> target, ctarget;
		if ( ! normal_tried[i] )
		{
			for ( int j = 0 ; j < n ; j++ )
				target.insert( iavl[j].substr(0,i ) );
			//cout << "Will look for : " << endl;
//			for ( int j = 0 ; j < n ; j++ )
//				cout << " " << ireq[j].substr(0,i) << endl << endl;
//			for ( multiset<string>::iterator iter = target.begin();
//					iter != target.end() ; iter++ )
//				cout << "'" << *iter << "'" << endl;

			for ( int j = 0 ; j < n ; j++ )
			{
//				cout << "Contents of normal : " << endl;
//				for ( multiset<string>::iterator iter = target.begin();
//						iter != target.end() ; iter++ )
//					cout << "'" << *iter << "'" << endl;
//
//				multiset<string>::iterator iter = target.find( ireq[j].substr(0,i) );
//				cout << "Looking for '" << ireq[j].substr(0,i) << "' in normal" << endl;
				if ( iter != target.end() )
					target.erase( iter );
				else
				{
//					cout << "Not found '" << ireq[j].substr(0,i) << "' in normal" << endl;
					break;
				}
	/*
	*/
			}
			if ( target.empty() )
				continue;
		}
		for ( int j = 0 ; j < n ; j++ )
			ctarget.insert( iavl[j].substr(0,i-1 ) + (iavl[j][i-1]=='1' ? '0' : '1') );
		for ( int j = 0 ; j < n ; j++ )
		{
//			cout << "Contents of complemented : " << endl;
//			for ( multiset<string>::iterator iter = ctarget.begin();
//					iter != ctarget.end() ; iter++ )
//				cout << "'" << *iter << "'" << endl;
//			multiset<string>::iterator iter = ctarget.find( ireq[j].substr(0,i) );
//			cout << "Looking for '" << ireq[j].substr(0,i) << "' in complimented" << endl;
			if ( iter != ctarget.end() )
				ctarget.erase( iter );
			else
			{
//				cout << "Not found '" << ireq[j].substr(0,i) << "' in complimented" << endl;
				break;
			}
		}
		if ( ctarget.empty() )
		{
			for ( int j = 0 ; j < n ; j++ )
				iavl[j][i-1] = (iavl[j][i-1]=='1' ? '0' : '1');
			to_flip++;
			continue;
		}
		cout << "NOT POSSIBLE" << endl;
		return;
	}
	if ( to_flip > l - to_flip )
		to_flip = l - to_flip;
	cout << to_flip << endl;
}
#endif

int subsolve( int i, int n, int l, vector<string> & iavl, vector<string> & ireq )
{
	if ( i > l )
		return 0;
	int num_flips = -1;
	multiset<string> target, ctarget;
	for ( int j = 0 ; j < n ; j++ )
		target.insert( iavl[j].substr(0,i ) );
//	cout << "Will look for : " << endl;
//	for ( int j = 0 ; j < n ; j++ )
//		cout << " " << ireq[j].substr(0,i) << endl;
//
	for ( int j = 0 ; j < n ; j++ )
	{
//		cout << "Contents of normal : " << endl;
//		for ( multiset<string>::iterator iter = target.begin();
//				iter != target.end() ; iter++ )
//			cout << "'" << *iter << "'" << endl;
//
		multiset<string>::iterator iter = target.find( ireq[j].substr(0,i) );
//		cout << "Looking for '" << ireq[j].substr(0,i) << "' in normal" << endl;
		if ( iter != target.end() )
			target.erase( iter );
		else
		{
//			cout << "Not found '" << ireq[j].substr(0,i) << "' in normal" << endl;
			break;
		}
		/*
		 */
	}
	if ( target.empty() )
		num_flips = subsolve( i+1, n, l, iavl, ireq );
	for ( int j = 0 ; j < n ; j++ )
		ctarget.insert( iavl[j].substr(0,i-1 ) + (iavl[j][i-1]=='1' ? '0' : '1') );
	for ( int j = 0 ; j < n ; j++ )
	{
//		cout << "Contents of complemented : " << endl;
//		for ( multiset<string>::iterator iter = ctarget.begin();
//				iter != ctarget.end() ; iter++ )
//			cout << "'" << *iter << "'" << endl;
		multiset<string>::iterator iter = ctarget.find( ireq[j].substr(0,i) );
//		cout << "Looking for '" << ireq[j].substr(0,i) << "' in complimented" << endl;
		if ( iter != ctarget.end() )
			ctarget.erase( iter );
		else
		{
//			cout << "Not found '" << ireq[j].substr(0,i) << "' in complimented" << endl;
			break;
		}
	}
	int num_c_flips = -1;
	if ( ctarget.empty() )
	{
		
		for ( int j = 0 ; j < n ; j++ )
			iavl[j][i-1] = (iavl[j][i-1]=='1' ? '0' : '1');
		num_c_flips = subsolve( i+1, n, l, iavl, ireq );
		if ( num_c_flips >= 0 )
			num_c_flips++;
		for ( int j = 0 ; j < n ; j++ )
			iavl[j][i-1] = (iavl[j][i-1]=='1' ? '0' : '1');
	}
	if ( num_flips == -1 )
		return num_c_flips;
	else if ( num_c_flips == -1 )
		return num_flips;
	if ( num_flips < num_c_flips )
		return num_flips;
	else
		return num_c_flips;
}
void solve( int casenum )
{
	cout << "Case #" << casenum << ": ";
string s;
cin >> s;
string sout = s.substr(0,1);
for ( int i =1 ; i < s.size(); i++ )
{
  if ( s[i] >= sout[0] )
	sout = s.substr(i, 1) + sout;
  else
	sout = sout + s.substr(i,1);
}
cout << sout << endl;
};
int main(int argc, char * argv[] )
{
	int t;
	cin >> t;
	for ( int casenum = 1; casenum <= t; casenum++ )
	{
		solve( casenum );
	}

}
