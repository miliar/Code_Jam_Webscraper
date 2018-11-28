//Author: Vipul Gaur
#include<cstdio>
#include<vector>
#include<set>
#include<utility>
#include<map>
#include<cstring>
#include<string>
#include<algorithm>
#include<bitset>

using namespace std;

int arr1[4][4], arr2[4][4];
int check[18];

int main()
{
	int i,j,t,r,T,n,sum,ans,temp,ctr=0,ans1,ans2,casen=1;
	FILE *ifp, *ofp;
	char outputFilename[] = "output.txt";

    ifp = fopen("input.in", "r");
	ofp = fopen(outputFilename, "w");

	fscanf(ifp,"%d", &t); T=t;
	while(T--)
    {
        memset(check,0,sizeof(check)); ctr=0;
        fscanf(ifp,"%d",&ans1 );
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                fscanf(ifp,"%d", &arr1[i][j]);
                if((i+1)==ans1)
                {
                    check[arr1[i][j]]=1;
                }
            }
        }
        fscanf(ifp,"%d",&ans2 );
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                fscanf(ifp,"%d", &arr2[i][j]);
                if((i+1)==ans2)
                {
                    if(check[arr2[i][j]]==1)
                    {
                        ctr++; ans=arr2[i][j];
                    }
                }
            }
        }
        fprintf(ofp,"Case #%d: ", casen);
        if(ctr==1)
            fprintf(ofp,"%d\n", ans);
        else if(ctr>1)
            fprintf(ofp,"Bad magician!\n");
        else
            fprintf(ofp,"Volunteer cheated!\n");
        casen++;
    }


	return 0;
}
