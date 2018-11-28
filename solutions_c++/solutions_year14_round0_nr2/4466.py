#include<iostream>
#include<stdio.h>
using namespace std;
int main(){
	
	double c,f,x,pc,pr,tt,y=1;//farm_cost,farm_rate,cookie_goal,present_cookie,present rate,total time
	int t;//test cases
	freopen( "input.txt", "r", stdin );
	freopen( "output.txt", "w", stdout );
	cin>>t;
	while(t--){
		pc=0;
		pr=2;
		tt=0;
		cin>>c>>f>>x;
		while(1){
			if (x/(pr)>(c/pr+x/(pr+f))){
				tt+=c/pr;
				pr=pr+f;
			//	printf("%.7f   %.7f \n",tt,c/pr);
			}else{
				tt+=x/pr;
			//	printf("* %.7f   %.7f *\n",tt,x/pr);
				break;
			}
		}
		
			cout<<"Case #"<<y++<<": ";
			printf("%.7f",tt);
			cout<<endl;
			
		
		
	}
	
	return 0;

} 
