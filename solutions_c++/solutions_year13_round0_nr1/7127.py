#include <cstdlib>
#include <cstdio>
using namespace std;

int main(int argc, char** argv) {
    int tc;
    char temp;
    int i,j,k;
    int xwin,owin;
    char array[4][4];
    char **ptr=argv;
    FILE *ofp;
    char *ofn= *++ptr;
	ofp = fopen(ofn,"w");
	if (ofp == NULL) {
		fprintf(stderr, "Can't open output file\n");
		exit(1);
	}
    scanf("%d",&tc);
    for(i=0;i<tc;i++)
    {
        for(j=0;j<4;j++)
        {
            scanf("%c",&temp);
            for(k=0;k<4;k++)
            {
                scanf("%c",&array[j][k]);
            }
        }
        fprintf(ofp,"Case #%d: ",i+1);
        for(j=0;j<4;j++)
        {
            xwin=0,owin=0;
            for(k=0;k<4;k++)
            {
                if(array[j][k]=='X')    xwin++;
                else if(array[j][k]=='O')       owin++;
                else if(array[j][k]=='T')       xwin++,owin++;
            }
            if(xwin==4)
            {
                fprintf(ofp,"X won");
                goto end;
            }
            else if(owin==4)
            {
                fprintf(ofp,"O won");
                goto end;
            }
        }
        for(j=0;j<4;j++) 
        {
            xwin=0,owin=0;
            for(k=0;k<4;k++)
            {
                if(array[k][j]=='X')    xwin++;
                else if(array[k][j]=='O')       owin++;
                else if(array[k][j]=='T')       xwin++,owin++;
            }
            if(xwin==4)
            {
                fprintf(ofp,"X won");
                goto end;
            }
            else if(owin==4)
            {
                fprintf(ofp,"O won");
                goto end;
            }
        }
        xwin=0,owin=0;
        for(j=0,k=0;j<4;j++,k++)
        {
            if(array[k][j]=='X')        xwin++;
            else if(array[k][j]=='O')   owin++;
            else if(array[k][j]=='T')   xwin++,owin++;
        }
        if(xwin==4)
        {
            fprintf(ofp,"X won");
            goto end;
        }
        else if(owin==4)
        {
            fprintf(ofp,"O won");
            goto end;
        }
        xwin=0,owin=0;
        for(j=0,k=3;j<4;j++,k--)
        {
            if(array[k][j]=='X')        xwin++;
                else if(array[k][j]=='O')       owin++;
                else if(array[k][j]=='T')       xwin++,owin++;
        }
        if(xwin==4)
        {
            fprintf(ofp,"X won");
            goto end;
        }
        else if(owin==4)
        {
            fprintf(ofp,"O won");
            goto end;
        }
        
        for(j=0;j<4;j++)
        {
            for(k=0;k<4;k++)
            {
                if(array[j][k]=='.')
                {
                    fprintf(ofp,"Game has not completed");
                    goto end;
                }
            }
        }
        
        fprintf(ofp,"Draw");
end:    fprintf(ofp,"\n");
        scanf("%c",&temp);
    }
	fclose(ofp);
    return 0;
}

