#include <iostream>
using namespace std;

typedef	unsigned int	uint;
#define	PRINT_RESULT(x,y)	cout << "Case #" << x << ": " << y << endl;

int main(int argc, char* argv[])
{
	/*The first line of the input gives the number of test cases, T.
	 * T test cases follow.
	 * Each consists of one line with Smax, the maximum shyness level of the shyest person in the audience,
	 * followed by a string of Smax + 1 single digits.
	 */

	/* Read the number of TCs */
	int i, j = 0;
	uint n_tc_count = 0;
	cin >> n_tc_count;

	if (n_tc_count == 0)
		exit(1);

	for (i = 0; i < n_tc_count; i++) {
		int	n_smax = 0;
		uint	*p_audience_shyness_level = NULL;
		uint	audience = 0;
		int	total_count = -1;
		uint	local_req = 0;
		uint	total_req = 0;
		
		cin >> n_smax;
		cin >> audience;

		p_audience_shyness_level = (uint *)malloc(sizeof(uint) * (n_smax + 1));
		if (!p_audience_shyness_level) {
			return 1;
		}
		memset(p_audience_shyness_level, 0, (sizeof(uint) * (n_smax + 1)));

		/* Get the audience count for each shyness level */

		for (j = n_smax; j >= 0; j--) {
			p_audience_shyness_level[j] = audience % 10;
			audience /= 10;
		}

		for (j = 0; j <= n_smax; j++) {
			total_count += p_audience_shyness_level[j];
			if (total_count < j) {
				local_req = j - total_count;
				total_count += local_req;
				total_req += local_req;
			}
		}

		PRINT_RESULT(i+1, total_req);
		if (p_audience_shyness_level) {
			free(p_audience_shyness_level);
			p_audience_shyness_level = NULL;
		}
	}

	return 0;
}