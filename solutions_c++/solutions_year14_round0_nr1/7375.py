#include<iostream>
#include<cstdio>
#include<fstream>
#include<cstdlib>
using namespace std;

int main()
{
    FILE * file=fopen("A-small-attempt0.in","r");
    FILE * file2=fopen("output.txt","w");
	int mas[4][4];
	int mas2[4][4];
	int count;
	fscanf(file,"%d",&count);
	for (int s = 0; s < count; s++)
	{
	    int n,m;
	    fscanf(file,"%d",&n);
	    for(int j=0;j<4;j++)
        {
            for(int k=0;k<4;k++)
            {
                fscanf(file,"%d",&mas[j][k]);
            }
        }
        fscanf(file,"%d",&m);
        for(int j=0;j<4;j++)
        {
            for(int k=0;k<4;k++)
            {
                fscanf(file,"%d",&mas2[j][k]);
            }
        }
        n--;m--;
	    /**/
	    int c=0;
	    int num;
	    for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                if(mas[n][i]==mas2[m][j])
                {
                    c++;
                    num=mas[n][i];
                }
            }
        }
        if(c==0) fprintf(file2,"Case #%d: Volunteer cheated!\n",s+1);
        else if(c==1)fprintf(file2,"Case #%d: %d\n",s+1,num);
        else if(c>1)fprintf(file2,"Case #%d: Bad magician!\n",s+1);
	}
	fclose(file);
	fclose(file2);
}
