#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <fstream>

int main(int argc, char **argv)
{
	char c[1003];
	fscanf(stdin, "%s", &c);
	int T = atoi(c);

	int shyness[10];
	int s_max = 0;
	for (int i = 0; i < T; i++) {
		fscanf(stdin, "%s", &c);
		s_max = atoi(c);
		memset(shyness, 0, sizeof(shyness));
		fscanf(stdin, "%s", &c);
		for (int j = 0; j <= s_max; j++)
			shyness[j] = c[j] - '0';
		int friends = 0;
		int standing = 0;
		for (int j = 0; j <= s_max; j++) {
			if (standing < j && shyness[j]) {
				int new_friends = j - standing;
				friends += new_friends;
				standing += new_friends;
			}
			standing += shyness[j];
			//printf("j: %d\tstanding: %d\tfriends: %d\n", j, standing, friends);
		}

		fprintf(stdout, "Case #%d: %d\n", (i+1), friends);
	}
}
