#include<iostream>

#define lim 2000

FILE *inp, *out;

char str[lim+1];
int count[26],num[10];

void solve(int x)
{
	switch(x)
	{
		case 0:
			--count['Z'-'A'];
			--count['E'-'A'];
			--count['R'-'A'];
			--count['O'-'A'];
			++num[0];
			break;
		case 1:
			--count['O'-'A'];
			--count['N'-'A'];
			--count['E'-'A'];
			++num[1];
			break;
		case 2:
			--count['T'-'A'];
			--count['W'-'A'];
			--count['O'-'A'];
			++num[2];
			break;	
		case 3:
			--count['T'-'A'];
			--count['H'-'A'];
			--count['R'-'A'];
			--count['E'-'A'];
			--count['E'-'A'];
			++num[3];
			break;			
		case 4:
			--count['F'-'A'];
			--count['O'-'A'];
			--count['U'-'A'];
			--count['R'-'A'];
			++num[4];
			break;			
		case 5:			
			--count['F'-'A'];			
			--count['I'-'A'];
			--count['V'-'A'];
			--count['E'-'A'];
			++num[5];
			break;
		case 6:
			--count['S'-'A'];
			--count['I'-'A'];
			--count['X'-'A'];
			++num[6];
			break;
		case 7:
			--count['S'-'A'];
			--count['E'-'A'];
			--count['V'-'A'];
			--count['E'-'A'];
			--count['N'-'A'];
			++num[7];
			break;
		case 8:
			--count['E'-'A'];
			--count['I'-'A'];
			--count['G'-'A'];
			--count['H'-'A'];			
			--count['T'-'A'];
			++num[8];
			break;
		default:
			--count['N'-'A'];
			--count['I'-'A'];
			--count['N'-'A'];
			--count['E'-'A'];
			++num[9];
			break;		
	}
}

int main(){
	int T,i,j;	
	inp = fopen("inp.in","r");
	out = fopen("out.txt","w");
	fscanf(inp,"%d",&T);
	for(i=1;i<=T;++i)
	{
		fscanf(inp,"%s",str);
		for(j=0;j<26;++j)
		count[j]=0;
		for(j=0;j<10;++j)
		num[j]=0;
		for(j=0;str[j]!='\0';++j)
		{
			++count[str[j]-'A'];
		}
		while(count['Z'-'A']>0)
		solve(0);
		while(count['W'-'A']>0)
		solve(2);
		while(count['U'-'A']>0)
		solve(4);
		while(count['X'-'A']>0)
		solve(6);
		while(count['G'-'A']>0)
		solve(8);
		while(count['O'-'A']>0)
		solve(1);
		while(count['R'-'A']>0)
		solve(3);
		while(count['F'-'A']>0)
		solve(5);
		while(count['V'-'A']>0)
		solve(7);
		while(count['N'-'A']>0)
		solve(9);		
		fprintf(out,"Case #%d: ",i);
		for(j=0;j<10;++j)
		{
			while(num[j]-->0)
			fprintf(out,"%d",j);
		}
		fprintf(out,"\n");
	}
	return 0;
}
