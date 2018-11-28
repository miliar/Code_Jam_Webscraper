#include<cstdio>
#include<cstring>
#include<string>
#include<iostream>
#include<cstdlib>
#include<vector>
using namespace std;

#define MAX 1E4

vector<bool> flag;

void fs()
{
	int num,p,q;
	char s[100],c[100];
	flag.resize(MAX+1);
	for(int i=1;i<=1E2;i++){
		itoa(i,c,10);
		p=0;
		q=strlen(c)-1;
		while(p<q){
			if(c[p]!=c[q]) break;
			p++;
			q--;
		}
		if(p>=q){
			num=i*i;
			itoa(num,s,10);
			p=0;
			q=strlen(s)-1;
			while(p<q){
				if(s[p]!=s[q]) break;
				p++;
				q--;
			}
			if(p>=q) flag[num]=true;
		}
	}
	return;
}

int main()
{
	freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small.out","w",stdout);
	fs();
	int T,a,b,sum;
	cin>>T;
	for(int cas=0;cas<T;cas++){
		sum=0;
		cin>>a>>b;
		for(int i=a;i<=b;i++){
			if(flag[i]) sum++;
		}
		cout<<"Case #"<<cas+1<<": "<<sum<<endl;
	}
	return 0;
}
			