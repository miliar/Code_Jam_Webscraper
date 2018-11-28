#include <cstdio>
#include <cstring>
#include <algorithm>
#include <map>
#include <vector>
#include "string"


int main(int argc, char *argv[])
{
	FILE *fin, *fout;
	if (argc > 1)
	{
		char tname[200];
		fin = fopen(argv[1],"r");
		strncpy (tname,argv[1],200);
		strncpy(strstr (tname,".in"),".out",4);
		fout = fopen(tname,"w");
	} else {
		fin = fopen("A.in","r");
		fout = fopen("A.out","w");
	}


	int t;
	fscanf(fin,"%d",&t);
  int mp[30];
	for (int ti=0; ti<t; ti++)
	{
		int n;
		fscanf(fin,"%d", &n);
    
    for (int i=0; i<n; i++)
    {
      fscanf(fin,"%d", mp+i);
    }
		std::string evacp;
    int mpleft = 0;
    for (int i=0; i<n; i++) mpleft += mp[i];

	while (mpleft > 0)
	{
		int max0 = 0;
		int max1 = 0;
		int max2 = 0;
		int im0 = -1;
		int im1 = -1;
		int im2 = -1;
		for (int i = 0; i < n; i++)
		{
			if (mp[i] > max0) {
				max2 = max1;
				im2 = im1;
				max1 = max0;
				im1 = im0;
				max0 = mp[i];
				im0 = i;

			} else 	if (mp[i] > max1) {
				max2 = max1;
				im2 = im1;
				max1 = mp[i];
				im1 = i;

			} else 	if (mp[i] > max2) {
				max2 = mp[i];
				im2 = i;

			}
		}
		if (mpleft > 3)
		{
			if (max0 > 1)
			{
				if (2 * max1 <= mpleft - 2)
				{
					evacp = evacp + (char)('A' + im0) + (char)('A' + im0) + ' ';
					mp[im0] -= 2;
				}
				else
				{
					evacp = evacp + (char)('A' + im0) + (char)('A' + im1) + ' ';
					mp[im0]--;
					mp[im1]--;
				}
			}
			else
			{
				evacp = evacp + (char)('A' + im0) + (char)('A' + im1) + ' ';
				mp[im0]--;
				mp[im1]--;
			}
			mpleft -= 2;
		}
		else if (mpleft == 3)
		{
			evacp = evacp + (char)('A' + im0) + ' ';
			mp[im0] -= 1;
			mpleft--;
		}
		else {
			evacp = evacp + (char)('A' + im0) + (char)('A' + im1) + ' ';
			mp[im0]--;
			mp[im1]--;
			mpleft -= 2;
		}

	}

		fprintf(fout,"Case #%d: %s\n", ti+1, evacp.c_str());

	}
	fclose(fin);
	fclose(fout);
	return 0;
}