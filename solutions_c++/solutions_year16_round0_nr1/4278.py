#include <cstdio>
#include <cstring>

int main()
{
	int ti, tc,i;
	scanf("%d", &tc);
	for (ti = 1; ti <= tc; ++ ti) {
		unsigned long long num, next;
		scanf("%llu", &num);
		//printf("%llu\n", num);
		if (num==0) {
			printf("Case #%d: INSOMNIA\n", ti);
			continue;
		}
		bool seen[10];
		for (i=0;i<=9;++i)
			seen[i] = 0;
		
		bool found = 0;
		unsigned long long prod = 2;
		next = num;
		while (!found) {
			char str[30];
			sprintf(str, "%llu", next);
			int len =strlen(str);
			for (i=0;i<len;++i)
				seen[str[i]-'0'] = 1;
			found = 1;
			for (i=0;i<=9;++i)
				if (seen[i]==0) {
					found = 0;
					break;
				}
			if (found) {
				printf("Case #%d: %llu\n",ti, next);
			}
			//printf("%llu\n", next);
			next =num *prod;
			prod++;
			
		}
	}

}