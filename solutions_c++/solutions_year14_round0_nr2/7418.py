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



int main()
{
	int i,j,t,r,T,n,sum,ans,temp,ctr=0,ans1,ans2,casen=1;
	double c,f,x,total,present;
	FILE *ifp, *ofp;
	char outputFilename[] = "output.txt";

    ifp = fopen("input2large.in", "r");
	ofp = fopen(outputFilename, "w");

	fscanf(ifp,"%d", &t); T=t;
	while(T--)
    {
        total=0; present=2;
        fscanf(ifp,"%lf", &c);
        fscanf(ifp,"%lf", &f);
        fscanf(ifp,"%lf", &x);
        while(1)
        {
            if((x/present) > ((c/present)+(x/(present+f))))
            {
                total+=(c/present); present+=f;
            }
            else
            {
                total+=(x/present);
                break;
            }
        }


        fprintf(ofp,"Case #%d: ", casen);
        fprintf(ofp,"%.7f\n", total);
        casen++;
    }


	return 0;
}
