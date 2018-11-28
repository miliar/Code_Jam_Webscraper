#include<stdio.h>
#include<string.h>
#include<vector>

using namespace std;

FILE *fin;
FILE *fout;

int a[10][10];
int b[10][10];
bool ansa[20];
bool ansb[20];

int main(){
	fin = fopen("A-small-attempt0.in","r");
	fout = fopen("gcj.out","w");
	int T;
	fscanf(fin,"%d",&T);
	int rowa,rowb;
	for(int cas = 1;cas <= T;++cas){
		fscanf(fin,"%d",&rowa);
		for(int i = 1;i <= 4;++i)
			for(int j = 1;j <= 4;++j)
				fscanf(fin,"%d",&a[i][j]);
		fscanf(fin,"%d",&rowb);
		for(int i = 1;i <= 4;++i)
			for(int j = 1;j <= 4;++j)
				fscanf(fin,"%d",&b[i][j]);
		memset(ansa,false,sizeof(ansa));
		memset(ansb,false,sizeof(ansb));
		for(int i = 1;i <= 4;++i){
			ansa[a[rowa][i]] = true;
			ansb[b[rowb][i]] = true;
		}
		vector<int> vec;
		for(int i = 1;i <= 16;++i)
			if(ansa[i] && ansb[i])
				vec.push_back(i);
		fprintf(fout,"Case #%d: ",cas);
		if(vec.size() > 1)
			fprintf(fout,"Bad magician!\n");
		else if(vec.size() == 0)
			fprintf(fout,"Volunteer cheated!\n");
		else
			fprintf(fout,"%d\n",vec[0]);
	}
	fclose(fin);
	fclose(fout);
	return 0;
}

