#include <sstream>
#include <string>
#include <cstdio>
using namespace std;

void readCase(int grid[3]) {

	char work[20];
	int rLine;

}

double check(double grid[3])
{

	double f = 2.0;
	double n0time = 0.0;
	double n1time;
	double n2time;

	while ( 1 ) {
		n1time = (grid[2] / f) + n0time;
		n0time += grid[0] / f;
		n2time = (grid[2] / (f + grid[1])) + n0time;

//		printf("n1[%lf] n2[%lf] n0[%lf]\n", n1time, n2time, n0time);
		if (n1time < n2time) 
			break;
		f += grid[1];
	}
	return n1time;
}


void body(int counter) {

	double grid[3];
	string	str[3];
	printf("Case #%d: ", counter);

	scanf("%lf %lf %lf", &grid[0], &grid[1], &grid[2]); 
	printf("%0.7lf\n", check(grid));
	return;
}

int main() {
	int counter = 0;
	int loop; 
	scanf("%d",&loop);
	while(loop--) {
		body(++counter);
	}
	return 0;
}
