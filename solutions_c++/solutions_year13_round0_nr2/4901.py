#include <stdio.h>
#include <fstream>

bool checkLawn(int lawn[100][100], int height, int width, int x, int y, int v) {
	bool result = false;
	
	bool vert = true;
	for(int i = 0; i < height; i++) {
		if(lawn[i][y] > v) {
			vert = false;
		}
	}

	bool horz = true;
	for(int i = 0; i < width; i++) {
		if(lawn[x][i] > v) {
			horz = false;
		}
	}

	return vert || horz;
}

void lawnT(std::fstream &in, FILE *out, int c) {
	int lawn[100][100];
	int width, height;
	in >> height;
	in >> width;

	for(int j = 0; j < height; j++) {
		for(int k = 0; k < width; k++) {
			in >> lawn[j][k];
		}
	}

	bool canMow = true;
	for(int j = 0; j < height; j++) {
		for(int k = 0; k < width; k++) {
			if(!checkLawn(lawn, height, width, j, k, lawn[j][k])) {
				fprintf(out, "Case #%d: NO\n", c);
				return;
			}
		}
	}

	fprintf(out, "Case #%d: YES\n", c);
}

int main(int argc, char **argv) {
	std::fstream in("input.txt");
	FILE *out = fopen("output.txt", "w");

	int lawns;
	in >> lawns;


	for(int i = 0; i < lawns; i++) {
		lawnT(in, out, i + 1);
	}

	in.close();
	fclose(out);
}