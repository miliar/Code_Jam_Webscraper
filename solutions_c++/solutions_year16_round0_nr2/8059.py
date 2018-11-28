#include<iostream>
using namespace std;
int main(){
	char *x;
	x=new char[102];
	FILE *f,*g;
	f=fopen("C:\\Users\\hasee\\Downloads\\B-large.in","r");
	g=fopen("C:\\Users\\hasee\\Downloads\\B-large.out","w");
	fscanf(f,"%s",x);
	int a=0;
	while (!feof(f))
	{
		a++;
		fscanf(f,"%s ",x);
		int i=1,t=0;
		for (;x[i]!=NULL; i++)
		{
			if(x[i-1]!=x[i])
				t++;
		}
		if(x[i-1]=='-')
			t++;
		fprintf(g,"Case #%d: %d\n",a,t);
	}
	fclose(f);
	fclose(g);
	return 0;
};