#include<iostream>
#include<cstring>
#include<fstream>
using namespace std;
int T;
#define rep(i,j,k) for(int i=j;i<=k;i++)
#define mem(a) memset(a,0,sizeof(a))
typedef long long ll;
bool a[10];
void ans(int n){
	mem(a);
	if(n==0){
		cout<<"INSOMNIA"<<endl;
	} else {
		int i=0,sum=0;
		while(sum!=10){
			i++;
			ll num=i*n;
			while(num){
				if(a[num%10]==0){
					a[num%10]=1;
					sum++;
				}
				num/=10;
			}
		}
		cout<<i*n<<endl;
	}
}
int main(){
	//freopen("A-large.in","r",stdin);
	//freopen("out","w",stdout);
	cin>>T;
	rep(i,1,T){
		int num;
		cin>>num;
		cout<<"Case #"<<i<<": ";
		ans(num);
	}
}
