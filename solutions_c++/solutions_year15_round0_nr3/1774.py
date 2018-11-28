#include <fstream>
#include <string>

using namespace std;

string strInput;
string Mul(string x, string y);

int main()
{
	ifstream fin("C.in");
	ofstream fout("C.out");
	
	int T, L, X;
	string strTmp;
	fin >> T;
	for(int i = 1; i <= T; i++)
	{
		fin >> L >> X;
		fin >> strTmp;
		bool I = false, J = false, K = false;
		strInput = "";
		// if(X > 12) { X = 12; }
		for(int j = 1; j <= X; j++)
		{ strInput += strTmp; }
		string ans = strInput.substr(0, 1);
		if(ans == "i") { I = true; }
		for(int j = 1; j < strInput.length(); j++)
		{
			ans = Mul(ans, strInput.substr(j, 1));
			if(!I)
			{
				if(ans == "i") { I = true; }
			}
			else
			{
				if(ans == "k") { J = true; }
			}
		}
		if(ans == "-1" && I && J) { K = true; }
		if(K) { fout << "Case #" << i << ": YES" << endl; }
		else { fout << "Case #" << i << ": NO" << endl; }
	}
	return 0;
}

string Value(string x)
{
	string ans = x.substr(0, 1); x = x.substr(1, x.length() - 1);
	for(int i = 0; i < x.length(); i++)
	{ ans = Mul(ans, x.substr(i, 1)); }
	return ans;
}

string Mul(string x, string y)
{
	int nCnt = 0;
	string ans = "";
	if(x[0] == '-') { nCnt++; x = x[1]; }
	if(y[0] == '-') { nCnt++; y = y[1]; }
	if(x == "1")
	{
		if(y == "1") { ans = "1"; }
		if(y == "i") { ans = "i"; }
		if(y == "j") { ans = "j"; }
		if(y == "k") { ans = "k"; }
	}
	if(x == "i")
	{
		if(y == "1") { ans = "i"; } 
		if(y == "i") { ans = "1"; nCnt++; }
		if(y == "j") { ans = "k"; }
		if(y == "k") { ans = "j"; nCnt++; }
	}
	if(x == "j")
	{
		if(y == "1") { ans = "j"; }
		if(y == "i") { ans = "k"; nCnt++; }
		if(y == "j") { ans = "1"; nCnt++; }
		if(y == "k") { ans = "i"; }
	}
	if(x == "k")
	{
		if(y == "1") { ans = "k"; }
		if(y == "i") { ans = "j"; }
		if(y == "j") { ans = "i"; nCnt++; }
		if(y == "k") { ans = "1"; nCnt++; }
	}
	if(nCnt & 1) { ans = "-" + ans; }
	return ans;
}

string Div(string x, string y)
{
	int nCnt = 0;
	string ans = "";
	if(x[0] == '-') { nCnt++; x = x[1]; }
	if(y[0] == '-') { nCnt++; y = y[1]; }
	if(x == "1")
	{
		if(y == "1") { ans = "1"; }
		if(y == "i") { ans = "i"; nCnt++; }
		if(y == "j") { ans = "j"; nCnt++; }
		if(y == "k") { ans = "k"; nCnt++; }
	}
	if(x == "i")
	{
		if(y == "1") { ans = "i"; } 
		if(y == "i") { ans = "1"; }
		if(y == "j") { ans = "k"; }
		if(y == "k") { ans = "j"; nCnt++; }
	}
	if(x == "j")
	{
		if(y == "1") { ans = "j"; }
		if(y == "i") { ans = "k"; nCnt++; }
		if(y == "j") { ans = "1"; }
		if(y == "k") { ans = "i"; }
	}
	if(x == "k")
	{
		if(y == "1") { ans = "k"; }
		if(y == "i") { ans = "j"; }
		if(y == "j") { ans = "i"; nCnt++; }
		if(y == "k") { ans = "1"; }
	}
	if(nCnt & 1) { ans = "-" + ans; }
	return ans;
}
