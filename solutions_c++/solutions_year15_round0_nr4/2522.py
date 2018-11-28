#include <bits/stdc++.h>

#define F(i,a,b) for(int i = a; i < b; i++)
#define pb push_back
#define mp make_pair
#define all(a) a.begin(), a.end()


using namespace std;

typedef vector<int> vi;
typedef vector<vi> vii;
typedef pair<int,int> pii;
typedef vector<pii> vpii;
typedef vector<string> vs;
typedef vector<vs> vvs;
typedef  long long ll;

int main()
{
	std::ios_base::sync_with_stdio(false);
	int T,D=0,X,R,C;
	cin >> T;
	
	F(cs,0,T)
	{
		cin >> X >> R >> C;
		
		
			if(X == 1)
				cout << "Case #" << cs+1 << ": " << "GABRIEL" << endl;
			else if(X == 2)
			{
				if((R * C) % 2 == 0)
					cout << "Case #" << cs+1 << ": " << "GABRIEL" << endl;
				else
					cout << "Case #" << cs+1 << ": " << "RICHARD" << endl;
			}
			else if(X == 3)
			{
				if(R > C)
					swap(R,C);
			
				if(R == 2 && C == 3)
					cout << "Case #" << cs+1 << ": " << "GABRIEL" << endl;
				else if(R == 3 && C == 3)
					cout << "Case #" << cs+1 << ": " << "GABRIEL" << endl;
				else if(R == 3 && C == 4)
					cout << "Case #" << cs+1 << ": " << "GABRIEL" << endl;
				else
					cout << "Case #" << cs+1 << ": " << "RICHARD" << endl;
			}
			else if(X == 4)
			{
				if(R > C)
					swap(R,C);
				
				if(R == 4 && C == 4)
					cout << "Case #" << cs+1 << ": " << "GABRIEL" << endl;
				else	if(R == 3 && C == 4)
					cout << "Case #" << cs+1 << ": " << "GABRIEL" << endl;
				else
					cout << "Case #" << cs+1 << ": " << "RICHARD" << endl;
			}
		
		
		
	}
	
	return 0;
}
