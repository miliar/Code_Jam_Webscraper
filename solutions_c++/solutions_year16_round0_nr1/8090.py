#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
int main() {
	int t;
	//scanf("%d",&t);
	int X=1;
	ifstream f1;
    ofstream f2;
    f1.open("A-Large.in");
    f2.open("output.out");
	f1>>t;
	while(t--)
	{
		ll smax;int a[10]={0};
		//string s;
		//scanf("%d",&smax);
		f1>>smax;ll i=0,ans;
		bool b=true;
		if(smax==0) {f2<<"Case #"<<X<<": "<<"INSOMNIA"<<endl;}
		else{
		while(b)
        {
            i++;
            ll x=i*smax;
            ans=x;
            while(x)
            {
                a[x%10]=1;
                x/=10;
            }
            int j=0;
            for(;j<10;j++) if(a[j]==0) break;
            if(j==10) b=false;
        }
        f2<<"Case #"<<X<<": "<<ans<<endl;
        //X++;
		}
		X++;

		//x++;
	}
	f1.close();
    f2.close();
	return 0;
}
