#include<iostream>
#include<set>
using namespace std;

int main()
{
	int T;
	cin >> T;
	for (int t = 0; t < T; t++){
		double ans = 10000000;//INF
		double C, F, X;
		cin >> C >> F >> X;
		double total_time=0.0;
		double speed = 2.0;
		while (true){
			double time_to_goal = X / speed;
			if (ans > total_time + time_to_goal) ans = total_time + time_to_goal;
			else break;
			total_time += C / speed;
			speed += F;
		}
		cout << "Case #" << t + 1 << ": ";
		printf("%lf\n", ans);
//		cout << ans << endl;
	}
}