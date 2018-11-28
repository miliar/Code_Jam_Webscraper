// MainProject.cpp : Defines the entry point for the console application.
//
 
#pragma comment(linker, "/STACK:66777216")
#define _CRT_SECURE_NO_WARNINGS
#include <unordered_set>
#include <unordered_map>
#include <functional>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <fstream>
#include <cassert>
#include <iomanip>
#include <cstring>
#include <cstdio>
#include <cctype>
#include <limits>
#include <bitset>
#include <string>
#include <vector>
#include <ctime>
#include <queue>
#include <stack>
#include <cmath>
#include <set>
#include <map>
#include <vector>
using namespace std;
 
typedef long long LL;
typedef long double LD;
 
 
#define rep(i,n) for(int (i)=0;(i)<(int)(n);++(i))
#define rer(i,l,u) for(int (i)=(int)(l);(i)<=(int)(u);++(i))
#define reu(i,l,u) for(int (i)=(int)(l);(i)<(int)(u);++(i))
#if defined(_MSC_VER) || __cplusplus > 199711L
#define aut(r,v) auto r = (v)
#else
#define aut(r,v) typeof(v) r = (v)
#endif
#define each(it,o) for(aut(it, (o).begin()); it != (o).end(); ++ it)
#define pb(x) push_back(x)
#define mp(x,y) make_pair((x),(y))
#define all(v) (v).begin(), (v).end()
#define sz(v) (int)(v).size()
#define mset(m,v) memset(m,v,sizeof(m))
 
#define INF 0x3f3f3f3f
#define INFL 0x3f3f3f3f3f3f3f3fLL
 
typedef vector<int> vi; typedef pair<int,int> pii; typedef vector<pair<int,int> > vpii;
typedef long long ll; typedef vector<long long> vl; typedef pair<long long,long long> pll; typedef vector<pair<long long,long long> > vpll;
typedef vector<string> vs; typedef long double ld;
 
 
#define CIA

bool go;

bool isPrm(LL in, LL& fdiv)
{
	if (in <=1)
	{
		fdiv=1;
        return false;
    }
    else if (in == 2)
    {
        return true;
    }
    else if (in % 2 == 0)
    {
    	fdiv=2;
        return false;
    }
    else
    {
        bool ret = true;
        int dvr = 3;
        double num_d = static_cast<double>(in);
        int ul = static_cast<int>(sqrt(num_d)+1);
        
        while (dvr <= ul)
        {
            if (in % dvr == 0)
            {
                ret = false;
                fdiv=dvr;
                break;
            }
            dvr +=2;
        }
        return ret;
    }
}


void permRec( char* v, string pre, int n, int k, int& j )
{
	if(!go)
		return;
	
	if (k == 0) 
	{
        // pre
        //cout << pre << endl;
        string s = "1";
        s.append(pre);
        s.append(1,'1');
        
        //cout << s << endl;
        bool ret = true;
        LL arr[14];
        rer(bs,2,10)
        {
        	LL val = 0;
        	for(int x=s.length()-1; x >=0; --x)
        	{
        		if( s[x] == '1' )
        		{
        			val += pow(bs,(s.length()-x-1));
        		}
			}
			LL fdiv = 0;
			if(isPrm(val, fdiv))
			{
				ret = false;
				break;
			}
			else
			{
				arr[bs] = fdiv;
			}
		}
		
		if(ret)
		{
			cout << s << " ";
			rer(y,2,10)
			{
				cout << arr[y] << " ";
			}
			cout << endl;
			
			--j;
			if(j==0)
				go = false;
		}
        
        return;
    }
    
    rep(i,n)
    {
    	string newPrefix = pre;
    	newPrefix.append(&v[i], 1); 

        permRec(v, newPrefix, n, k - 1, j);
		
		if(!go)
			return; 
	}
}

void perm( char* v, int k, int& j )
{
	permRec( v, "", 2, k, j );
}

int main()
{
#ifdef CIA
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#else
#define TASK "matrix"
	//freopen(task".in", "r", stdin);
	//freopen(task".out", "w", stdout);
#endif

	int cs;
	cin >> cs;
	
	rer(i,1,cs)
	{
		int n,j;
		cin >> n >> j;
		char set[] = {'0', '1'};
		
		cout << "Case #" << cs << ":" << endl;
		
		go = true;
		perm(set, n-2, j);
		
		
		
	}

	
 
#ifdef CIA
	cerr << fixed << setprecision(3) << "\nExecution time = " << clock() / 1000.0 << "s\n";
#endif
	return 0;
}

