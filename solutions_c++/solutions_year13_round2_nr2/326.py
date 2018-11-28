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
#include<cmath>
using namespace std;
typedef long long int ll;
typedef long double ld;
#define INF 100000000000000000LL

ll diff(ll a,ll b)
{
    return a>b ? a-b : b-a;
}

#define COMB_NUM 1001L
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
    init_comb();
	fstream in,out;
	//in.open("test.in.txt",ios::in); out.open("test.out.txt",ios::out);
	//in.open("B-small-attempt3.in",ios::in); out.open("B-small-0.out",ios::out);
	  in.open("B-large.in",ios::in); out.open("B-large-0.out",ios::out);

	istream& input = in;
	ostream& output = out;

	ll case_id,total_case,temp;
    ld ans;
	input>>total_case; 
	ll I,H,K,L,N,n,x,y,r,s;

	for(case_id=1;case_id<=total_case;case_id++)
	{
        input>>n>>x>>y;
        s=0;temp=1;
        for(r=-1;s<n;r++)
        {
            s+=temp;
            temp+=4;
        }
        //cout<<r<<" "<<temp<<" "<<s<<endl;
        temp -=4;
        
        if(x<0) x=-x;
        
        if(x+y<2*r) ans = 1.0;
        else if(x+y>2*r) ans = 0.0;
        else if(x==0)
        {
            if(s==n) ans = 1.0;
            else ans = 0.0;
        }
        else
        {
            ll b = n-s+temp;
            if(b-y-1<0) ans = 0.0;
            else if(b-r*2>=y+1) ans = 1.0;
            else  
            {
                ld no = 0.0;
                ld de = pow((ld)2.0,(ld)b);
                for(H=0;H<=y;H++) no+=comb[b][H];
                //ans = 1.0 - (no / (ld)(1<<b));
                ans = 1.0 - (no / de);
            }
        }
        
        output<<fixed;
        output.precision(10);
		output<<"Case #"<<case_id<<": ";
		output<<ans;
		output<<endl;
	}
    system("PAUSE");
    return EXIT_SUCCESS;
}










