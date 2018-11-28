//Sacch hai mahaz sangharsh hi!
#include <bits/stdc++.h>
#define mod 1000000007
#define ll long long int
#define pb(x) push_back(x)
#define MP(x,y) make_pair(x,y)
using namespace std;

int main(){
	ios::sync_with_stdio(false);
	freopen ("out.txt","w",stdout);
    freopen ("in.txt","r",stdin);
	int t;
	cin>>t;
	int caseno=0;
	while(t--){
		caseno++;
		int lim;
		cin>>lim;
		char str[1024];
		cin>>str;
		ll people=str[0]-'0';
		ll sol=0;
		int l=strlen(str);
		for(int i=1;i<l;i++)
		{
			if(people<i && str[i]!='0'){
				sol=sol+i-people;
				people=i;
			}
			people=people+str[i]-'0';
			//cout<<people<<" "<<sol<<endl;
		}
		cout<<"Case #"<<caseno<<": "<<sol<<endl;
	}
    return(0);
}
