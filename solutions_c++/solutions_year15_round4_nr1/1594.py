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

#define MAXX 107

#define right asjfawje4r
#define left lasfjejf
#define INF (1<<29)


int R, C;

char graph[MAXX][MAXX];

int state[MAXX][MAXX];
vector<paii>v;
paii left, right, up, down;
bool visited[MAXX][MAXX];


paii operator+(paii x, paii y)
{
	return MP(x.fr + y.fr, x.sc + y.sc);
}


void traverse(paii u)
{
	paii lastPos = u;

	paii lastDirection;

	char ch;

	

	while( 0 <= u.fr && u.fr < R && 0 <= u.sc && u.sc < C)
	{


		ch = graph[u.fr][u.sc];

		if(ch != '.')
		{
			lastPos = u;

			if(visited[u.fr][u.sc])
			{
				break;
			}
			visited[u.fr][u.sc] = true;
		}


		if(ch == '<')
		{
			lastDirection = left;
		}
		else if ( ch == '>')
		{
			lastDirection = right;
		}
		else if(ch == 'v')
		{
			lastDirection = down;
		}
		else if(ch == '^')
		{
			lastDirection = up;
		}

		u = u + lastDirection;
	}


	if(0 <= u.fr && u.fr < R && 0 <= u.sc && u.sc < C)
	{

	}
	else
	{
		 u = lastPos;
		state[u.fr][u.sc] = 1;
		v.pb(u);
	}



}



int solve()
{

	int ret = 0;


	mem(state, 0);

	mem(visited, 0);


	v.clear();



	
	loop(i, R)
	{
		loop(j, C)
		{
			if(graph[i][j] != '.')
			{
				traverse(MP(i, j));
			}
		}
	}

	loop(i, SZ(v))
	{
		int cnt = 0;

		loop(j, R)
		{
			if(graph[j][ v[i].sc] != '.')
			{
				//cerr<<"here "<<j<<" "<<v[i].sc<<endl;
				cnt++;
			}
		}

		loop(j, C)
		{
			if(graph[v[i].fr][j] != '.')
			{
				//cerr<<"here "<<v[i].fr<<" "<<j<<endl;
				cnt++;
			}
		}

		if(cnt == 2)
		{
			return INF;
		}
		//dump(cnt);
	}


	return SZ(v);

}




int main()
{
	left = MP(0, -1);
	right = MP(0, 1);
	up = MP(-1, 0);
	down = MP(1, 0);



	int kases, kaseno = 0;

	cin>>kases;

	while(kases--)
	{
		cin>>R>>C;

		loop(i, R)
		{
			cin>>graph[i];
		}

		int ret = solve();



		pf("Case #%d: ", ++kaseno);

		if(ret == INF)
		{
			cout<<"IMPOSSIBLE"<<endl;
		}
		else
		{
			cout<<ret<<endl;
		}
	}





}
