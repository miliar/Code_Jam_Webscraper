#include <fstream>
#include<math.h>
using namespace std;

ifstream fin("input.txt");
ofstream fout("output.txt");
int T, D,IND, max_el = -1;
int non_empty_plate[1001];

void solve ()
{
	int time_count = 0;
	int min_time_count = 1000;
	for(int i = 1; i <= max_el; i++) {
		
		time_count = i;
		for(int j = 1; j <= D; j++) {
			int rmndr = max(non_empty_plate[j] - i, 0);
			time_count +=  rmndr / i + (rmndr % i == 0? 0 : 1) ;
		}
		if(time_count < min_time_count)
			min_time_count = time_count;
	}
	fout<<"Case #"<<IND<<": "<<min_time_count<<"\n";
	min_time_count = 1000;

}
int main()
{
	fin>>T;

	for( IND = 1; IND <= T; IND++) {
		fin>>D;
		for(int j = 1; j <= D; j++) {
			fin>>non_empty_plate[j];
			if(non_empty_plate[j] > max_el)
				max_el = non_empty_plate[j];
		}
		solve();
		max_el = -1;

	}
	return 0;
}