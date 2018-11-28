#include<bits/stdc++.h>
using namespace std;

int main()
{
	int t;
	char s[105];
	int n,m,f;
	FILE *fp,*fp1;
	fp = fopen("B-large.in","r");
	fp1 = fopen("output.txt","w");
	fscanf(fp,"%d",&t);
	for(int j=1;j<=t;j++){
		fscanf(fp,"%s",s);
		fprintf(fp1,"Case #%d: ",j);
		m =0;
		f = 0;
		n = strlen(s);
		for(int i=0;i<n;){
			if(s[i]=='-'){
				while(i<n&&s[i]=='-'){
					i++;
				}
				if(f==0){
					m += 1;
					f = 1;
				}
				else
				m += 2;
			}
			else{
			f = 1;
			i++;
			}
		}
		fprintf(fp1,"%d\n",m);
	}
	fclose(fp);
	fclose(fp1);
	return 0;	
}
