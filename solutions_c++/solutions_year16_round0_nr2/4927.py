#include <bits/stdc++.h>

using namespace std;
int main(){
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
	int T,N=0,flag=0;
	string str;
	cin>>T;
	for(int I=1;I<=T;I++,N=flag=0){
        cin>>str;
        for(flag=0 ; flag < str.length()-1 ; flag++)
            if(str[flag] != str[flag+1])N++;
        if(str[str.length()-1] == '-')N++;
        cout<<"Case #"<<I<<": "<<N<<endl;
	}
}
