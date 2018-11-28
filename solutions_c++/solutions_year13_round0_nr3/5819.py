#include <cstdio>
#include <cmath>
#include <string>

bool pal(int n);
bool isSquarePoly(int a)
{
	bool res1 = false;
	int floorSqrt = (int)floor(sqrt(a));
	if(floorSqrt*floorSqrt == a)
	{
		if(pal (a)) res1 = true;
		if(!pal(floorSqrt)) res1 = false;
	}
	if(res1) printf(" %d ", a);
	return res1;
}

bool pal(int n) 
{ 
    int a = n; 
    int b = 0; 
    while(n) 
    { 
        b = (b * 10) + (n % 10); 
        n /= 10; 
    } 
    return a == b;
}

void main()
{
	FILE *f = fopen("small.in", "r");
	FILE *fout = fopen ("out.out", "w+");
	int A, B, T;
	long answer = 0;
	fscanf(f,"%d", &T);
	for(int t = 1; t <= T; t++)
	{
		fscanf(f, "%d %d", &A, &B);
		for(int  i = A; i <= B; i++)
		{
			if(isSquarePoly(i)) answer++;
		}
		fprintf(fout, "Case #%d: %d\n", t, answer);
		answer = 0;
	}
}