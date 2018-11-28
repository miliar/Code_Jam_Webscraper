#include<iostream>
#include<cstdio>
#include<fstream>
#include<vector>
#include<set>
#include<map>
#include<algorithm>
#include<sstream>
#include<string>
#include<iterator>
#include<functional>
#include<time.h>
#include<iomanip>
using namespace std;
typedef long long int ll;
typedef long double ld;
#define INF 100000000000000000LL

ll diff(ll a,ll b)
{
    return a>b ? a-b : b-a;
}

/*#define COMB_NUM 10001L
ll comb[COMB_NUM][COMB_NUM];
//need init_comb();
void init_comb()
{
    comb[0][0]=1;
    ll i,j;
    for(i=1;i<COMB_NUM;i++)
    {
        comb[i][0]=comb[i][i]=1;
        for(j=1;j<i;j++)
            comb[i][j]=comb[i-1][j]+comb[i-1][j-1];
    }
}
*/

#define print(a)      for(int i=0;i<a.size();i++) cout<<a[i]<<" "; cout<<endl;
#define print2n(a,n)      for(int i=0;i<=n;i++) cout<<a[i]<<" "; cout<<endl;

void llFromString(const string &s,ll &a,ll &b)
{
    string replacedString = s;
    replace_if(replacedString.begin(),
               replacedString.end(),
               bind2nd(equal_to<char>(),'.'),
               ' ');
               
    istringstream buffer(replacedString);
    buffer>>a;
    if(buffer.good())
    {
        buffer>>b;
    }
    else
    {
        b=0;
    }
}


template<class T>
vector<T> split(const std::string &s) {
    
    string replacedString = s;
    replace_if(replacedString.begin(),
               replacedString.end(),
               bind2nd(equal_to<char>(),'.'),
               ' ');
    
    vector<T> ret;
    istringstream buffer(replacedString);
    copy(istream_iterator<T>(buffer),
         istream_iterator<T>(), back_inserter(ret));
    return ret;    
}// vector<ll> k = split<ll>(s);
ll s[1000001],m[1000001],man[1000001];
struct Tree {
    vector<Tree*> trees;
    ll s;
    ll n;
};

ll low, up;

Tree t[1000001];

ll dfs(Tree aTree) {
    if(aTree.s<low || aTree.s>up) return 0;
    ll ret = 1;
    for(int I=0;I<aTree.trees.size();I++) {
        ret += dfs(*aTree.trees[I]);
    }
    return ret;
}
int main()
{
	fstream in,out;
	//in.open("test.in.txt",ios::in); out.open("test.out.txt",ios::out);
	in.open("A-small-attempt0.in",ios::in); out.open("A-small-0.out",ios::out);
	//  in.open("A-large.in",ios::in); out.open("A-large-0.out",ios::out);

	istream& input = in;
	ostream& output = out;

	ll case_id,total_case,temp,ans;

	input>>total_case; 
	ll I,H,K,L,as,cs,rs,am,cm,rm,D,N,s0,m0;
	
	for(case_id=1;case_id<=total_case;case_id++)
	{
        input>>N>>D>>s0>>as>>cs>>rs>>m0>>am>>cm>>rm;
        ans=1;
        s[0]=s0;
        m[0]=m0;
        
        t[0].s=s0;
        t[0].n=0;

        for(I=1;I<N;I++) {
            s[I] = (s[I-1]*as+cs)%rs;
            m[I] = (m[I-1]*am+cm)%rm;
            man[I] = m[I]%I;
            t[man[I]].trees.push_back(t+I);
            t[I].n=I;
            t[I].s=s[I];
        }
        low = s[0]-D, up=s[0];
        
        for(;low<=s[0];low++,up++) {
            ans = max(ans, dfs(t[0]));
        }
        
        //for(I=0;I<N;I++) cout<<s[I]<<" "<<man[I]<<endl;
        for(I=0;I<N;I++) t[I].trees.clear();
        
		output<<"Case #"<<case_id<<": ";
		output<<ans;
		output<<endl;
	}
    system("PAUSE");
    return EXIT_SUCCESS;
}











