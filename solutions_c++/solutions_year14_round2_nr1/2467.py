#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <set>

char str[100][102];
char mainStr[102];
int N;
bool printEn = false;
using namespace std;

int solve()
{
	int ret = 0;
	int i,j;
	char num[100][101];
	for(i=0;i<N;i++)
		for(j=0;j<101;j++)
		{
			num[i][j] = 0;
		}
	strcpy(mainStr,str[0]);
	j=0;
	for(i=0;i<strlen(str[0]);)
	{
		mainStr[j] = str[0][i];
		while(str[0][i] == mainStr[j])i++;
		j++;
	}
	mainStr[j]=0;
//	for(i=0; mainStr[i];)
//		if(mainStr[i] == mainStr[i+1])
//			strcpy(&mainStr[i],&mainStr[i+1]);
//		else
//			i++;
if(printEn)cout<<"main>"<<mainStr<<endl;
	int len = strlen(mainStr);
	for(i=0;i<N;i++)
	{
		int k = 0;
if(printEn)cout<<i<<" "<<str[i]<<endl;
		for(j=0;j<len;j++)
		{
if(printEn)cout<<j<<' '<<mainStr[j]<<' '<<str[i][k]<<endl;
			while(mainStr[j] == str[i][k])
			{
				num[i][j]++;
				k++;
			}
			if(!num[i][j])
				return -1;
		}
if(printEn)cout<<"aha"<<k<<' '<<strlen(str[i])<<endl;
		if(k!=strlen(str[i]))
			return -1;
	}
	for(j=0;j<len;j++)
	{
		double mean = 0;
		for(i=0;i<N;i++)
			mean += num[i][j];
		mean/=N;
		if((mean - ((int) mean)) < 0.5)
			mean = (int)mean;
		else
			mean = 1 + (int) mean;
		for(i=0;i<N;i++)
			ret += abs(num[i][j]-mean);
	}
	return ret;
}

int main()
{
	FILE *in,*out;
	char line[1000];
	int T, t;
	int i, j;
	in = fopen("A.in","r");
	out = fopen("A.out","w+");
//	fgets(line,999,in);
//	sscanf(line,"%d",&T);
	fscanf(in,"%d ",&T);
	for(t = 1; t <= T; t++)
	{
		fscanf(in,"%d ",&N);
		for(i=0; i<N; i++)
		{
			fgets(str[i],102,in);//empty line
			j = strlen(str[i]);
			while(str[i][j]<'a' || str[i][j]>'z')str[i][j--] = 0;
		}
if(t==4)printEn=true;else printEn=false;
		i=solve();
		if(i<0)
			fprintf(out, "Case #%d: Fegla Won\n", t);
		else
			fprintf(out, "Case #%d: %d\n", t, i);
	}
	fclose(in);
	fclose(out);
}
