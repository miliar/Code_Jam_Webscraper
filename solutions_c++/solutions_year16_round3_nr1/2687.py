#include<iostream>
using namespace std;
#define _PROBLEM1
#ifdef _PROBLEM1
int main(){
	int l = 0, t;
	FILE *f, *g;
	g = fopen("C:\\Users\\hasee\\Downloads\\A-Large.out", "w");
	f = fopen("C:\\Users\\hasee\\Downloads\\A-Large.in", "r");
	fscanf(f, "%d", &t);
	while (l < t){
		fprintf(g, "Case #%d: ", l + 1);
		int x, m, k, n[2];
		k = 1;
		fscanf(f, "%d", &x);
		int *d = new int[x];
		for (int i = 0; i < x; i++)
			fscanf(f, "%d", &d[i]);
		int s = 0;
		for (int i = 0; i < x; i++)
		{
			s += d[i];
		}
		if (s % 2 != 0){
			m = 0;
			for (int i = 0; i < x; i++)
			{
				if (m < d[i]){ m = d[i]; n[0] = i; }
			}
			d[n[0]]--;
			fprintf(g, "%c ", n[0] + 65);
		}
		while (k != 0){
			n[0] = -1;
			n[1] = -1;
			for (int j = 0; j < 2; j++){
				m = 0;
				for (int i = 0; i < x; i++)
				{
					if (m < d[i] && d[i] != 0){ m = d[i]; n[j] = i; }
				}
				if (d[n[j]] != 0){ d[n[j]]--; }
			}
			if (n[0] != -1){ fprintf(g, "%c", n[0] + 65); }
			if (n[1] != -1){ fprintf(g, "%c", n[1] + 65); }
			fprintf(g, " ");
			k = 0;
			for (int i = 0; i < x; i++)
			if (d[i] != 0) k = 1;
		}
		l++;
		fprintf(g, "\n");
	}
}
#endif