/*	SURENDRA KUMAR MEENA	*/
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <queue>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <ctime>
using namespace std;
typedef long long int LL;
#define FF(i,m,n)	for(int i=m;i<n;i++)
#define F(i,n)	FF(i,0,n)
#define R(i,n,k) for(int i=n;i>=k;i--)
#define CLR(s,v) memset(s,v,sizeof(s))
string to_str(LL x){ ostringstream o;o<<x;return o.str();}
LL to_int(string s){ istringstream st(s); LL i;	st>>i;return i;}

string multi(string s1,string s2){
	string s;
	int i,j,k,l,m,c,sz1=s1.length(),sz2=s2.length();
	for(i=0;i<sz1+sz2;i++)	s+="0";
	char ch;
	for(i=sz2-1;i>=0;i--){
		c=0;
		for(j=sz1-1;j>=0;j--){
			m=(s2[i]-'0')*(s1[j]-'0')+c+s[sz1-j-1+sz2-i-1]-'0';
			c=m/10;
			m%=10;
			s[sz1-j-1+sz2-i-1]=(char)(m+'0');
		}
		if(c>0)
			s[sz1-j-1+sz2-i-1]=(char)((s[sz1-j-1+sz2-i-1]-'0'+c)+'0');
	}
	i=sz1+sz2-1;
	while(s[i]=='0'){
		s.erase(s.begin()+i);
		i--;
	}
	reverse(s.begin(),s.end());
	return s;
}

bool isPalindrome(string s) {
    string ss = s;
    reverse(ss.begin(), ss.end());
    return s==ss;
}

vector<string> vs[101];
vector<string> allValues;
set<string> st;
bool cmp(string s1, string s2) {
    int l1 = s1.size();
    int l2 = s2.size();
    if(l1!=l2)  return l1<l2;
    return s1<s2;
}
void preComp() {
    F(i,101)
        vs[i].clear();
    vs[1].push_back("0");
    vs[1].push_back("1");
    vs[1].push_back("2");
    vs[2].push_back("11");
    
    for(int i=4; i<52; i+=2) {
        string s = "1";
        s += string(i-2, '0');
        s += "1";
        vs[i].push_back(s);
    }

    FF(i,3,52) {
        for(int len=i-2; len>0; len-=2) {
            string s = string((i-len)/2-1, '0');
            F(k,vs[len].size()) {
                string ss = "1";
                ss += s;
                ss += vs[len][k];
                ss += s;
                ss += "1";
                
                if(isPalindrome(multi(ss,ss))) {
                    vs[i].push_back(ss);
                }
            }
        }
//        cout<<i<<" "<<vs[i].size()<<endl;
    }
    FF(i,1,52) {
        F(j,vs[i].size())   allValues.push_back(vs[i][j]);
    }
    allValues.push_back("3");
    FF(i,2,52) {
        string s = "2";
        s += string(i-2,'0');
        s += "2";
        allValues.push_back(s);

        if(i%2==1) { 
            string s = "2";
            s += string(i/2-1,'0');
            s += "1";
            s += string(i/2-1,'0');
            s += "2";
            allValues.push_back(s);
        }
    }
    
    sort(allValues.begin(), allValues.end(), cmp);
//    F(i,422) cout<<i+1<<" : "<<allValues[i]<<endl;
    
    F(i,allValues.size()) {  
        allValues[i] = multi(allValues[i], allValues[i]);
        st.insert(allValues[i]);
    }
    
//    cout<<allValues.size()<<endl;
 //   cout<<allValues[allValues.size()-1].size()<<endl;
  //  cout<<allValues[allValues.size()-1]<<endl;
}

int getCount(string n) {
    int lft=0, rgt=allValues.size()-1, md;
    while(rgt-lft>1) {
        md = (lft+rgt)/2;
        if(cmp(n, allValues[md])) rgt = md-1;
        else                    lft = md;
    }
    while(true) {
        if(cmp(n, allValues[lft]))   return lft-1;
        lft++;
    }
    return md;
}

int main(){
    preComp();
    int t;
    cin>>t;
    FF(kase,1,t+1){
        cout<<"Case #"<<kase<<": ";
        string a,b;
        cin>>a>>b;
        int ans = getCount(b) - getCount(a);
        ans += (st.find(a)!=st.end()) ? 1 : 0;
        cout<<ans<<endl;
    }
    return 0;
}
