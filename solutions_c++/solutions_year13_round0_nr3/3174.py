#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cmath>
using namespace std;

int T;
long long a,b,ans;

bool fair(long long data){
	long long temp,back;
	temp=data;back=0;
	while (temp>0){
		back=back * 10 +(temp % 10);
		temp=temp / 10;
	}
	return (back==data)?true:false;
}

int main(){
	freopen("C-small-attempt0.in","r",stdin);freopen("std.out","w",stdout);
	cin>>T;
	for (int h=1;h<=T;h++){
		cin>>a>>b;ans=0;
		for (long long i = ceil(sqrt(a));i <= floor(sqrt(b));i++)
			if (fair(i) && fair(i*i)) ans++;
		cout<<"Case #"<<h<<": "<<ans<<endl;
	}
	return 0;
}
