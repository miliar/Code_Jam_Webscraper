#include <cstdio>
#include <cstdlib>
using namespace std;

int main() {
	FILE *in;
	in = fopen("A-large.in", "r");
	FILE *out;
	out = fopen("out.in", "w");
	int T;
	fscanf(in, "%d", &T);
	int cnt = 0;
	while (cnt < T) {
		int S = 0;
		fscanf(in, "%d", &S);
		int *shyArray = new int[S+1];
		char c;
		for (int i = 0; i <= S; i++) {
			c = fgetc(in);
			while (c == ' ') c = fgetc(in);
			if (c == '\0') break;
			if (c <= '9' && c >= '0') {
				shyArray[i] = (int) (c - '0');
			}
		}
		int nowNum = 0;
		int inviteNum = 0;
		for (int i = 0; i <= S; i++) {
			if (nowNum >= i)
				nowNum += shyArray[i];
			else {
				inviteNum += i - nowNum;
				nowNum = i + shyArray[i];
			}
		}
		
		fprintf(out, "Case #%d: %d\n", cnt + 1, inviteNum);
		cnt++;
	}
	fclose(in);
	fclose(out);
}
