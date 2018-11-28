#include <algorithm>
#include <cstdio>
#include <cstring>
#include <vector>
#include <queue>

using namespace std;

char* INPUT_FILE = "D:\\Anton\\gcj_files\\C-large.in";
char* OUTPUT_FILE = "D:\\Anton\\gcj_files\\r1b_prob3_out.txt";
char* DICT_FILE = "D:\\Anton\\gcj_files\\garbled_email_dictionary.txt";
//char* DICT_FILE = "D:\\Anton\\gcj_files\\my_dict.txt";

int gt;
char word[102];
char input_word[4002];
int input_len;
string currw;

struct Node {
	Node* next[27];
	string last_word;
};

Node* root;
int dp[4002][5];
char stack[4002];

Node* create_node() {
	Node* tmp = new Node();
	memset(tmp->next, 0, sizeof(tmp->next));
	return tmp;
}

void add_word(const char* word, Node* node) {
	int index = ((*word == 0) ? 26 : (*word - 'a'));
	if (node->next[index] == NULL) {
		node->next[index] = create_node();
	}
	if (index < 26) {
		add_word(word+1, node->next[index]);
	}
	else {
		node->last_word = currw;
	}
}

void try_words(int pos, int steps, Node* node, int curr_value) {
	//printf("Trying %d, %d\n", pos, steps);
	steps = min(steps, 4);
	//if (pos == 38 && steps == 0) {
	//	printf("ghello\n");
	//}
	if (node->next[26] != NULL) {
		if (dp[pos][steps] == -1 || dp[pos][steps] > curr_value) {
			dp[pos][steps] = curr_value;
			//printf("Update %d, %d = %d with %s\n", pos, steps, curr_value, node->last_word.c_str());
			//if (pos == 8 && steps == 4) {
			//	printf("here\n");
			//}
		}
	}

	if (pos >= input_len) {
		return;
	}

	int index = input_word[pos] - 'a';
	if (node->next[index] != NULL) {
		//printf("%c ", input_word[pos]);
		try_words(pos+1, min(4, steps+1), node->next[index], curr_value);
	}

	if (steps >= 4) {
		for (int i = 0; i < 26; i++) {
			if (i == index) continue;
			if (node->next[i] != NULL) {
				try_words(pos+1, 0, node->next[i], curr_value+1);
			}
		}
	}
}

int main() {

	freopen(INPUT_FILE, "r", stdin);
	freopen(OUTPUT_FILE, "w", stdout);

	FILE *f = fopen(DICT_FILE, "r");
	//int max_len = 0;
	root = create_node();
	while(fgets(word, 100, f)) {
		if (word[strlen(word) - 1] == 10) {
			word[strlen(word) - 1] = 0;
		}
		currw = word;
		//max_len = max(max_len, (int)strlen(word));
		add_word(word, root);
	}
	fclose(f);

	//printf("%d\n", max_len);

	scanf("%d", &gt);

	input_word[0] = ' ';
	for (int gi=1; gi <= gt; gi++) {
		scanf("%s", input_word+1);
		input_len = strlen(input_word);
		for (int i = 0; i <= input_len; i++) {
			for (int j = 0; j < 5; j++) {
				dp[i][j] = -1;
			}
		}
		dp[1][4] = 0;
		for (int i = 1; i < input_len; i++) {
			for (int j = 0; j < 5; j++) {
				if (dp[i][j] != -1) {
					//printf("Trying222 %d, %d", i, j);
					try_words(i, j, root, dp[i][j]);
				}
			}
		}

		int ans = 1000000;
		for (int i = 0; i < 5; i++) {
			if (dp[input_len][i] != -1) {
				ans = min(ans, dp[input_len][i]);
			}
		}
/*
		for (int i = 0; i <= input_len; i++) {
			printf("%d ->", i);
			for (int j = 0; j < 5; j++) {
				printf(" %d", dp[i][j]);
			}
			printf("\n");
		}
		*/
		printf("Case #%d: %d\n", gi, ans);
	}

	return 0;
}
