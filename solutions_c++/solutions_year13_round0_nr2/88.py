#include <stdio.h>

int min(int a, int b) {
	return a < b ? a : b;
}

int max(int a, int b) {
	return a > b ? a : b;
}

template<class T>
void mswap(T &a, T &b) {
	T tmp = a;
	a = b;
	b = tmp;
}

struct Lawn {
	int *data;
	int n, m;
	int *minRow, *maxRow;
	int *minCol, *maxCol;
	Lawn(int n, int m) {
		this->n = n;
		this->m = m;
		data = nullptr;
		minRow = nullptr;
		maxRow = nullptr;
		minCol = nullptr;
		maxCol = nullptr;
		if (n>0 && m>0) {
			data = new int[n*m];
			minRow = new int[n];
			maxRow = new int[n];
			minCol = new int[m];
			maxCol = new int[m];
		}
	}
	~Lawn() {
		if (data) {
			delete[] data;
			delete[] minRow;
			delete[] maxRow;
			delete[] minCol;
			delete[] maxCol;
		}
	}
	bool empty() {
		return n==0 || m==0;
	}
	int* elPtr(int i, int j) {
		return data + i*m + j;
	}
	int& el(int i, int j) {
		return *elPtr(i, j);
	}
	void compute() {
		for (int i=0; i<n; i++) {
			minRow[i] = 101;
			maxRow[i] = 0;
		}
		for (int i=0; i<m; i++) {
			minCol[i] = 101;
			maxCol[i] = 0;
		}
		for (int i=0; i<n; i++)
			for (int j=0; j<m; j++) {
				minRow[i] = min(minRow[i], el(i, j));
				maxRow[i] = max(maxRow[i], el(i, j));
				minCol[j] = min(minCol[j], el(i, j));
				maxCol[j] = max(maxCol[j], el(i, j));
			}
	}
	bool deleteRow(int r, int len) {
		return minRow[r]==len && maxRow[r]==len;
	}
	bool deleteCol(int c, int len) {
		return minCol[c]==len && maxCol[c]==len;
	}
	bool deleteEl(int r, int c, int len) {
		return deleteRow(r, len) || deleteCol(c, len);
	}
	bool exists(int value) {
		for (int i=0; i<n; i++)
			for (int j=0; j<m; j++)
				if (el(i, j) == value)
					return true;
		return false;
	}
	void swap(Lawn &other) {
		mswap(data, other.data);
		mswap(n, other.n);
		mswap(m, other.m);
		mswap(minRow, other.minRow);
		mswap(maxRow, other.maxRow);
		mswap(minCol, other.minCol);
		mswap(maxCol, other.maxCol);
	}
};

bool solve_lawnmower(const char *inFilename, const char *outFilename) {
	FILE *fin = fopen(inFilename, "r");
	FILE *fout = fopen(outFilename, "w");
	if (!fin || !fout)
		return false;

	int tests;
	fscanf(fin, "%d", &tests);
	for (int t=0; t<tests; t++) {
		int n, m;
		fscanf(fin, "%d%d", &n, &m);
		Lawn lawn(n, m);
		for (int i=0; i<n; i++)
			for (int j=0; j<m; j++)
				fscanf(fin, "%d", lawn.elPtr(i, j));
		lawn.compute();
		bool no = false;
		for (int len=1; len<=100; len++) if (lawn.exists(len)) {
			int newN = lawn.n, newM = lawn.m;
			for (int i=0; i<lawn.n; i++)
				if (lawn.deleteRow(i, len))
					newN--;
			for (int i=0; i<lawn.m; i++)
				if (lawn.deleteCol(i, len))
					newM--;

			if (newN==0 || newM==0)
				break;

			Lawn newLawn(newN, newM);
			newN = 0; newM = 0;
			for (int i=0; i<lawn.n; i++)
				for (int j=0; j<lawn.m; j++)
					if (!lawn.deleteEl(i, j, len)) {
						newLawn.el(newN, newM) = lawn.el(i, j);
						newM++;
						if (newM == newLawn.m) {
							newM = 0;
							newN++;
						}
					}
			if (newLawn.exists(len)) {
				no = true;
				break;
			}
			lawn.swap(newLawn);
			lawn.compute();
		}
		fprintf(fout, "Case #%d: %s\n", t+1, no ? "NO" : "YES");
	}

	fclose(fin);
	fclose(fout);

	return true;
}
