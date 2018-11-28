#include<iostream>
using namespace std;

int main(){
long T,cnt=1,r,t;

cin>>T;
while(T--){
cin>>r>>t;
int res=0;
long long i=r+1,j=r;
while(1){
	long long tmp=i*i - j*j;
        //cout<<i<<" i j "<<j<<" tmp "<<tmp<<" t "<<t<<endl;
	if(tmp <= t)res++;
	else
		break;

	t -= tmp;
	i += 2;
	j += 2;
}

cout<<"Case #"<<cnt++<<": "<<res<<endl;
}


return 0;
}
