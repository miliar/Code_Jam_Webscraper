#include <iostream>
#include <cstdio>
#include <vector>
using namespace std;

int main()
{
	FILE *in, *out;
    in=fopen("B-large.in","r");
    out=fopen("B-large.out","w");
    int T,j;
    double C,F,X;
    fscanf(in,"%d",&T);
    for(int k=0;k<T;k++)
    {
        fscanf(in,"%lf %lf %lf",&C,&F,&X);
        vector<double> costOfFarms;
        vector<double> totalTime;
        
		double init = 2.0,val,temp;
        costOfFarms.push_back(0.0);
        costOfFarms.push_back((C/init));
        totalTime.push_back(X/2.0);
        totalTime.push_back((X/(2.0+F))+costOfFarms[1]);
        j=1;
        while(1)
        {
            temp=(C/(init+(F*j)));
            val = costOfFarms[costOfFarms.size()-1];
            costOfFarms.push_back(temp+val);
            j++;
            if(totalTime[totalTime.size()-2]<totalTime[totalTime.size()-1])
                break;
            totalTime.push_back((X/(2.0+(j*F)))+costOfFarms[j]);
            }
			
        fprintf(out,"Case #%d: %.7f\n",k+1,totalTime[totalTime.size()-2]);
    }
    return 0;
}


