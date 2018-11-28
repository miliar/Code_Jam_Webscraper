#include<cstdio>
#include<cstdlib>

using namespace std;

float naoBlock[1000];
float kenBlock[1000];

int cmp(const void* v1, const void* v2)
{
	float f1 = *(float*) v1;
	float f2 = *(float*) v2;
	return (f1 < f2) - (f1 > f2);
}

int main()
{
	int nCase;
	scanf("%d", &nCase);
	for (int z = 1; z <= nCase; ++z)
	{
		int nBlock;
		scanf("%d", &nBlock);
		for (int i = 0; i < nBlock; ++i)
			scanf("%f", &naoBlock[i]);
		for (int i = 0; i < nBlock; ++i)
			scanf("%f", &kenBlock[i]);

		qsort(naoBlock, nBlock, sizeof(float), cmp);
		qsort(kenBlock, nBlock, sizeof(float), cmp);

		//for (int i = 0; i < nBlock; ++i)
		//	printf("%.3f ", naoBlock[i]);
		//printf("\n");
		//for (int i = 0; i < nBlock; ++i)
		//	printf("%.3f ", kenBlock[i]);
		//printf("\n");


		int a1, a2;
		int in = 0, ik = 0;
		a1 = 0;
		while (in < nBlock && ik < nBlock)
		{
			while (naoBlock[in] < kenBlock[ik] && ik<nBlock - 1) ik++;
			if (naoBlock[in] > kenBlock[ik])
				++a1;
			++in;
			++ik;
		}

		in = 0; ik = 0;
		a2 = 0;
		while (in < nBlock && ik < nBlock)
		{
			while (kenBlock[ik] < naoBlock[in] && in<nBlock - 1)
			{
				++in;
				++a2;
			}
			if (kenBlock[ik] < naoBlock[in])
				++a2;
			++ik;
			++in;
		}
		printf("Case #%d: %d %d\n", z, a1,  a2);
	}
	return 0;
}