#include <bits/stdc++.h>


using namespace std;

#define  mp make_pair


int graph[5][5] = { { 0,0,0,0,0},{0,1,2,3,4}, {0,2,-1,4,-3}, {0,3,-4,-1,2}, {0,4,3,-2,-1}};

map< char ,int> mp1;

void print(int k,bool flag)
{
		if ( flag)
		printf("Case #%d: YES\n",k);
		else
		printf("Case #%d: NO\n",k);
}


int main()
{
	 
	mp1['i'] = 2;
	mp1['j'] = 3;
	mp1['k'] = 4;
	
	
	freopen("1.txt","r",stdin);
	freopen("2.txt","w",stdout);
	int t;
	
	cin >> t;
	string s;
	int n,m;
	for ( int k = 1; k<= t; k++) {
		cin >> n;
		cin >> m;
		cin >> s;
		
		string temp ="";
		
		for ( int i = 0; i < m; i++)
			temp += s;
			
		n = temp.length();
		
		bool is_neg = false;
		
		int val = mp1[s[0]];
		
		int i ;
		for (  i = 1; i < n ; i++) {
			//cout << val << endl;
			if ( val == 2 )
				break;
			int t1 = val >0 ?val :-val;
			
			val = graph[t1][mp1[temp[i]]];
		//	cout <<" hey " << graph[t1][mp1[temp[i]]]<< endl;
		
			val *= is_neg ? -1:1;
		//	cout << val <<endl;
			if ( val < 0 )
				is_neg = true;
			else
				is_neg = false;
		}
		
		if ( i == n) {
			print(k,false);
			continue;
		}
		//cout << "12 23" << endl;
		val = mp1[temp[i]];
		i++;
		is_neg = false;
		for (; i < n; i++) {
			if ( val == 3 )
				break;
			int t1 = val >0 ?val :-val;
			val = graph[t1][mp1[temp[i]]];
		//	cout << val << endl;
			val *= is_neg ? -1:1;
		//		cout << val << endl;
			if ( val < 0 )
				is_neg = true;
			else
				is_neg = false;
		}
		//cout << "3" << endl;
		
	if ( i == n) {
			print(k,false);
			continue;
		}
	//	cout << "4" << endl;
		val = mp1[temp[i]];
		i++;
		is_neg = false;
		for (; i < n; i++) {
			int t1 = val >0 ?val :-val;
			val = graph[t1][mp1[temp[i]]];
			val *= is_neg ? -1:1;
			if ( val < 0 )
				is_neg = true;
			else
				is_neg = false;
		}
		
		if ( val == 4 && is_neg == false)
			print(k,true);
		else
			print(k,false);
		
			
		
		
		
		
		
		
		
	
	}
	return 0;
	
}
