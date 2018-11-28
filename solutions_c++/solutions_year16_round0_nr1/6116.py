#include <bits/stdc++.h>
#define rep(i,a,n) for(int i=a;i<n;i++)
#define repb(i,a,b) for(int i=a;i>=b;i--)
#define all(a) a.begin(),a.end()
using namespace std;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> pii;

int main(){
	ifstream fin("in.txt");
	ofstream fout("out1.txt");
	
	int t,n;
	cin>>t;

	rep(x,0,t){
		cin>>n;
		int d[10]={},cnt=0,ans=-1;
		rep(i,1,100){
			int now=i*n;
			while(now){
				int tmp=now%10;
				if(!d[tmp]){
					d[tmp]=1;
					cnt++;
					if(cnt==10){
						ans=i*n;
						i=100;
						break;
					}
				}
				now/=10;
			}
		}
		fout<<"Case #"<<x+1<<": ";
		if(ans==-1) fout<<"INSOMNIA";
		else fout<<ans;
		fout<<endl;
	}
}