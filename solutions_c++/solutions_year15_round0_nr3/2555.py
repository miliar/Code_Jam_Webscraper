/****************************************************************
   ▄█    █▄       ▄████████    ▄████████  ▄█  ▀█████████▄
  ███    ███     ███    ███   ███    ███ ███    ███    ███
  ███    ███     ███    ███   ███    █▀  ███   ███    ███
 ▄███▄▄▄▄███▄▄   ███    ███   ███        ███  ▄███▄▄▄██▀
▀▀███▀▀▀▀███▀  ▀███████████ ▀███████████ ███ ▀▀███▀▀▀██▄
  ███    ███     ███    ███          ███ ███    ███    ██▄
  ███    ███     ███    ███    ▄█    ███ ███    ███    ███
  ███    █▀      ███    █▀   ▄████████▀  █▀   ▄█████████▀
****************************************************************/



#include<bits/stdc++.h>


#define FOR(i, s, e) for(int i=s; i<e; i++)
#define loop(i, n) FOR(i, 0, n)
#define sf scanf
#define pf printf
#define pb push_back
#define MP make_pair
#define fr first
#define sc second
#define ll long long
#define dd double
#define all(v) v.begin(), v.end()
#define PI acos(-1.0)
#define mem(ara, value) memset(ara, value, sizeof(ara))
#define paii pair<int, int>
#define pall pair<ll, ll>
#define SZ(a) int(a.size())
#define read(nm) freopen(nm, "r", stdin)
#define write(nm) freopen(nm, "w", stdout)

#define take(args...) asdf,args
#define dump(x) cerr<<#x<<" = "<<x<<endl
#define debug(args...) cerr,args; cerr<<endl;
using namespace std;


template<typename T>
ostream& operator<<(ostream& output, vector<T>&v)
{
    output<<"[ ";
    if(SZ(v))
    {
        output<<v[0];
    }
    FOR(i, 1, SZ(v))
    {
        output<<", "<<v[i];
    }
    output<<" ]";
    return output;
}

template<typename T1, typename T2>
ostream& operator<<(ostream& output, pair<T1, T2>&p)
{
    output<<"( "<<p.fr<<", "<<p.sc<<" )";
    return output;
}




template<typename T>
ostream& operator,(ostream& output, T x)
{
    output<<x<<" ";
    return output;
}



struct ASDF{
    ASDF& operator,(int &a) {
        sf("%d", &a);
        return *this;
    }
    ASDF& operator,(long int &a){
        sf("%ld", &a);
        return *this;
    }
    ASDF& operator,(long long int &a){
        sf("%lld", &a);
        return *this;
    }
    ASDF& operator,(char &c){
        sf("%c", &c);
        return *this;
    }
    ASDF& operator,(double &d){
        sf("%lf", &d);
        return *this;
    }

    template<typename T>
    ASDF& operator,(T &a){
        cin>>a;
        return *this;
    }
}asdf;



//Header ends here

int len, repeat;
string given, str;


string mul(string a, string b)
{
	/*
	if(a == "-1")
	{
		return "-" + b;
	}
	else if(a[0] == '-')
	{
		return mul(b, a.substr(1));
	}*/
	if(a[0] == '-')
	{
		string tmp = mul(a.substr(1), b);
		if(tmp[0] == '-')
		{
			return tmp.substr(1);
		}
		else
		{
			return "-" + tmp;
		}
	}


	if(a == "1")
	{
		return b;
	}
	else if(b == "1")
	{
		return a;
	}
	else if(a == "i")
	{
		if(b == "i")
			return "-1";
		else if(b == "j")
			return "k";
		else
			return "-j";
	}
	else if(a == "j")
	{
		if(b == "i")
			return "-k";
		else if(b == "j")
			return "-1";
		else
			return "i";
	}
	else if(a == "k")
	{
		if(b == "i")
			return "j";
		else if(b == "j")
			return "-i";
		else
			return "-1";
	}
}
bool solve()
{
	bool iFound, kFound, minusFound;
	iFound = kFound = minusFound = 0;
	
	string now = "1";

	loop(i, SZ(str))
	{
		string tmp;
		tmp += str[i];
		now = mul(now, tmp);
		//dump(now);
		if(now == "i")
		{
			iFound = true;
		}
		else if(now == "k" && iFound)
		{
			kFound = true;
		}
		//cerr<<now<<endl;
	}

	if(now == "-1")
		minusFound = true;

	return (iFound && kFound && minusFound);
}

int main()
{
	//cout<<mul("-k", "k")<<endl;
	int kases, kaseno = 0;
	cin>>kases;

	while(kases--)
	{
		cin>>len>>repeat;
		cin>>given;
		str = "";
		loop(i, repeat)
		{
			str = str + given;
		}
		if(solve())
		{
			pf("Case #%d: YES\n", ++kaseno);
		}
		else
		{
			pf("Case #%d: NO\n", ++kaseno);
		}
	}

    return 0;
}
