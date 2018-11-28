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
#include<utility>
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

int main()
{
	fstream in,out;
	//in.open("test.in.txt",ios::in); out.open("test.out",ios::out);
	//in.open("D-small-attempt0.in",ios::in); out.open("D-small-01.out",ios::out);
	in.open("D-large.in",ios::in); out.open("D-large-0.out",ios::out);

	istream& input = in;
	ostream& output = out;
	
	ll case_id,total_case;
    ll l[101][101],p[101][101];
	input>>total_case; 
	ll I,H,K,L,M,N , y, z,w;
	ld x;
	bool u[100];
	
	for(case_id=1;case_id<=total_case;case_id++)
	{
        input>>N;
        vector<pair<ld,ll> > v;
        for(I=0;I<N;I++)
        {
            input>>x;
            v.push_back(make_pair(x,1));
        }
        
        for(I=0;I<N;I++)
        {
            input>>x;
            v.push_back(make_pair(x,2));
        }
        
        sort(v.begin(),v.end());
        
        y=N;
        z=0;
        w=0;
        for(vector<pair<ld,ll> >::iterator it = v.begin();it != v.end();it++)
        {
            if(it->second == 2) w++;
            else w==0 ? y-- : w--;
        }

        w=0;
        for(vector<pair<ld,ll> >::reverse_iterator it = v.rbegin();it != v.rend();it++)
        {
            if(it->second == 2) w++;
            else w==0 ? z++ : w--;
        }
        
		output<<"Case #"<<case_id<<": "<<y<<" "<<z;
		output<<endl;
	}
    system("PAUSE");
    return EXIT_SUCCESS;
}
