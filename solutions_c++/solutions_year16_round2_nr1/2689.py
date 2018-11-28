#pragma warning(disable:4996) 

#include <cstdio>
#include <deque>
#include <algorithm>
#include <vector>

using namespace std;

const int length = 1001;

int main(void) {
	FILE * fp;
	fp = fopen("A.txt", "w");
	
	int in;
	scanf("%d", &in);
	for (int h = 0; h < in; h++) {
		char str[2001];
		scanf("%s", str);
		vector<int> arr;
		int k = 0;
		for (int i = 0; i <= strlen(str); i++) {
			if (str[i] == 'Z') {
				str[i] = 'x';
				for (int j = 0; j <= strlen(str); j++) {
					if (str[j] == 'E') {
						str[j] = 'x';
						break;
					}
				}
				for (int j = 0; j <= strlen(str); j++) {
					if (str[j] == 'R') {
						str[j] = 'x';
						break;
					}
				}
				for (int j = 0; j <= strlen(str); j++) {
					if (str[j] == 'O') {
						str[j] = 'x';
						break;
					}
				}
				arr.push_back(0);
			}

			if (str[i] == 'X') {
				str[i] = 'x';
				for (int j = 0; j <= strlen(str); j++) {
					if (str[j] == 'S') {
						str[j] = 'x';
						break;
					}
				}
				for (int j = 0; j <= strlen(str); j++) {
					if (str[j] == 'I') {
						str[j] = 'x';
						break;
					}
				}
				arr.push_back(6);
			}

			if (str[i] == 'U') {
				str[i] = 'x';
				for (int j = 0; j <= strlen(str); j++) {
					if (str[j] == 'F') {
						str[j] = 'x';
						break;
					}
				}
				for (int j = 0; j <= strlen(str); j++) {
					if (str[j] == 'R') {
						str[j] = 'x';
						break;
					}
				}
				for (int j = 0; j <= strlen(str); j++) {
					if (str[j] == 'O') {
						str[j] = 'x';
						break;
					}
				}
				arr.push_back(4);
			}
		}

		for (int i = 0; i <= strlen(str); i++) {
			if (str[i] == 'G') {
				str[i] = 'x';
				for (int j = 0; j <= strlen(str); j++) {
					if (str[j] == 'E') {
						str[j] = 'x';
						break;
					}
				}
				for (int j = 0; j <= strlen(str); j++) {
					if (str[j] == 'I') {
						str[j] = 'x';
						break;
					}
				}
				for (int j = 0; j <= strlen(str); j++) {
					if (str[j] == 'H') {
						str[j] = 'x';
						break;
					}
				}
				for (int j = 0; j <= strlen(str); j++) {
					if (str[j] == 'T') {
						str[j] = 'x';
						break;
					}
				}

				arr.push_back(8);
			}
		}

		for (int i = 0; i <= strlen(str); i++) {
			if (str[i] == 'H') {
				str[i] = 'x';
				for (int j = 0; j <= strlen(str); j++) {
					if (str[j] == 'T') {
						str[j] = 'x';
						break;
					}
				}
				for (int j = 0; j <= strlen(str); j++) {
					if (str[j] == 'R') {
						str[j] = 'x';
						break;
					}
				}
				for (int j = 0; j <= strlen(str); j++) {
					if (str[j] == 'E') {
						str[j] = 'x';
						break;
					}
				}
				for (int j = 0; j <= strlen(str); j++) {
					if (str[j] == 'E') {
						str[j] = 'x';
						break;
					}
				}

				arr.push_back(3);
			}
		}

		for (int i = 0; i <= strlen(str); i++) {
			if (str[i] == 'F') {
				str[i] = 'x';
				for (int j = 0; j <= strlen(str); j++) {
					if (str[j] == 'I') {
						str[j] = 'x';
						break;
					}
				}
				for (int j = 0; j <= strlen(str); j++) {
					if (str[j] == 'V') {
						str[j] = 'x';
						break;
					}
				}
				for (int j = 0; j <= strlen(str); j++) {
					if (str[j] == 'E') {
						str[j] = 'x';
						break;
					}
				}

				arr.push_back(5);
			}
		}

		for (int i = 0; i <= strlen(str); i++) {
			if (str[i] == 'S') {
				str[i] = 'x';
				for (int j = 0; j <= strlen(str); j++) {
					if (str[j] == 'E') {
						str[j] = 'x';
						break;
					}
				}
				for (int j = 0; j <= strlen(str); j++) {
					if (str[j] == 'V') {
						str[j] = 'x';
						break;
					}
				}
				for (int j = 0; j <= strlen(str); j++) {
					if (str[j] == 'E') {
						str[j] = 'x';
						break;
					}
				}
				for (int j = 0; j <= strlen(str); j++) {
					if (str[j] == 'N') {
						str[j] = 'x';
						break;
					}
				}

				arr.push_back(7);
			}
		}

		for (int i = 0; i <= strlen(str); i++) {
			if (str[i] == 'I') {
				str[i] = 'x';
				for (int j = 0; j <= strlen(str); j++) {
					if (str[j] == 'N') {
						str[j] = 'x';
						break;
					}
				}
				for (int j = 0; j <= strlen(str); j++) {
					if (str[j] == 'N') {
						str[j] = 'x';
						break;
					}
				}
				for (int j = 0; j <= strlen(str); j++) {
					if (str[j] == 'E') {
						str[j] = 'x';
						break;
					}
				}
				arr.push_back(9);
			}

		}

		for (int i = 0; i <= strlen(str); i++) {
			if (str[i] == 'N') {
				str[i] = 'x';

				arr.push_back(1);
			}
		}
		for (int i = 0; i <= strlen(str); i++) {
			if (str[i] == 'T') {
				str[i] = 'x';

				arr.push_back(2);
			}
		}




		std::sort(arr.begin(), arr.end());
		fprintf(fp, "Case #%d: ", h + 1);
		for (int i = 0; i < arr.size(); i++) {
			fprintf(fp, "%d", arr[i]);
		}
		fprintf(fp, "\n");

	}
	return 0;
}