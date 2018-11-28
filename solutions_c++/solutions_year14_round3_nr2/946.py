#include<iostream>	//------------------------------------------------------------//
#include<cstdio>    //  ___  ___ _____ ______                                     //
#include<algorithm> //  |  \/  |/  ___|| ___ \     This C++ Template Belongs to   //
#include<cmath>     //  | .  . |\ `--. | |_/ /        Manish Singh Bisht          //
#include<vector>    //  | |\/| | `--. \| ___ \       http://fb.me/manish05        //
#include<set>       //  | |  | |/\__/ /| |_/ /    Email: manish05@facebook.com    //
#include<map>       //  \_|  |_/\____/ \____/                                     //
#include<functional>//------------------------------------------------------------//
#include<string>
#include<cstring>
#include<bitset>
#include<cstdlib>
#include<queue>
#include<utility>
#include<fstream>
#include<sstream>

#include<stack>
#include<cstdio>
#include<ctime>
         

using namespace std;
#define gc getchar_unlocked
#define MEM(a,b) memset(a,(b),sizeof(a))
#define FOR(i,n) for(int i=(0);i<(n);i++)
#define TR(v,it) for(typeof(v.begin()) it(v.begin()) ; it != v.end() ; it++)
#define SZ(v) (int)sizeof(v)
#define CLEAR(a) memset((a),0,sizeof(a))
#define S(n) scanf("%d", &n)
#define P(k) printf("%d\n", k)
#define pb push_back
#define mp make_pair
#define ll long long
#define VI vector<int>
#define PII pair<int, int>
#define ft first
#define sd second
#define all(a) a.begin(),a.end()
#define lb lower_bound
#define ub upper_bound
#define inf (1<<30)
#define PNL printf("\n")
#define md 1000000007
#define bigger(a,b) (a>b?a:b)
#define smaller(a,b) (a<b?a:b)
#define positive(a) (bigger(a,-a))
ll modPow(ll a,ll b)
{ll x;
    for(x=1;b>0;b/=2,a=(a*a)%md)
        if(b%2==1)
                x=(x*a)%md;
  return x%md;
}

string convertInt(int number){stringstream ss;ss << number;return ss.str();}
int convertString(string s){int num;stringstream sstr(s);sstr>>num;return num;}
int gcd(int a, int b){ return b?gcd(b,a%b):a; }

unsigned int hash(const char* s,unsigned int seed = 0)
{
	unsigned hash = seed;while(*s)
    {
        hash = hash * 101  +  *s++;
    }
    return hash;
}
int main(int argc,char *argv[])
{
ifstream fin(argv[1]);
ofstream fout("output.txt");

	int t;
	fin>>t;
	for(int i=1;i<=t;i++){
	fout<<"Case #"<<i<<": ";
		int n;
		fin>>n;
		string str[n];
		int order[n];
		set<int> mid[26];
		set<int> ex[26];
		FOR(i,n){
			order[i]=i;
			fin>>str[i];
			for(int j=0;j<str[i].length();j++){
				ex[str[i][j]-'a'].insert(i);
			}
			for(int j=1;j<str[i].length()-1;j++){
				
				if(str[i][j]!=str[i][j-1] && str[i][j]!=str[i][j+1])
				mid[str[i][j]-'a'].insert(i);
			}
			string tempS=str[i];
			str[i]="";
			int k=0;
			while(k<tempS.length()){
				str[i].pb(tempS[k]);
				while(k<tempS.length() && tempS[k]==str[i][str[i].length()-1])k++;
			}
		}
		
	int Ans=0;;
		int imp=0;
		
		for(int i=0;i<26;i++){
			if(mid[i].size()>0 && ex[i].size()>1)
				imp=1;
		}
		
		int cnt[26],cnt2[26];
		
		FOR(i,26)cnt[i]=0;
		FOR(i,n){
			FOR(j,str[i].length())
				cnt[str[i][j]-'a']++;
		}		
		if(!imp){
			do
			{
				
				FOR(i,26)cnt2[i]=0;
				
				int flag=1;
				char last=str[order[0]][0];
				for(int i=0;i<n;i++){
					for(int j=0;j<str[order[i]].length();j++)
					{
							if(str[order[i]][j]==last)cnt2[last-'a']++;
							else if(cnt2[str[order[i]][j]-'a']>0){
								flag=0;
								goto End;
							}else {
								last=str[order[i]][j];
								cnt2[last-'a']++;
							}
					}
				}

				End:
				if(flag)Ans++;
			
			}while(next_permutation(order,order+n));
		}
	fout<<Ans<<endl;
	}
fin.close();
fout.close();
return 0;
}


