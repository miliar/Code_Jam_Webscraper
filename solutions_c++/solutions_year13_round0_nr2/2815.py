#include<cstdio>
#include<vector>
#include<set>
#include<utility>
#include<map>
#include<cstring>
#include<string>
#include<algorithm>

using namespace std;

int lawn[10][10];
int row[10], col[10];

int main()
{
    int t,i,j,n,m,k,l,c=1,val,check,test;
	char ch;
	FILE *ifp, *ofp;
    char outputFilename[] = "outl.txt";

    ifp = fopen("inl.in", "r");
	ofp = fopen(outputFilename, "w");
	
	fscanf(ifp, "%d", &t);
	while(t--)
	{
		fscanf(ifp,"%c", &ch);
		fscanf(ifp,"%d%d", &n, &m);
		memset(lawn,0, sizeof(lawn));
		memset(row,0,sizeof(row)); memset(col,0,sizeof(col));
		check=0;
		for(i=0;i<n;i++)
		{
			fscanf(ifp,"%c", &ch);
			for(j=0;j<m;j++)
			{
				fscanf(ifp,"%d", &val);
				lawn[i][j]=val;
			}
		}
        /*
        for(i=0;i<n;i++)
    	{
			printf("\n");
			for(j=0;j<m;j++)
			{
				printf("%d ", lawn[i][j]);
			}
		}*/
		
        for(i=0;i<n;i++)
        {
				test=0;
                for(k=0;k<m;k++)
				{
					if(lawn[i][k] != 1)
					{
						test=1;
						break;
					}
				}
                if(test != 1)
    				row[i]=1;
        }
				
				
				
        for(j=0;j<m;j++)
        {
				test=0;
                for(k=0;k<n;k++)
				{
					if(lawn[k][j] != 1)
					{
						test=1;
						break;
					}
				}
                if(test != 1)
    				col[j]=1;
        }
				
		
		for(i=0;i<n;i++)
		{
			for(j=0; j<m; j++)
			{
			val=lawn[i][j];
			
			if(val==1 && row[i] == 0 && col[j] == 0)
			{
				check=1;
				break;
			}
			}
			if(check == 1)
			   break;
		}
		fprintf(ofp,"Case #%d: ", c);
        c++;
		if(check == 0)
		   fprintf(ofp,"YES\n");
		else
		   fprintf(ofp,"NO\n");
		
	}

	return 0;
}