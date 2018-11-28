#include <iostream>
#include <stdio.h>
#include <string.h>

using namespace std;

int count_group(const char* str) {
    if (strlen(str) > 0) {
		int g = 1;
		int i = 0;
		char prev = str[0], curr;	
		while (str[i] != '\0') {
            curr = str[i++];
			if (curr != prev) {
				g++;
				prev = curr;
			}
		}
        return g;
	}
	else
		return 0;
}

int main(int argc, char *args[]) {
	if (argc == 2 && strcmp(args[1], "small") == 0) {
		freopen("small.in", "r", stdin);
		freopen("small.out", "w", stdout);
	}
	else if (argc == 2 && strcmp(args[1], "large") == 0) {
		freopen("large.in", "r", stdin);
		freopen("large.out", "w", stdout);
	}
	else {
		cout << "\nPlease enter \"small\" or \"large\" test file.";
		return 0;
	}

	int T;
	cin >> T;
	for (int i=0; i<T; i++) {
		string tmp;
        cin >> tmp;
    	const char* s = tmp.c_str();
		bool lastminus = (s[strlen(s)-1] == '-' ? true : false); 
        int groupcnt = count_group(s);
        int ops;

			 if (groupcnt == 1 && !lastminus)
			ops = 0;
		else if (groupcnt == 1 && lastminus)
			ops = 1;
		else if (groupcnt == 2 && !lastminus)
			ops = 1;
		else if (groupcnt == 2 && lastminus)
			ops = 2;
		else if (groupcnt > 2 && !lastminus)
			ops = groupcnt - 1;
		else if (groupcnt > 2 && lastminus)
			ops = groupcnt;

		printf("Case #%d: %d\n", i+1, ops);
	}

	fclose(stdin);
	fclose(stdout);
	return 0;	
}	
