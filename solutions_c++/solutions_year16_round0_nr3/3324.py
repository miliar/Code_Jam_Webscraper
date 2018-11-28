//Harhit bansal
#include<iostream>
#include<string>

#include<cmath>
using namespace std;

#define lli long long int
int count=0;



lli myfunc(lli n){
    for(lli i=2;i*i<=n;i++){
        if(n%i==0)
            return i;
    }
    return 0;
}
lli cool(string s,int base){
    int n=s.length();
    lli ans=0;
    for(lli i=0;i<n;i++){
        ans=ans+(s[i]-48)*pow(base,n-i-1);
    }
    return ans;
}void go(string s,int n,int j,int flag1);
int main() {
	
	int t,test=1;
	cin>>t;
	while(t--){
		lli n,j;
		cin>>n>>j;
		cout<<"Case #"<<test<<":\n";
		go("",n,j,0);
		test++;
	}
	return 0;
}
void go(string s,int n,int j,int flag1){
    if(count<j){
    if(flag1==0){
        go("1",n,j,1);
    }
    if(flag1==n-1){
        go(s+"1",n,j,flag1+1);
    }
    if(flag1>0&&flag1<n-1){
    go(s+"1",n,j,flag1+1);
    go(s+"0",n,j,flag1+1);
    }
    if(flag1==n){
        if(myfunc(cool(s,2))&&myfunc(cool(s,3))&&myfunc(cool(s,4))&&myfunc(cool(s,5))&&myfunc(cool(s,6))&&myfunc(cool(s,7))&&myfunc(cool(s,8))&&myfunc(cool(s,9))&&myfunc(cool(s,10))){
            //cout<<s<<" "<<cool(s,2)<<" "<<cool(s,3)<<" "<<cool(s,4)<<" "<<cool(s,5)<<" "<<cool(s,6)<<" "<<cool(s,7)<<" "<<cool(s,8)<<" "<<cool(s,9)<<" "<<cool(s,10)<<"\n";
            cout<<s<<" "<<myfunc(cool(s,2))<<" "<<myfunc(cool(s,3))<<" "<<myfunc(cool(s,4))<<" "<<myfunc(cool(s,5))<<" "<<myfunc(cool(s,6))<<" "<<myfunc(cool(s,7))<<" "<<myfunc(cool(s,8))<<" "<<myfunc(cool(s,9))<<" "<<myfunc(cool(s,10))<<"\n";
            count++;
        }
    }
    }
}