/*Archit Mittal*/

#include<iostream>
#include<algorithm>
#include<vector>
#include<string>
#include<map>
#include<sstream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<climits>
#include<cmath>
#include<utility>
#include<set>
#include<ios>
#include<fstream>
#include<iomanip>

#define ull unsigned long long
#define ll long long
#define pii pair<int,int>
#define pb(x) push_back(x)
#define S(x) scanf("%d",&x)
#define Sl(x) scanf("%lld",&x)
#define M(x,i) memset(x,i,sizeof(x))
#define F(i,a,n) for(i=(a);i<(n);++i)
#define FD(i,a,n) for(i=(a);i>=(n);--i)

using namespace std;

int v[200][200];
int main()
{
    ifstream fin;
    ofstream fout;
    
     fin.open("inp.in");
    fout.open("out.txt");
    
    int t,i,j,cnt,sum,k,n,tot;
    vector<int> tmp;
    fin>>t;

    int ts=1;
    while(t--){
	    fout<<"Case #"<<ts++<<": ";
	    fin>>n;
	    sum=0;
	    string s;
	    set<string> st;
	    F(i,0,n){
		    fin>>s;
		    cnt=1;
		    string str="";
		    str+=s[0];
		    k=0;
		    tot=0;
		    F(j,1,s.length()){
			if(s[j]==s[j-1])cnt++;
			else {
				//cout<<i<<" "<<k<<" "<<cnt<<endl;
				v[i][k++]=cnt;
				cnt=1;
				tot++;
				str+=s[j];
			}
		    }
		    if(cnt){
			    //cout<<i<<" "<<k<<" "<<cnt<<endl;
			    tot++;
			    v[i][k]=cnt;
		    }
		    st.insert(str);
	    }
	    //cout<<tot<<endl;
	    if(st.size()>1){
		    fout<<"Fegla Won\n";
	    } else {
		    F(i,0,tot){
			    tmp.clear();
			    F(j,0,n){
				   // cout<<j<<" "<<i<<" "<<v[j][i]<<endl;
				    tmp.pb(v[j][i]);
			    }
			    sort(tmp.begin(),tmp.end());
			    int sz=tmp.size();
			   // cout<<sz<<endl;
			    if(sz&1){
				    F(j,0,n){
					    sum+=fabs(v[j][i]-tmp[sz/2]);
				    }
		    			//cout<<sum<<endl;
			    } else {
				    int val1=0;
				    int val2=0;
				    F(j,0,n){
					    val1+=fabs(v[j][i]-v[sz/2][i]);
				    }
				    F(j,0,n){
					    val2+=fabs(v[j][i]-v[(sz/2)+1][i]);
				    }
				    sum+=min(val1,val2);
			    }
		    }
		    fout<<sum<<endl;
	    }
    }
}
