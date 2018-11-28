#include <bits/stdc++.h>

using namespace std;

#define MOD 1000000007
#define llu long long unsigned
#define lld long long
#define ld long

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt","w",stdout);
	string str;
	lld test,n,i,j,k,a,b,c,t;
	cin>>test;
	for(t=1;t<=test;t++){
        cin>>str;
        n=0;
        for(i=1;i<str.length();i++){
            if(str[i]!=str[i-1])
                n++;
        }
        if(str[str.length()-1]=='-')
            n++;
        cout<<"Case #"<<t<<": "<<n<<endl;
	}
    return 0;
}
