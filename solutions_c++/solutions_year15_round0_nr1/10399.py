#include<bits/stdc++.h>
using namespace std;
#define f_in(st) freopen(st,"r",stdin);
#define f_out(st) freopen(st,"w",stdout);

int main(){
	f_in("in.txt");
	f_out("out.txt");
	int t;
	cin>>t;
	for(int x = 1 ; x <= t ; x++){
		int n;
		cin>>n;
		char str[1006];
		cin>>str;
		int s = 0 , r = 0;
		for(int i=0;str[i]!='\0';i++){
			if(str[i] == '0')
				continue;
			if(s >= i){
				s += (str[i]-'0');
			}else{
				r = (i - s);
				s += r + (str[i]-'0');
			}
		}
		
		cout<<"Case #"<<x<<": "<<r<<endl;
	}
	return 0;
}

