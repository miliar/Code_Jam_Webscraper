#include <stdio.h>
#include <stdlib.h>

FILE * f;
FILE * fl;
int v[1024];

int main()
{
    f = fopen("B-large.in", "r");
    fl = fopen("B-large.out", "w");
    int i, j, best, test, cases, unempty, maxPile = 0;
    int minPassed;
    ///bool exit = false;

    fscanf(f, "%d", &cases);
    for(test = 0; test < cases; test++)
    {
        fscanf(f, "%d", &unempty);
        best = 1000001;
        for(i = 0; i < unempty; i++)
        {
            fscanf(f, "%d", &v[i]);
            if(v[i] > maxPile)
                maxPile = v[i];
        }

        for(i = 1; i <= maxPile; i++)
        {
            minPassed = i;
            for(j = 0; j < unempty; j++)
            {
                if(v[j] > i)
                {
                    minPassed = minPassed + ((v[j]/i)-1);
                    if(v[j] % i != 0)
                        minPassed++;
                }
            }
            ///v[maxPile] = v[maxPile] - minPassed - 1;
        		/*int mux=maxVet(v);
        		for(int j=1;j<=mux;j++){
        			secs=j;
        			for(int i=0;i<v.length;i++){
        				if(v[i]>j){
        					secs=secs+((v[i]/j)-1);
        					if(v[i]%j != 0){
        						secs++;
        					}
        				}
        			}
        		if (secs<migliore){
        				migliore=secs;
        		}
        		}
        		pw.println("Case #"+cont+": "+migliore);*/
            ///minPassed++;
            ///printf("%d", minPassed);
            if(minPassed < best)
                best = minPassed;
        }
        fprintf(fl, "Case #%d: %d\n", test+1, best);
    }



    fclose(f);
    fclose(fl);
    return 0;
}
