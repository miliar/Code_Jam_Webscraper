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
	int i,t,r,T,n,sum,ans,temp;
	FILE *ifp, *ofp;
	char outputFilename[] = "output.txt";

    ifp = fopen("input.in", "r");
	ofp = fopen(outputFilename, "w");
	fscanf(ifp,"%d", &t);
	i=1;
	while(t--)
	{
		fscanf(ifp,"%d %d", &r, &T);
		ans=0; temp = r;
		sum=(2*temp)+1;
		while(sum<=T)
		{
			temp+=2;
			sum+=((2*temp)+1);
			ans++;
		}

		fprintf(ofp,"Case #%d: %d",i, ans);
		i++;
		if(t!=0)
		   fprintf(ofp,"\n");
	}
	return 0;
}
