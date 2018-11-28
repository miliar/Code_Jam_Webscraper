#include <stdio.h>

int getnumber(int arr1[4],int arr2[4]);

int main()
{
	int T;
	int n;

	int a,b;

	int arr1[4], arr2[4];

	int i,j,k,temp;

	FILE* fin=fopen("A-small-attempt0.in" , "r");
	FILE* fout=fopen("output.out","w");
	
	fscanf(fin,"%d",&T);

	for(i=0 ; i<T ; i++)
	{
		fscanf(fin, "%d",&a);
		for(j=1 ; j<a ; j++)
		{
			for(k=0 ; k<4 ; k++)
				fscanf(fin, "%d", &temp);
		}
		
		for(k=0 ; k<4 ; k++)
			fscanf(fin, "%d", &arr1[k]);

		for(j=0 ; j<4-a ; j++)
		{
			for(k=0 ; k<4 ; k++)
				fscanf(fin, "%d", &temp);
		}

		
		fscanf(fin, "%d",&a);
		for(j=1 ; j<a ; j++)
		{
			for(k=0 ; k<4 ; k++)
				fscanf(fin, "%d", &temp);
		}
		
		for(k=0 ; k<4 ; k++)
			fscanf(fin, "%d", &arr2[k]);

		for(j=0 ; j<4-a ; j++)
		{
			for(k=0 ; k<4 ; k++)
				fscanf(fin, "%d", &temp);
		}

		n=getnumber(arr1,arr2);
		if(n == 0)
			fprintf(fout,"Case #%d: Volunteer cheated!\n",i+1);
		else if(n == -1)
			fprintf(fout,"Case #%d: Bad magician!\n",i+1);
		else
			fprintf(fout,"Case #%d: %d\n",i+1,n);		
	}

	fclose(fin);
	fclose(fout);

	return 0;
}

int getnumber(int arr1[4],int arr2[4])
{
	int n=0;
	int i,j;

	for(i=0 ; i<4; i++)
	{
		for(j=0 ; j<4 ; j++)
		{
			if(arr1[i] == arr2[j])
			{
				if(n!=0)
					return -1;
				n=arr1[i];
			}
		}
	}

	return n;
}
