/*
 * Pool_Small.cpp
 *
 *  Created on: May 30, 2015
 *      Author: jonathan
 */

#include <stdio.h>

int main()
{
	FILE* file,*out;
	file = fopen("B-small-attempt0.in","r");
	out = fopen("B-small-out.txt","w");
	int num,i,j,k,l;
	double *target = new double[2];
	double *t1 = new double[2];
	double *t2 = new double[2];
	double q1,q2;
	char a;
	fscanf(file,"%d",&num);
	for (i=0;i<num;i++)
	{
		fscanf(file,"%d",&j);
		if (j == 1)
		{
			for (k=0;k<2;k++) {fscanf(file,"%lf",&target[k]);}
			for (k=0;k<2;k++) {fscanf(file,"%lf",&t1[k]);}
			if (target[1] == t1[1] && t1[0] != 0)
			{
				fprintf(out,"Case #%d: %lf\n",i+1,target[0]/t1[0]);
			} else {fprintf(out,"Case #%d: IMPOSSIBLE\n",i+1);}
		}
		else if (j == 2)
		{
			for (k=0;k<2;k++) {fscanf(file,"%lf",&target[k]);}
			for (k=0;k<2;k++) {fscanf(file,"%lf",&t1[k]);}
			for (k=0;k<2;k++) {fscanf(file,"%lf",&t2[k]);}
			if (t1[1] == t2[1]) {
				if (target[1] == t1[1] && t1[0] + t2[0] != 0)
				{
					fprintf(out,"Case #%d: %lf\n",i+1,target[0]/(t1[0]+t2[0]));
				} else {fprintf(out,"Case #%d: IMPOSSIBLE\n",i+1);}
			} else {
				q2 = (t1[1]*target[0] - target[0]*target[1])/(t1[1] - t2[1]);
				q1 = (t2[1]*target[0] - target[0]*target[1])/(t2[1] - t1[1]);
				if (q1 >= 0 && q2 >= 0)
				{
					if (q1/t1[0] > q2/t2[0])
					{
						fprintf(out,"Case #%d: %lf\n",i+1,q1/t1[0]);
					} else {fprintf(out,"Case #%d: %lf\n",i+1,q2/t2[0]);}
				} else {fprintf(out,"Case #%d: IMPOSSIBLE\n",i+1);}
			}
		}
	}
}


