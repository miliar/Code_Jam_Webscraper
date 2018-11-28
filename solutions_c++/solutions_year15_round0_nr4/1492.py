#include <bits/stdc++.h>
using namespace std;

int main()
 { freopen("ran.txt","r",stdin);
	freopen("o.txt","w",stdout);
	int test_case,case_no,a,b,C;
	scanf("%d", &test_case);
	for(case_no = 1; case_no <= test_case; case_no++)
	 {
		scanf("%d %d %d", &a,&b,&C);
		int omin = b*C;
		if(a == 1)
		{
			printf("Case #%d: GABRIEL\n", case_no);
		}else if(a == 2)
		{
			if(omin%2 == 0){
				printf("Case #%d: GABRIEL\n", case_no);
			}else{
				printf("Case #%d: RICHARD\n", case_no);
			}
		}
		else if(a == 3)
		{
			if(omin == 6 || omin == 9 || omin == 12)
			{
				printf("Case #%d: GABRIEL\n", case_no);
			}
			else
			{
				printf("Case #%d: RICHARD\n", case_no);
			}
		}
		else
		{
			if(omin == 12 || omin == 16)
			{
				printf("Case #%d: GABRIEL\n", case_no);
			}
			else
			{
				printf("Case #%d: RICHARD\n", case_no);
			}
		}
	}
	fclose(stdout);
	return 0;
}
