#include <bits/stdc++.h>
using namespace std;

int t,n,j;
long long s;

bool p[10];

bool foo(long long x){
    if(x == 0){
	p[0] = true;
    } else{
	while(x){
	    p[x%10] = true;
	    x /= 10;
	}
    }
    for(int i=0;i<10;i++) if(!p[i]) return false;
    return true;
}

int main(){
    cin >> t;
    for(int ii=1;ii<=t;ii++){
	memset(p,0,sizeof(p));
	cin >> n;
	s = n;
	for(j=0;j<1000;j++,s+=n){
	    if(foo(s)) break;
	}
	if(j == 1000)
	    printf("Case #%d: INSOMNIA\n",ii);
	else
	    cout << "Case #"<<ii<<": "<< s << endl;
    }
    return 0;
}
