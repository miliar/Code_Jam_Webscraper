#include <cstdio>
#include <string>
#include <vector>
using namespace::std;


int main() 
{
	FILE* file_in = fopen("A-large.in","r");
	FILE* file_out = fopen("A-large.out","w");
	int n_case;
	fscanf(file_in,"%d",&n_case);
	for (int i_case = 0; i_case < n_case; ++i_case) {
		int s_max;
		fscanf(file_in,"%d",&s_max);
		char buf[1024];
		fscanf(file_in,"%s",buf);
		vector<int> audience(s_max+1);
		for (int i = 0; i < s_max + 1; ++i) {
			audience[i] = buf[i] - '0';
		}
		
		int friend_num = 0;
		int current_audience = 0;
		for (int i = 0; i < audience.size(); ++i) {
			if (current_audience >= i) {
				current_audience += audience[i];
			}else{
				friend_num += i - current_audience;
				current_audience += audience[i] + (i - current_audience);
			}
			//printf("i %d c %d fr %d\n" , i , current_audience, friend_num);
		}
		fprintf(file_out,"Case #%d: %d\n", i_case + 1, friend_num);
	}


	
	fclose(file_out);
	fclose(file_in);

	system("pause");
	return 0;
}