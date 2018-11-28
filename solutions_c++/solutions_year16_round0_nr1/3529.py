#include "stdio.h"
#include "memory.h"

const int p2[10] = {1,2,4,8,16,32,64,128,256,512};

int appeared;

void update(int x)
{
    while (x>0)
    {
        appeared |= p2[x%10];
        x /= 10;
    };
}

int main(void)
{
    int n;
    FILE * pFile,*pFileout;
    pFile = fopen("input.in","r");
    pFileout = fopen("output.txt","w");
    fscanf(pFile,"%d",&n);
    int i,j,k;
    for (i=0;i<n;i++)
    {
        int x;
        appeared = 0;
        fscanf(pFile,"%d",&x);
        if (x == 0)
        {
            fprintf(pFileout,"Case #%d: INSOMNIA\n",i+1);
            continue;
        }
        j = 1;
        while (1)
        {
            update(j*x);
            if (appeared == 0x3FF)
            {
                fprintf(pFileout,"Case #%d: %d\n",i+1,j*x);
                break;
            }
            j++;
        }
    }
    fclose(pFile);
    fclose(pFileout);
    return 0;
}

