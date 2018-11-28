#include <bits/stdc++.h>

using namespace std;

int main(){
	int T;
	cin>>T;
	for(int k=1; k<=T; k++){
		double C, F, X;
		int z;
		cin>>C>>F>>X;
		double rate=2, n_rate;
		double act_seconds=0, n_seconds=0;
		int iterations=0;
		//cout<<C<<" "<<F<<" "<<X<<endl;
		while(true){
			double next_farm=C/rate;
			//printf("Next farm: %.7lf\n", next_farm);
			double time_goal=(X/rate)+act_seconds;

			//Next step
			n_seconds = act_seconds + next_farm;
			n_rate=rate+F;
			double n_time_goal=(X/n_rate)+n_seconds;

			if(n_time_goal<time_goal){
				time_goal=n_time_goal;
				rate=n_rate;
				act_seconds=n_seconds;
			}
			else{
				act_seconds+=X/rate;
				break;
			}
			//printf("State %d:\n\n",iterations);
			//printf("Rate: %.7lf\n", rate);
			//printf("Time to win: %.7lf\n", time_goal);
			//printf("Seconds of game: %.7lf\n", act_seconds);
			iterations++;
		}
		printf("Case #%d: %.7lf\n", k, act_seconds);

	}
}