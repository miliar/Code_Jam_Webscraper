#include<iostream>
#include<string>
#include<cmath>
using namespace std;
FILE *fin = fopen("C-small-attempt0.in","r");
FILE *fout = fopen("outfile.txt","w");
int a,b;
bool OK(int x)
{
	char temp[100];
	sprintf(temp,"%d",x);
	int len = strlen(temp);
	int i = 0, j = len -1;
	while(i < j && temp[i] == temp[j]){
		i++;
		j--;
	}
	if(i<j)
		return false;
	return true;
}
void work()
{
	int i;
	int cnt = 0;
	for(i = a;i<=b;++i){
		if(!OK(i))
			continue;
		int ii = sqrt(i);
		if(ii * ii != i)
			continue;
		if(OK(ii))
			cnt++;
	}
	fprintf(fout,"%d\n",cnt);
}
int main()
{	
	int ca;
	fscanf(fin,"%d",&ca);
	int i;
	for(i = 1;i<=ca;++i){
		fscanf(fin,"%d%d",&a,&b);
		fprintf(fout,"Case #%d: ",i);
		work();
	}
	return 0;
}