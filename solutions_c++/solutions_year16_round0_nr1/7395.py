#include<bits/stdc++.h>
using namespace std;

int main()
{
	int t;
	set<long long int>s;
	long long int n,k,tmp;
	FILE *fp,*fp1;
	fp = fopen("A-large.in","r");
	fp1 = fopen("output.txt","w");
	fscanf(fp,"%d",&t);
	for(int i=1;i<=t;i++){
		fscanf(fp,"%lld",&n);
		fprintf(fp1,"Case #%d: ",i);
		if(n==0){
			fprintf(fp1,"INSOMNIA\n");
		}
		else{
			k = n;
			while(true){	
				tmp = k;
				while(tmp!=0){
					s.insert(tmp%10);
					tmp /=10;
				}
				if(s.size()==10)
					break;
				k += n;
			}
			fprintf(fp1,"%lld\n",k);
		}
		s.clear();
	}
	fclose(fp);
	fclose(fp1);
	return 0;	
}
