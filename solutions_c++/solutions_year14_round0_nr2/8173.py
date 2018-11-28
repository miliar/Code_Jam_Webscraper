#include <iostream>
using namespace std;
int main(){
	int t;

	cin >> t;
	int l=0;
	while(t--){
		l++;
		cout << "Case #" <<l<< ": "; 

		double c,f,x;
		cin >> c >> f >> x;

		double ans = 0,cur,forw;
		int n =0;
		while(1){
			cur = x/(2 + n*f);
			forw = c/(2 + n*f) + x/(2 + (n + 1)*f);

			if(cur < forw){
				ans +=cur;
				break;
			}
			else{
				ans += c/(2 + n*f);
				n++;
			}
		}

		printf("%.7lf\n", ans);

		/*n = (f*x - c*( 2 + f))/( f*c );

		printf("n %d\n",n);
		double ans = 0;
		for(int i =0 ; i<=n; i++){
			ans += ( 1/(2 + i*f));  
		}

		ans = ans* c;
		printf("ans %lf\n",ans);

		if(n >= 0)
			ans = ans + x/(2 + (n+1)*f);
		else
			ans = ans + x/2;
				printf("%.7lf\n", ans);*/

	}
}