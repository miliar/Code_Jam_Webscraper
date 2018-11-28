#include <bits/stdc++.h>
using namespace std;
string str;
int main()
{
	freopen("input.in","r",stdin);
	freopen("output.in","w",stdout);
	int t,s,p,i,ans,j;
	cin>>t;
	j = 1;
	while(t--){
		ans = 0;
		cin>>s;
		cin>>str;
		p = str[0] - '0';
		if((str[0] - '0') == 0){
			ans++;
			p = ans;	
		}
		
		for(i = 1; i < s + 1; i++){
			if((str[i] - '0') != 0){
				if(p >= i){
					p = p + str[i] - '0';
				}else{
					ans = ans + i - p;
					p = (p + ans + str[i] - '0');
				}
			}
		}
		//cout<<p<<endl;
		cout<<"Case  #"<<j++<<":"<<" "<<ans<<endl;
	}
	return 0;
}
