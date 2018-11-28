#include<stdio.h>
#include<conio.h>
#include<iostream>

using namespace std;


int partition(int* input, int p, int r);
void quicksort(int* input, int p, int r);

int main()
{
	int t,i,j;
	int a[10],b[700],count;
	FILE *fp,*fp1;
	if((fp = fopen("A-large.in","r")) == NULL) {
		printf("Cannot open the file\n");
		return 0;
	}
	fp1 = fopen("A-large-output.in","w");
	fscanf(fp,"%d",&t);
	char ch;
	ch = fgetc(fp);
	for(i = 1;i <= t;i++){
		for(j=0;j<10;j++) {
			a[j] =0;
		}
		count=-1;
		while(1) {
			ch = fgetc(fp);
			if(ch == '\n' || ch ==  EOF) break;
			if(ch == 'G') {
				count++;
				b[count]=8;
				a[8]--;
				a[7]--;
			} else if (ch == 'U') {
				count++;
				b[count] = 4;
				a[5]--;
			} else if (ch == 'W') {
				count++;
				b[count]= 2;
			} else if (ch == 'X') {
				count++;
				b[count] = 6;
				a[6]--;
				a[8]--;
			} else if (ch == 'Z') {
				count++;
				b[count]= 0;		
			} else if (ch == 'F') {
				a[5]++;
			} else if (ch == 'S') {
				a[6]++;
			} else if (ch == 'H') {
				a[7]++;
			} else if (ch == 'I') {
				a[8]++;
			} else if (ch == 'N') {
				a[9]++;
			}
		}
		while(a[5]>0) {
			count++;
			a[5]--;
			a[8]--;
			b[count] = 5;
		}
		while(a[6]>0) {
			count++;
			a[6]--;
			a[9]--;
			b[count] = 7;
		}
		while(a[7]>0) {
			count++;
			a[7]--;
			b[count] = 3;
		}
		while(a[8]>0) {
			count++;
			b[count] = 9;
			a[9] = a[9] -2;
			a[8]--;
		}
		while(a[9]>0) {
			count++;
			b[count]= 1;
			a[9]--;
		}
		quicksort(b,0,count);
		fprintf(fp1,"Case #%d: ",i);
		for(j=0;j<=count;j++) {
			fprintf(fp1,"%d",b[j]);
		}
		fprintf(fp1,"\n");
		//printf("Case #%d: %lld\n",i,ans);
	}
	fclose(fp1);
	return 0;
}

int partition(int* input, int p, int r)
{
    int pivot = input[r];

    while ( p < r )
    {
        while ( input[p] < pivot )
            p++;

        while ( input[r] > pivot )
            r--;

        if ( input[p] == input[r] )
            p++;
        else if ( p < r )
        {
            int tmp = input[p];
            input[p] = input[r];
            input[r] = tmp;
        }
    }

    return r;
}

void quicksort(int* input, int p, int r)
{
    if ( p < r )
    {
        int j = partition(input, p, r);        
        quicksort(input, p, j-1);
        quicksort(input, j+1, r);
    }
}
