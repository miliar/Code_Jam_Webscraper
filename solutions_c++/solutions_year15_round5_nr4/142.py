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

int main()
{
	fstream in,out;
	//in.open("test.in.txt",ios::in); out.open("test.out.txt",ios::out);
	in.open("D-small-attempt0.in",ios::in); out.open("D-small-0.out",ios::out);
	//  in.open("D-large.in",ios::in); out.open("D-large-0.out",ios::out);

	istream& input = in;
	ostream& output = out;

	ll case_id,total_case,temp,ans;

	input>>total_case; 
	ll I,H,K,L,N,P,E[10001],F[10001];
	for(case_id=1;case_id<=total_case;case_id++)
	{  
        multiset<ll> sp,s,st,a;
        input>>P;
        for(I=0;I<P;I++) input>>E[I];
        for(I=0;I<P;I++) {
            input>>F[I];
            for(H=0;H<F[I];H++) sp.insert(E[I]);
        }
        
        sp.erase(sp.find(0));
        s.insert(0);
        
        while(sp.size()){
           /* cout<<"s prime: ";
            for(multiset<ll>::iterator it=sp.begin();it!=sp.end();it++) cout<<*it<<" ";
            cout<<endl;
            
            cout<<"s: ";
            for(multiset<ll>::iterator it=s.begin();it!=s.end();it++) cout<<*it<<" ";
            cout<<endl;
            */
            ll t=*min_element(sp.begin(),sp.end());
            a.insert(t);
            for(multiset<ll>::iterator it=s.begin();it!=s.end();it++) {
                st.insert(*it+t);
                multiset<ll>::iterator it2 = sp.find(*it+t);
                if(it2 !=sp.end()){
                    
                    sp.erase(it2);
                } else {
                    cout<<"warning"<<endl;
                }
                 
            }
            s.insert(st.begin(),st.end());
            st.clear();
            
        }
        
        
        
		output<<"Case #"<<case_id<<": ";
		for(multiset<ll>::iterator it=a.begin();it!=a.end();it++) output<<*it<<" ";
		//output<<ans;
		output<<endl;
	}
    system("PAUSE");
    return EXIT_SUCCESS;
}











 
