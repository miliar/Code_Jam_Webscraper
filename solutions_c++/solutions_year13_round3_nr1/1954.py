#include <cstdio>
#include <cstdlib>
#include <cstring>
bool isC(char a)
{
	if (a == 'a' || a == 'e' || a == 'i' || a == 'o' || a == 'u')
		return false;
	return true;
}
bool hasC(char *name, int i, int j, int n)
{
	int ccount = 0, k = 0;
	while (i <= j){
		if(isC(name[i])) {
			ccount++;
			if(ccount >= n)
				return true;
		}
		else {
			ccount = 0;
		}
		i++;
	}
	return false;
}
int countC(char *name, int nameLen, int size, int n) 
{
	int i = 0, j, count = 0;
	for(i = 0; i < nameLen - size+1; i++){
		j = i + size -1;
		if(hasC(name, i, j, n))
			count++;
	}
	//printf ("\n%s has %d nvalue for substring size %d", name, count, size);
	return count;
}
int main()
{
	const size_t size = 1000004;
	int numOfCases, i, j;
	char *name = (char *)malloc(size);
	//char name[256];
	int n, nvalue, nameLen, count;

	scanf("%d", &numOfCases);
	for (i = 0; i < numOfCases; i++){
		scanf("%s %d", name, &n);
		nameLen = strlen(name);
		count  = 0;

		/*numOfCases = 1;
		strcpy(name, "gcj");
		nameLen = 3;
		n = 2;*/

		for (j = n; j <= nameLen; j++ ){
			count +=countC(name, nameLen, j, n);
		}
		printf("Case #%d: %d\n", i+1, count);
	}

	free(name);

	return 0;
}

