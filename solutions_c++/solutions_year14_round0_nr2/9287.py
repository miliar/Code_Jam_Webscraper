
#include <stdio.h>
#include <iostream>
#include <stdlib.h>
using namespace std;
int ProcessInput();

int main()
{

int testcases, i;

cin >> testcases;

//cout <<"Number of testcases:" << testcases << endl;
for(i=0; i < testcases; i++) {
	cout<<"Case #"<<i + 1<<": ";
	ProcessInput();
}

return 0;
}

double time_taken(double C, double F, double X, int n)
{
	int i;
	double total_time;
	
	total_time = 0;
	for(i = 0; i < n; i ++)
		total_time += C/(2 + i*F);

	total_time += X/(2+n*F);
	return total_time;
}
 
int ProcessInput()
{
double C, F, X;
double cur_time_taken, new_time_taken;
int i, done;
cin >> C;
//cout << "C is " << C << endl;
cin >> F;
//cout << "F is " << F << endl;
cin >> X;
//cout << "X is " << X << endl;

i = 0;
cur_time_taken = time_taken(C, F, X, i);

done = 0; 

while(!done)
{
	i++;
	new_time_taken = time_taken(C, F, X, i);
	if(new_time_taken > cur_time_taken) 
		done = 1;
	else
		cur_time_taken = new_time_taken;
}

//cout << cur_time_taken << endl;
printf("%0.7f\n", cur_time_taken);

return 0;

}

