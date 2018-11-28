#include <bits/stdc++.h>
using namespace std;

#define pb push_back
#define inf 2248012
#define mp make_pair
#define sci(x) scanf("%d",&x)
#define scii(x,y) scanf("%d %d",&x,&y)
#define sciii(x,y,z) scanf("%d %d %d",&x,&y,&z)

typedef long long ll;

int main(){
	int af;
	cin>>af;
	for(int y=0; y<af; y++){
		int m[10]={0,0,0,0,0,0,0,0,0,0};
		string p;
		cin>>p;
		char r[2000001],r2[2000001];
		memset(r2,'0',sizeof(r));
		int t=p.size();
		int pot=0;
		for(int i=0;i<t; i++){
			int num=p[i]-'0';
			if(!m[num]){m[num]=1; pot++;}
		}
		for(int i=t-1,j=0;i>=0; i--){
			r[j]=p[i];
			r2[j]=p[i];
			j++;
		}
		if(t==1 && p[0]=='0') cout<<"Case #"<<y+1<<": INSOMNIA"<<endl;
		else{
			while(pot<10){
				int suma,res=0;
				//cout<<"sig "<<endl;
				for(int i=0; i<t; i++){
					int n1=r[i]-'0',n2=r2[i]-'0';
					//cout<<n1<<" "<<n2<<endl;
					suma=(n1+n2+res)%10; res=(n1+n2+res-suma)/10;
					//cout<<suma<<" res "<<res<<endl;
					if(!m[suma]){m[suma]=1; pot++;}
					char as=suma+'0';
					//cout<<"SUMA VALE "<<as<<endl;
					r[i]=as;
				}
				if(res){
					char as=res+'0';
					r[t]=as;
					if(!m[res]){m[res]=1; pot++;}
					t++;
				}
			}
			cout<<"Case #"<<y+1<<": ";
			for(int i=t-1; i>=0; i--){cout<<r[i];}
			cout<<endl;
		}
	}
}