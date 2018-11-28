#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <cmath>
#include <vector>
#include <map>

using namespace std;

int mp[100][100];
char seq[100];

int main(){
	int T,ti,N,i,ni,j,k,sum,flag,le;
	int mid,temp;
	char str[128];
	double po;
	FILE * fin, * fout;
	fin = fopen("A-small-attempt2.in","r");
	fout = fopen("A-small-attempt2.out","w");
	fscanf(fin,"%d",&T);
	flag=0;
	for (ti=0;ti<T;ti++){
		flag=0;
		fscanf(fin,"%d",&N);
		memset(mp,0,sizeof(mp));
		for (i=0;i<N;i++){
			fscanf(fin,"%s",str);
			le=strlen(str);
			if (i==0){
				j=0;
				ni=0;
				while(j<le){
					seq[ni]=str[j];
					while (str[j]!='\0'&&seq[ni]==str[j]) {
						j++;
						mp[ni][i]+=1;
					}
					ni++;
				}
			}
			else {
				j=0;
				k=0;
				while (k<ni){
					if (seq[k]!=str[j]){
						flag=-1;
						break;
					}
					while (str[j]!='\0'&&seq[k]==str[j]) {
						j++;
						mp[k][i]+=1;
					}
					k++;
				}
				if (j!=le){
						flag=-1;
						break;
				}
			}
		}
		if (flag!=-1){
			sum=0;
			for (i=0;i<ni;i++){
				temp=0;
				sort(&mp[i][0],&mp[i][N]);
				mid=mp[i][N/2];
				for (j=0;j<N;j++){
					if (mp[i][j]>mid) temp+=mp[i][j]-mid;
					else temp+=mid-mp[i][j];
				}
				sum+=temp;
			}
		}
		if (flag==-1) fprintf(fout,"Case #%d: Fegla Won\n",ti+1);
		else fprintf(fout,"Case #%d: %d\n",ti+1,sum);
	}
	fclose(fout);
	fclose(fin);
	return 0;
}
