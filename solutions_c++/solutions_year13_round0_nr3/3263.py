/*
#include<iostream>
#include<cstdio>
#include<string>
#include<sstream>
#include<cmath>
using namespace std;
long long parad[100000];
long long pos=0;
bool is_parad(long long num)
{
	stringstream ss;
	ss<<num;
	string s=ss.str();
	for(long long i=0;i<(int)s.length()/2;i++){
		if(s[i]!=s[(long long)s.length()-i-1])
			return false;
	}
	return true;
}
long long find_pos(long long x,int wh)
{
	long long temp=(long long)sqrt((double)x);
	long long l=0,h=pos-1;
	while(l<h-1){
		long long mid=(l+h)/2;
		if(parad[mid]>temp){
			h=mid;
		}
		else if(parad[mid]<temp){
			l=mid;
		}
		else
			return mid;
	}
	if(wh==1){
		if(parad[l]<temp)
			return h;
		else
			return l;
	}
	else{
		if(parad[h]>temp)
			return l;
		else
			return h;
	}
}
int main()
{
	FILE *fp,*fp_;
	freopen_s(&fp,"data.in","r",stdin);
	freopen_s(&fp_,"data.out","w",stdout);
	for(long long i=1;i<=1000000;i++){
		if(is_parad(i)){
			parad[pos++]=i;
		}
	}
	int T;
	long long a,b;
	cin>>T;
	for(int k=0;k<T;k++){
		cin>>a>>b;
		int ans=0;
		long long pos_a=find_pos(a,1);
		long long pos_b=find_pos(b,2);
		for(long long cnt=pos_a;cnt<=pos_b;cnt++){
			if(is_parad(parad[cnt]*parad[cnt]))
				ans++;
		}
		cout<<ans<<endl;
	}
	fcloseall();
	return 0;
}*/

#include<iostream>
#include<cstdio>
#include<string>
#include<sstream>
#include<cmath>
using namespace std;
bool is_parad(long long num)
{
	stringstream ss;
	ss<<num;
	string s=ss.str();
	for(long long i=0;i<(int)s.length()/2;i++){
		if(s[i]!=s[(long long)s.length()-i-1])
			return false;
	}
	return true;
}
bool is_square(long long num)
{
	long long temp=(long long)sqrt((double)num);
	if(temp*temp==num)
		return true;
	return false;
}
int main()
{
	FILE *fp,*fp_;
	freopen_s(&fp,"data.in","r",stdin);
	freopen_s(&fp_,"data.out","w",stdout);
	int T;
	long long a,b;
	cin>>T;
	for(int k=0;k<T;k++){
		cin>>a>>b;
		int ans=0;
		for(long long cnt=a;cnt<=b;cnt++){
			if(is_square(cnt)){
				long long temp=(long long)sqrt((double)cnt);
				if(is_parad(cnt)){
					if(is_parad(temp))
						ans++;
				}
			}
		}
		cout<<"Case #"<<k+1<<": "<<ans<<endl;
	}
	fcloseall();
	return 0;
}