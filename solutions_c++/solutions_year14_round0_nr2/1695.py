#include"cstdio"
#include"cstdlib"

main ()
{
    FILE *fpr,*fpw;
    fpr = fopen("B-large.in","r+");
    fpw = fopen("B-large.out","w+");
    int TEST;
    fscanf(fpr,"%d",&TEST);
    int n;
    for (n=1;n<=TEST;n++)
    {
        double rate=2.0;
        double time=0.0;
        double C,F,X;
        fscanf(fpr," %lf %lf %lf",&C,&F,&X);
        while (true)
        {
            double time1 = X/rate;
            double time2 = C/rate;
            double time3 = X/(rate+F);
            if (time1<=time2+time3) { time+=time1; break; }
            else { time+=time2; rate+=F; }
//            printf("FARM BOUGHT!\n");
        }
        fprintf(fpw,"Case #%d: ",n);
        fprintf(fpw,"%f",time);
        fprintf(fpw,"\n");
        printf("Case #%d: ",n);
        printf("%lf",time);
        printf("\n");
    }
    
    printf("YAY!");
    
    scanf(" ");
}
