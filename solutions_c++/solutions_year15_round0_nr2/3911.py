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
#define debug(args...) cout,args; cerr<<endl;
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


#define MAXX 1007
#define INF (1<<29)

int D;
int p[MAXX];

int maxElm = 0;

int getMove(int n)
{
	int totalMove = 0;

	loop(i, D)
	{
		totalMove += ((p[i]-1) / n);
	}

	return totalMove + n;
}





int solve()
{
	int low = 1, high = maxElm;
	int minMove = INF;
	while(low <= high)
	{
		//cout<<"low = "<<low<<" high = "<<high<<endl;
		if(high - low <= 10)
		{
			for(int i=low; i<=high; i++)
			{
				minMove = min(minMove, getMove(i));
			}
			break;
		}
		else
		{
			int m1, m2;
			int d = (high - low)/3;
			m1 = low + d;
			m2 = low + 2*d;

			int k1 = getMove(m1);
			int k2 = getMove(m2);
			//dump(k1);
			//dump(k2);
			if(k1 < k2)
			{
				high = m2;
			}
			else if(k1 > k2)
			{
				low = m1;
			}
			else
			{
				high = m2;
				low = m1;
			}

		}

	}

	return minMove;
}






int main()
{
	int kases, kaseno = 0;

	sf("%d", &kases);

	while(kases--)
	{
		sf("%d", &D);
		loop(i, D)
		{
			sf("%d", &p[i]);
			maxElm = max(maxElm, p[i]);
		}
		//cout<<"I M HERE"<<endl;
		pf("Case #%d: %d\n", ++kaseno, solve());
	}


}
