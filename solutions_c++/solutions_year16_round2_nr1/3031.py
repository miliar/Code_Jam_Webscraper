#include<iostream>
using namespace std;
void d(char *a, char *b){
	int t = 0;
	for (int i = 0; ; i++)
	{
		if (a[i] == b[t]){
			for (int j = i; a[j]!=NULL ; j++)
			{
				a[j] = a[j + 1];
			}
			t++;
			i = -1;
		}
		if (b[t]==NULL)
		{
			break;
		}
	}
}
void m(char *a){
	bool r = 0;
	for (int i = 0; ; i++)
	{
		if (a[i + 1]==NULL)
		{
			if (r == 0){ break; }
			else i = -1;
			r = 0;
			continue;
		}
		if (a[i]>a[i+1])
		{
			char x = a[i];
			a[i] = a[i + 1];
			a[i + 1] = x;
			r = 1;
		}
	}
}
int main(){
	char b[10000],a[20000];
	b[0] = NULL;
	int T;
	FILE *f, *g;
	f = fopen("C:\\Users\\hasee\\Downloads\\A-large.in", "r");
	g = fopen("C:\\Users\\hasee\\Downloads\\A-large.out", "w");
	fscanf(f, "%d", &T);
	int t = 0;
	while (t<T)
	{
		fscanf(f, "%s", a);
		while (a[0]!=NULL)
		{
			for (int i = 0; a[i] != NULL; i++)
			{
				if (a[i] == 'W')
				{
					strcat(b, "2");
					d(a, "TWO");
					i = -1;
				}
				else if (a[i] == 'G')
				{
					strcat(b, "8");
					d(a, "EIGHT");
					i = -1;
				}
				else if (a[i] == 'Z'){
					strcat(b, "0");
					d(a, "ZERO");
					i = -1;
				}
				else if (a[i] == 'U'){
					strcat(b, "4");
					d(a, "FOUR");
					i = -1;
				}
				else if (a[i] == 'X'){
					strcat(b, "6");
					d(a, "SIX");
					i = -1;
				}
			}
			for (int i = 0; a[i] != NULL; i++){
				if (a[i] == 'F'){
					strcat(b, "5");
					d(a, "FIVE");
					i = -1;
				}
				else if (a[i] == 'S'){
					strcat(b, "7");
					d(a, "SEVEN");
					i = -1;
				}
				else if (a[i] == 'T'){
					strcat(b, "3");
					d(a, "THREE");
					i = -1;
				}
				else if (a[i] == 'O'){
					strcat(b, "1");
					d(a, "ONE");
					i = -1;
				}
			}
			for (int i = 0; a[i] != NULL; i++){
				if (a[i] == 'I'){
					strcat(b, "9");
					d(a, "NINE");
					i = -1;
				}
			}
		}
		m(b);
		printf("Case #%d: %s\n", t + 1, b);
		fprintf(g, "Case #%d: %s\n", t+1, b);
		b[0] = NULL;
		t++;
	}
	fclose(f);
	fclose(g);
	return 0;
}