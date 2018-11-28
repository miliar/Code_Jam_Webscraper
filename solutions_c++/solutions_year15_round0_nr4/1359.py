#include <cstdio>
#include <iostream>
using namespace std;
int T,x,r,c;

int main(){
	freopen("D-small-attempt2.in","r",stdin);
	freopen("D-small.out","w",stdout);
	scanf("%d",&T);
	int ca=1;
	string yes="GABRIEL",no="RICHARD";
	string ans;
	while(T--){
	    scanf("%d%d%d",&x,&r,&c);
	    if(x==1){
			ans=yes;
	    }
	    else if(x==2){
			if(r*c%x==0) ans=yes;
			else ans=no;
	    }
	    else if(x==3){
			if(r*c%x==0&&r*c>3) ans=yes;
			else ans=no;
	    }
	    else {
	    	if(r*c>=12) ans=yes;
	    	else ans=no;
	    }
        printf("Case #%d: %s\n",ca++,ans.c_str());
	}
}
