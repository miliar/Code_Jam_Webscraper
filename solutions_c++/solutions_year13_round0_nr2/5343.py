#include<stdio.h>
FILE *in=fopen("b.in","r");
FILE *out=fopen("b.out","w");

int x[100][100],n,m,q,max_col[100],max_row[100],row_is_equal[100],col_is_equal[100];

void check()
{
	int i,j;
    //col
    //each cell, if not maximum, then the whole row should be equal
    for(j=0; j<m; j++)
    	for(i=0; i<n; i++)
    		if(x[i][j]!=max_col[j] && row_is_equal[i]==0)
    		{
    			fprintf(out,"Case #%d: NO\n",q);
		    	return;
		    }
    //row
    //each cell if Not maximum, then the whole col should be equaled
    for(i=0; i<n; i++)
    	for(j=0; j<m ;j++)
    		if(x[i][j]!=max_row[i] && col_is_equal[j]==0)
    		{
    			fprintf(out,"Case #%d: NO\n",q);
		    	return;
		    }
    fprintf(out,"Case #%d: YES\n",q);
    return;
}


int main()
{
    int t,i,j;
    fscanf(in,"%d",&t);
    for(q=1; q<=t; q++)
    {
        fscanf(in,"%d%d",&n,&m);
        for(i=0; i<n; i++)
            for(j=0; j<m;j++)
            {
                fscanf(in,"%d",&x[i][j]);
                if(i==0)
                    max_col[j] = x[i][j];
                else
                    max_col[j] >?= x[i][j];
                if(j==0)
                    max_row[i] = x[i][j];
                else
                    max_row[i] >?= x[i][j];
                if(j==0)
                    row_is_equal[i]=1;
                else if(row_is_equal[i])
                    row_is_equal[i] = (x[i][j]==x[i][j-1]);
                if(i==0)
                    col_is_equal[j] = 1;
                else if(col_is_equal[j])
                    col_is_equal[j] = x[i][j]==x[i-1][j];
            }
        check();
    }
    return 0;
}
