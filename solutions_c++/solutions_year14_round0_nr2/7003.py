#include<iostream>
using namespace std;

void process(int t)
{
	double c,f,x;
	cin>>c>>f>>x;

	double new_f = 2, final_time = 0.0000000, delta_time;
	double prev_time, next_time;

	while(1)
	{
		prev_time = x/new_f;
		delta_time = c/new_f;
		new_f += f;
		next_time = x/new_f;

		if(delta_time + next_time > prev_time)
		{
			//time to stop, we found answer
			final_time += prev_time;
			break;
		}
		final_time += delta_time;
	}

	cout.precision(7);
	cout<<std::fixed;
	cout<<"Case #"<<t<<": "<<final_time<<endl;
}

int main()
{
	int num_test = 0, t = 0;

	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	//redirect cin to file
	cin >> num_test;
	
	while(t < num_test)
	{
		process(++t);
	}
}