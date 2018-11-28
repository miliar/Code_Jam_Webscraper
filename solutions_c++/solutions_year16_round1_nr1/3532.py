#include<bits/stdc++.h>
#define MX 100000
#define pb push_back
#define mp make_pair
#define fs first
#define sec second
#define sc scanf
#define pr printf
using namespace std;
int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	freopen("A-large.in","r",stdin);
	freopen("output_large1.in","w",stdout);
	int t,n,i,j,k,T;
	string s;
    cin>>T;
    for(t=1;t<=T;++t){
    	cin>>s;
    	n=s.length();
    	deque<char> d;
    	d.push_back(s[0]);
    	for(i=1;i<n;++i){
    		if(s[i]>=d[0])
    			d.push_front(s[i]);
    		else
    			d.push_back(s[i]);
    	}
    	cout<<"Case #"<<t<<": ";
    	for(i=0;i<n;++i)
    		cout<<d[i];
    	cout<<endl;
    }
	return 0;
}
