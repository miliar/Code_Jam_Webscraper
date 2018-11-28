#include <iostream>
#include<string.h>
#include<stdio.h>
using namespace std;
#define gc getchar

int main() {
	int t,s,b[1001],ch,i,ans;
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	cin>>t;
	for(int n=1;n<=t;n++){
		ans = 0;
		cin>>s;
		ch = gc();
		//cout<<"ch 1 = "<<ch<<endl;
		ch = gc();
		//cout<<"ch 2 = "<<ch<<endl;
		i=0;
		b[i] = ch - 48;
		while(1){
			ch = gc();
			i++;
			if(ch == '\n')
				break;
			b[i] = b[i-1] + ch - 48;
			// cout<<"b[i]"<<b[i]<<endl;
			if(ch >= '1'){
				if(b[i-1] >= i)
					continue;
				else{
					ans += i - b[i-1];
					b[i] = i + ch - 48;
					// cout<<"ans = "<<ans<<endl;
				}
			}
		}
		cout<<"Case #"<<n<<": "<<ans<<endl;
		memset(b,0,1001);
	}
	return 0;
}
