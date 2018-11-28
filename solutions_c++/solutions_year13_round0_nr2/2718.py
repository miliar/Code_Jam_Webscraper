#include <string>
#include <fstream>

#define N 10
#define M 10
#define S 2

int begin [N][N];
int end [N][N];
int n, m;

void update_row()
{
	for (int row=0; row<n; row++) {
		if (end[row][0] == 1) {
			bool need = true;
			for (int col=0; col<m; col++) {
				if (end[row][col] > 1)
				{
					need = false;
					break;
				}
			}
			if (need == true) {
				for (int col=0; col<m; col++) {
					begin[row][col] = 1;
				}
			}
		}
	}
}
void update_col()
{
	for (int col=0; col<m; col++) {
		if (end[0][col] == 1) {
			bool need = true;
			for (int row=0; row<n; row++) {
				if (end[row][col] > 1)
				{
					need = false;
					break;
				}
			}
			if (need == true) {
				for (int row=0; row<n; row++) {
					begin[row][col] = 1;
				}
			}
		}
	}
}
int main()
{
	std::ofstream out;
	std::ifstream in;
	in.open("a.in");
	out.open("a.out");
	int Case;
	in >> Case;
	for (int t=1; t<=Case; t++)
	{
		in >> n >> m;
		for (int i=0; i<n; i++) {
			for (int j=0; j<m; j++) {
				in >> end[i][j];
			}
		}
		for (int i=0; i<n; i++) {
			for (int j=0; j<m; j++) {
				begin[i][j] = S;
			}
		}
		update_row();
		update_col();
		bool match = true;
		for (int i=0; i<n; i++)
		{
			for (int j=0; j<m; j++)
			{
				if (begin[i][j] != end[i][j]) {
					match = false;
					break;
				}
			}
		}
		if (match)
		{
			out << "Case #" << t<< ": YES" << std::endl;
		}
		else
		{
			out << "Case #" << t<< ": NO" << std::endl;
		}
	}
	return 0;
}