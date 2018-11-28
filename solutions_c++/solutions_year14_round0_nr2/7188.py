#include<iostream>
#include<cstdio>
#include<iomanip>
using namespace std;

int main() {
	//freopen("B-large.in", "r", stdin);
    //freopen("output.txt", "w", stdout);
  
    int t,r=1;
    double ini,c,f,x,ans1,ans2;
    
	
	cin>>t;
    while(t--) {
		ini=2.0;
		ans1=ans2=0.0;
			cout<<setprecision(12);
		cin>>c>>f>>x;
			//purchase no farm
			ans1=x/ini;
		//purchase 1 farm	
	    ans2+=c/ini;
		ini+=f;
		ans2+=x/ini;
		//purchase 1 more farm and compare
		while(ans2<ans1) {
		ans1=ans2;
		ans2-=x/ini;
		ans2+=c/ini;
		ini+=f;
		ans2+=x/ini;
		
	
		
	}
		
   cout<<"Case #"<<r<<": ";
   printf("%f\n",ans1);
   r++;
		
    }
    
    
}
