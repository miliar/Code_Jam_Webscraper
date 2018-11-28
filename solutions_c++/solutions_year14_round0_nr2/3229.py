#include <cstdio>
#include <vector>

using namespace std;


int T;
double C,F,X,time,new_time,whole_time,current_summing=2;
vector<double> results;

int main()
{
   freopen("C:\\Users\\Hepic\\Desktop\\out.txt","r",stdin);

   scanf("%d",&T);

   while(T--)
   {
       scanf("%lf%lf%lf",&C,&F,&X);

       while(true)
       {
           time=(double)(X/current_summing);

           new_time=(double)(C/current_summing);
           new_time+=(double)(X/(current_summing+F));

           if(new_time<time)
           {
               whole_time+=(double)(C/current_summing);
               current_summing+=F;
           }

           else if(time<=new_time)
           {
               whole_time+=time;
               break;
           }
       }

       results.push_back(whole_time);

       whole_time=0;
       current_summing=2;
   }


   for(int i=0; i<results.size(); ++i)
   {
       printf("Case #%d: %f\n",i+1,results[i]);
   }

   fclose(stdin);

   return 0;
}


