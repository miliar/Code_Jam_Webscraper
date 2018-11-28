#include <iostream>
#include <cstdio>
#include <cstdlib>


using namespace std;

int main(){
freopen("in.txt","r",stdin);
freopen("out.txt","w",stdout);
int t;cin >>t;
int s[1001];


for(int a=0;a<t;a++){

for(int i=0;i<=1000;i++)s[i]=0;
int smax;cin >>smax;

for(int i=0;i<=smax;i++){
	char c;cin>>c;s[i]=c-'0';
}
int cnt=0,need=0;
for(int i=0;i<=smax;i++){	//cout<<s[i];
	cnt+=s[i];
	if(s[i]==0){
		if(cnt<=i){
			need++;cnt++;
		}
	}
	
}

cout<<"Case #"<< a+1<<": "<<need<<endl;

}
return 0;
}