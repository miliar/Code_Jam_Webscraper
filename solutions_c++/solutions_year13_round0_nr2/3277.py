#include <string>
#include <math.h>
#include <string.h>
#include <stdio.h>
#include <time.h>
#include <iostream>
#include <fstream>
#include <limits.h>

typedef unsigned __int64 lint; 

#define F(i,b) for(lint i=0;i<(b);i++)
#define FIAN(i,a,n) for(lint i=a;i<n;i++)
#define FIANrev(i,a,n) for(lint i=a;i>n;i--)

using namespace std;

FILE * inputFile = fopen("D:\\Downloads\\Chrome\\B-small-attempt0.in", "r");
FILE * outputFile  = fopen("D:\\Downloads\\Chrome\\output.txt", "w");

int **a, N, M;
int *Nmax, *Mmax;
string res;
string line;
float sum;

//lint calcToysByIterator(const lint &i, const lint &j){
//	if ((i==N)||(j==M)) return 0;
//	lint res = 0;
//	if (A[i]==B[j]){
//		if (a[i] > b[j]){
//			a[i] -= b[j];
//			res += b[j] + calcToysByIterator(i,j+1);
//			a[i] += b[j];
//		}
//		if (b[j] > a[i]){
//			b[j] -= a[i];
//			res += a[i] + calcToysByIterator(i+1,j);
//			b[j] += a[i];
//		}
//		if (b[j] == a[i]){
//			res += a[i] + calcToysByIterator(i+1,j+1);
//		}
//	}
//	else{
//		res += max(calcToysByIterator(i+1,j),calcToysByIterator(i,j+1));
//	}
//	return res;
//}

void oneStep()
{
	res = "YES";

	fscanf(inputFile, "%d %d", &N, &M);

	a = new int*[N];
	F(i,N)
	{
		a[i] = new int[M];
		int tmp;
		F(j,M) 
		{
			fscanf(inputFile, "%d", &tmp);
			a[i][j] = tmp;
		}
	}

	Nmax = new int[N];
	Mmax = new int[M];
	F(i, N)
	{
		Nmax[i] = a[i][0];
		F(j, M) Nmax[i] = max(Nmax[i], a[i][j]);
	}
	F(j, M)
	{
		Mmax[j] = a[0][j];
		F(i, N) Mmax[j] = max(Mmax[j], a[i][j]);
	}

	F(i,N) F(j,M)
	{
		int tmp = a[i][j];
		if (tmp < Nmax[i] && tmp < Mmax[j])
		{
			res = "NO";
			goto stop;
		}
	}
stop:
	fprintf(outputFile, "%s", res.c_str());
	fprintf(outputFile, "\n");
}

int main()
{
	time_t timer = time(NULL);
	printf("%s\n", ctime(&timer));

	unsigned int T;
	fscanf(inputFile, "%d", &T);

	F(t,T){
		//TODO: solve here!
		fprintf(outputFile, "Case #%d: ", t+1);
		oneStep();
		timer = time(NULL);
		printf("step %d - %s\n", t, ctime(&timer));
	}

	fclose(inputFile);
	fclose(outputFile);

	timer = time(NULL);
	printf("%s\n", ctime(&timer));
	// qDebug("Time elapsed: %d ms", time1.elapsed());
	return 0;
}