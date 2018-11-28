#include <bits/stdc++.h>

using namespace std;

string suma(const string &a, const string &b) 
{ 
	int LA = a.size(), LB = b.size(), L = max(LA, LB), carry = 0;
    
    string x = string(L, '0'); 
    
    while(L--)
    {
    	LA--; LB--;
    	
        if(LA >= 0) carry += a[LA] - '0'; 
        if(LB >= 0) carry += b[LB] - '0'; 
        
        if(carry < 10) x[L] = '0' + carry, carry = 0;
        else x[L] = '0' + carry - 10, carry = 1;
    }
    
    if(carry) x = '1' + x; 
    return x;
} 

string prod(const string &a, const string &b)
{
	int LA = a.size(), LB = b.size();
	
	if(a=="0" || b=="0") return "0";
	else if(LA==1)
	{
		int m = a[0] - '0';
		
		string ans = string(LB, '0');
		
		int lleva = 0;
		
		while(LB--)
		{
			int d = (b[LB] - '0') * m + lleva;
			lleva = d/10;
			ans[LB] += d%10;
		}
		
		if(lleva) ans = (char)(lleva + '0') + ans;
		return ans;
	}
	else if(LB==1) return prod(b, a);
	else
	{
		string ans = "0";
		string ceros = "";
		for(int i=LA-1; i>=0; i--)
		{
			string s = prod(string(1, a[i]), b) + ceros;
			ceros += "0";
			ans = suma(ans, s);
		}
		return ans;
	}
}

bool check(const string &s)
{
	int L = s.size();
	for(int i=0, j=L-1; i<j; i++,j--)
		if(s[i] != s[j])
			return 0;
	return 1;
}

vector <string> good;

bool menor(const string &s1, const string &s2)
{
	if(s1.size() != s2.size()) return s1.size() < s2.size();
	return s1 < s2;
}

int f(string &s)
{
	if(menor(good[0], s))
	{
		int lo = 0, hi = good.size();
		while(hi - lo > 1)
		{
			int mid = (lo + hi) / 2;
			
			if(menor(good[mid], s)) lo = mid;
			else hi = mid;
		}
		return hi;
	}
	else return 0;
}

#define MAXD 15

int main()
{
	good.push_back("1");
	good.push_back("4");
	good.push_back("9");
	good.push_back("121");
	good.push_back("484");
	good.push_back("10201");
	good.push_back("12321");
	good.push_back("14641");
	good.push_back("40804");
	good.push_back("44944");
	
	string palin, square;
	
	for(int L=1; L<=MAXD-1; L++)
	{
		// 1xx1
		for(int mask=0; mask<(1<<L); mask++)
		{
			string s = "";
			for(int i=0; i<L; i++)
				s += '0' + ((mask & (1<<i)) != 0);
			
			string rs = s;
			reverse(rs.begin(), rs.end());
			
			palin = "1" + rs + s + "1";
			square = prod(palin, palin);
			if(check(square)) good.push_back(square);
		}
		
		// 2002
		palin = "2" + string(2*L, '0') + "2";
		square = prod(palin, palin);
		if(check(square)) good.push_back(square);
			
			
		if(L <= MAXD - 2)
		{
			// 1xdx1
			for(int mask=0; mask<(1<<L); mask++)
			{
				string s = "";
				for(int i=0; i<L; i++)
					s += '0' + ((mask & (1<<i)) != 0);
			
				string rs = s;
				reverse(rs.begin(), rs.end());
			
				palin = "1" + rs + "0" + s + "1";
				square = prod(palin, palin);
				if(check(square)) good.push_back(square);
			
				palin[L+1] = '1';
				square = prod(palin, palin);
				if(check(square)) good.push_back(square);

				palin[L+1] = '2';
				square = prod(palin, palin);
				if(check(square)) good.push_back(square);
			}
			
			// 20d02
			
			palin = "2" + string(L, '0') + "0" + string(L, '0') + "2";
			square = prod(palin, palin);
			if(check(square)) good.push_back(square);
			
			palin = "2" + string(L, '0') + "1" + string(L, '0') + "2";
			square = prod(palin, palin);
			if(check(square)) good.push_back(square);
  		}
  	}
  	
  	cout<<"Input File: ";
 	string fname;
 	
  	cin>>fname;
  	
  	freopen(fname.c_str(), "r", stdin);
  	freopen("out.txt", "w", stdout);
  	
  	int nCasos;
  	cin>>nCasos;
  	
  	for(int caso=1; caso<=nCasos; caso++)
  	{
  		string A, B;
  		cin>>A>>B;
  		
  		B = suma(B, "1");
  		
  		cout<<"Case #"<<caso<<": "<<f(B)-f(A)<<endl;
  	}
  	
	return 0;
}
