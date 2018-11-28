//
//  main.c
//  2016CodeJam
//
//  Created by 힘선주 on 2016. 4. 10..
//  Copyright © 2016년 Sunju. All rights reserved.
//

#include <stdio.h>
#pragma warning(disable:4996)

#define MAX 15
int T, N;
int V[MAX];
int main() {

	FILE *in, *out;
	in = fopen("A-large.in", "r");
	out = fopen("result.out", "w");

	fscanf(in,"%d",&T);

	for (int a = 1; a <= T; a++)
	{
		int i;
		fscanf(in,"%d", &N);
		for (i = 0; i<10; i++) V[i] = 0;

		if (N == 0)
		{
			fprintf(out,"Case #%d: INSOMNIA\n", a);
			continue;
		}
		if (N % 10 == 0) V[0] = 1;

		for (long long int x = N;; x += N)
		{
			for (long long int y = x; y>0; y /= 10)
			{
				if (V[y % 10] == 0) V[y % 10] = 1;
			}
			for (i = 0; i<10; i++) if (V[i] == 0)break;

			if (i == 10)
			{
				fprintf(out,"Case #%d: %lld\n", a, x);

				break;
			}
		}
	}


	return 0;
}