#include <stdio.h>
#include <algorithm>

int T;
int A;
int mo[1000000];
int i, j, k;
int n;
int ans=0;
int tmp, tmp2;

int icmp(const void *p1, const void *p2)
{
  int v1, v2;
  
  v1 = *(int *)p1;
  v2 = *(int *)p2;
  if(v1 < v2)
    return -1;
  else if(v1 == v2)
    return 0;
  else
    return 1;
}

int check(int a, int i){
	int ans=0;
	while (a <= i){
		a = 2*a - 1;
		ans+=1;
	}
	tmp2 = a;
	return ans;
}
void process(){
	FILE *ip, *op;

	ip = fopen("input.txt", "r");
	op = fopen("output.txt","w");
	
	fscanf(ip, "%d", &T);

	for (k=0; k<T; k++){
		fscanf(ip, "%d %d", &A, &n);

		for (i=0; i<n; i++){
			fscanf(ip, "%d", &mo[i]);
		}

		qsort(mo, n, sizeof(int), icmp);


		for (i=0; i<n; i++){
			if (A > mo[i]){
				A += mo[i];
				continue;
			}else{
				if ((2*A-1) > mo[i]){
					A = 2*A -1;
					A+=mo[i];
					ans +=1;
					continue;
				}else{
					
					if (A == 1){
						ans+=n-i;
						break;
					}

					tmp = check(A, mo[i]);
					if (n-i >= tmp){
						ans += tmp;
						A = tmp2;
						A+=mo[i];
						continue;
					}else{
						ans+=n-i;
						break;
					}
					
					
				}
			}
		}

		fprintf(op, "Case #%d: %d\n", k+1, ans);
		ans = 0;

	}



	fclose(ip);
	fclose(op);


}

int main(){
	process();
	return 0;
}
