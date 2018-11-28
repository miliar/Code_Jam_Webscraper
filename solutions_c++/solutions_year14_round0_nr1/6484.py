#include <fstream>

int main() {
	std::ifstream fin("mt.in");
	std::ofstream fou("mt.out");
	int n;
	int arr[4];
	int ans;
	int temp;
	int flag;
	int num;
	fin >> n;
	for (int i = 1; i <= n; i++) {
		flag = 0;
		fin >> ans;
		for (int j = 0; j < (ans - 1) * 4; j++)
			fin >> temp;
		for (int j = 0; j < 4; j++) {
			fin >> arr[j];
		}
		for (int j = 0; j < (4 - ans) * 4; j++)
			fin >> temp;
		fin >> ans;
		for (int j = 0; j < (ans - 1) * 4; j++)
			fin >> temp;
		for (int j = 0; j < 4; j++) {
			fin >> temp;
			for (int k = 0; k < 4; k++) {
				if (temp == arr[k]) {
					flag++;
					num = temp;
				}
			}
		}
		for (int j = 0; j < (4 - ans) * 4; j++)
			fin >> temp;
		
		fou << "case #" << i << ": ";
		if (flag == 0)
			fou << "Volunteer cheated!";
		else if (flag == 1)
			fou << num;
		else
			fou << "Bad magician!";

		fou << std::endl;
	}
	return 0;
}