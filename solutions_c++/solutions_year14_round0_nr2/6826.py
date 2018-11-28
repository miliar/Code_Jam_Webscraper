# include <iostream>
# include <cstdio>
# include <vector>
using namespace std;

int main()
{
	int t;
	cin >> t;
	
	for (int i = 0; i < t; i++){
		double c,f,x;
		cin >> c >> f >> x;
		double prev = x/2.000;
		double tm = 2.000;
		double ans = 0.0;
		double prev_temp;
		double prev_tm;
		
		prev_temp = 0.00;
		prev_tm = 2.00;
		for (int k = 1; ; k++){
		//	cout << "for k " << k << endl;
			double temp;
		//	cout << prev_temp << " " << prev_tm << endl;
			tm = prev_tm;
			prev_tm = tm+f;
			temp = prev_temp + (c/tm);
		//	cout << temp <<" " << tm << endl;
			prev_temp = temp;
			tm = tm +f;
			temp = temp + (x/tm);
			if(temp > prev){
				ans = prev;
				break;
			}
		
		//	cout << " ans " << temp << endl;
			prev = temp;
		}
		cout << "Case #" << i+1<<": ";
		printf("%.7lf\n",ans);
		
		
		
	}
	return 0;
}
