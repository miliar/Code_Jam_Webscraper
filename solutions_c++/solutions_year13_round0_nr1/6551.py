#include<iostream>
#include<fstream>
#include<cstring>
using namespace std;
FILE *fin = fopen("A-large.in","r");
FILE *fout = fopen("outfile.txt","w");
char st[4][9];
int cnt[90];
void init()
{
	int i;
	for(i=0;i<4;++i)
		fscanf(fin,"%s",st[i]);
}
bool out()
{
	if(cnt[88] == 4 || (cnt[88] == 3 && cnt[84] == 1)){
		fprintf(fout,"X won\n");
		return true;
	}
	else if(cnt[79] == 4 || (cnt[79] == 3 && cnt[84] == 1)){
		fprintf(fout,"O won\n");
		return true;
	}	
	return false;
}
void init1()
{
	cnt[88] = 0; cnt[84] = 0; cnt[79] = 0; cnt[46] = 0;
}
void work()
{
	int i,j;
	for(i=0;i<4;++i){
		init1();
		for(j=0;j<4;++j)
			cnt[st[i][j]]++;
		if(out()) return;
	}
	
	for(i=0;i<4;++i){
		init1();
		for(j=0;j<4;++j)
			cnt[st[j][i]]++;
		if(out()) return;
	}
	
	init1();
	cnt[st[0][0]]++;
	cnt[st[1][1]]++;
	cnt[st[2][2]]++;
	cnt[st[3][3]]++;
	
	if(out()) return;
	
	init1();
	cnt[st[0][3]]++;
	cnt[st[1][2]]++;
	cnt[st[2][1]]++;
	cnt[st[3][0]]++;
	
	if(out()) return;
	
	init1();
	for(i=0;i<4;++i)
		for(j=0;j<4;++j)
			cnt[st[i][j]]++;
		
		if(cnt[46] == 0)
			fprintf(fout,"Draw\n");
		else 
			fprintf(fout,"Game has not completed\n");
		
		
}	
int main()
{
	int ca;
	fscanf(fin,"%d",&ca);
	int i;
	for(i=1;i<=ca;++i){
		init();
		fprintf(fout,"Case #%d: ",i);
		work();
	}
	return 0;
}