#include <iostream>
#include <string.h>
#include <stdio.h>

using namespace std;

static int count_set_bits(int n)
{
	int c = 0;
	while(n)
	{
		n = n & (n-1);
		c++;
	}
	return c;
}

char c[5];
char buf[17];

short int xmask;
short int omask;
short int dotmask;
short int tmask;

int main()
{
	FILE *fp = fopen("A-large.in", "r");
	if(!fp)
		return -1;
	int t,i,j;
//	char newline[2];
	if(fscanf(fp, "%d", &t) != 1)
		return printf("Can't read number of test cases\n");
	for(i = 1; i <= t; i++)
	{
		xmask = 0x0;
		omask = 0x0;
		dotmask = 0x0;
		tmask = 0x0;
	
		c[0] = buf[0] = '\0';

		cout<<"Case #"<<i<<": ";
		for(j = 0; j < 4; j++)
		{
			fscanf(fp, "%s", c);
			strcat(buf, c);
		}
		for(j = 0; j < 16; j++)
		{
			if(buf[j] == 'X' || buf[j] == 'x')
				xmask |= (1<<j);
			else if(buf[j] == 'O' || buf[j] == 'o')
				omask |= (1<<j);
			else if(buf[j] == '.')
				dotmask |= (1<<j);
			else if(buf[j] == 'T' || buf[j] == 't')
				tmask |= (1<<j);
		}
		if( (xmask & 0x000f) == 0x000f || (xmask & 0x00f0) == 0x00f0 || (xmask & 0x0f00) == 0x0f00 || (xmask & 0xf000) == 0xf000 
				|| (xmask & 0x1248) == 0x1248 || (xmask & 0x8421) == 0x8421 || (xmask & 0x1111) == 0x1111 
				|| (xmask & 0x2222) == 0x2222 || (xmask & 0x4444) == 0x4444 || (xmask & 0x8888) == 0x8888 )	
		{	cout<<"X won\n"; continue; }
		
		else if( (omask & 0x000f) == 0x000f || (omask & 0x00f0) == 0x00f0 || (omask & 0x0f00) == 0x0f00 || (omask & 0xf000) == 0xf000 
				|| (omask & 0x1248) == 0x1248 || (omask & 0x8421) == 0x8421 || (omask & 0x1111) == 0x1111 
				|| (omask & 0x2222) == 0x2222 || (omask & 0x4444) == 0x4444 || (omask & 0x8888) == 0x8888 )	
		{	cout<<"O won\n"; continue; }
		
		else
		{
		xmask |= tmask;
		omask |= tmask;
		
		if( (xmask & 0x000f) == 0x000f || (xmask & 0x00f0) == 0x00f0 || (xmask & 0x0f00) == 0x0f00 || (xmask & 0xf000) == 0xf000 
				|| (xmask & 0x1248) == 0x1248 || (xmask & 0x8421) == 0x8421 || (xmask & 0x1111) == 0x1111 
				|| (xmask & 0x2222) == 0x2222 || (xmask & 0x4444) == 0x4444 || (xmask & 0x8888) == 0x8888 )	
		{	cout<<"X won\n"; continue; }
		
		else if( (omask & 0x000f) == 0x000f || (omask & 0x00f0) == 0x00f0 || (omask & 0x0f00) == 0x0f00 || (omask & 0xf000) == 0xf000 
				|| (omask & 0x1248) == 0x1248 || (omask & 0x8421) == 0x8421 || (omask & 0x1111) == 0x1111 
				|| (omask & 0x2222) == 0x2222 || (omask & 0x4444) == 0x4444 || (omask & 0x8888) == 0x8888 )	
		{	cout<<"O won\n"; continue; }
		
		else if(count_set_bits(dotmask) != 0)
			cout<<"Game has not completed\n";
		else 
			cout<<"Draw\n";
		}
	}	
	
	return 0;
}
