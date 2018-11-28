#include <iostream>
#include <cmath>
#include <algorithm>
#include <iomanip>
using namespace std;

int main(){
	int t;cin>>t;
	for(int w=0;w<t;w++){
		double c, f, x;
		cin>>c>>f>>x;
		double number=2.0;
		double ans=0;
		while(1){
			double ans1, ans2;
			ans1=x/number;
			ans2=c/number+x/(number+f);
			if(ans1>ans2){
				ans+=c/number;
				number+=f;
			}
			else{
				ans+=ans1;
				break;
			}
		}
		cout<<"Case #"<< fixed <<setprecision(7)<<w+1<<": "<<ans<<endl;
	}
}
