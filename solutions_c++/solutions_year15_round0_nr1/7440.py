#include <cstdio>

using namespace std;


int main()
{

	FILE *fp,*rd;
	fp=fopen("C:/Users/prabhusa/Desktop/ans.txt","w");
	rd=fopen("C:/Users/prabhusa/Desktop/magic.txt","r");
	int T;
	fscanf(rd,"%d",&T);
	for (int test=1;test<=T;test++) {
		
		int max_lev,con=0,count=0;
		
		
			fscanf(rd,"%d",&max_lev);
			char levarr[max_lev+1];
			fscanf(rd,"%c",&levarr[0]);
			for(int j=0;j<=max_lev;j++) {
				fscanf(rd,"%c",&levarr[j]);
				printf("con: %d  j: %d count: %d levarr: %c\n",con,j,count,levarr[j]);
				if(con<j && j!=0) {
					count += j-con;
					con += j-con;
					printf("count increased count: %d, con: %d\t",count,con);
				}

				con+=(int) (levarr[j]-'0');
			}

		
			
			printf("Case #%d: %d\n",test,count);
			fprintf(fp,"Case #%d: %d\n",test,count); 
		
	}
}
	
