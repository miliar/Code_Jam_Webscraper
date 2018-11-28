// by Neo

#include<iostream>
#include<vector>
#include<string>
#include<cmath>
#include<algorithm>
#include<set>
#include<map>
using namespace std;

#pragma warning(disable:4996)

typedef long long Int;
#define FOR(i,a,b) for(int i=a;i<=b;++i)
#define CONTAINS(str,key) (str.find_first_of(key) != string::npos)
#define sz(s) (int)(s).size()

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);

	int T;
	scanf("%d\n",&T);			// Read the Number of cases
	const string X_WON = "X won";
	const string O_WON = "O won";
	const string DRAW  = "Draw";
	const string NOT_OVER = "Game has not completed";
	string empty;	// for empty line

	FOR(t,1,T)				// Loop for every case
	{
		string hLines[4] = {"    ","    ","    ","    "};	// Horizontal Lines
		string vLines[4] = {"    ","    ","    ","    "};	// Vertical Lines
		string dLines[2] = {"    ","    "};					// Diogonal Lines
		string wholeString = "";						// All 4 lines connected

		string ans = "";
		for (int j=0, k=0; j<4; j++, k=0)
		{
			getline(cin, hLines[j]);		// Read each line
			
			vLines[k][j] = hLines[j][k]; k++;
			vLines[k][j] = hLines[j][k]; k++;
			vLines[k][j] = hLines[j][k]; k++;
			vLines[k][j] = hLines[j][k]; 

			dLines[0][j] = hLines[j][j];
			dLines[1][j] = hLines[j][3-j];

			wholeString.append(hLines[j]);
		}

		for (int j=0, k=0; j<4; j++, k=0)
		{
			if (!CONTAINS(hLines[j], "X.") || !CONTAINS(vLines[j], "X."))
			{
				ans = O_WON;
				break;
			}
			else if (!CONTAINS(hLines[j], "O.") || !CONTAINS(vLines[j], "O."))
			{
				ans = X_WON;
				break;
			}
		}

		if (ans == "")
		{
			if (!CONTAINS(dLines[0], "X.") || !CONTAINS(dLines[1], "X."))		
				ans = O_WON;			
			else if (!CONTAINS(dLines[0], "O.") || !CONTAINS(dLines[1], "O."))		
				ans = X_WON;
			else if(CONTAINS(wholeString, "."))
				ans = NOT_OVER;
			else
				ans = DRAW;
		}

		cout << "Case #" << t << ": " << ans << "\n";
		getline(cin, empty);
	}

	fclose(stdout);
	fclose(stdin);
	return 0;
}