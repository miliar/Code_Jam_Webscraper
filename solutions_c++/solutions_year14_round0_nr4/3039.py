#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;


int T,blocks,naomi_war_score,naomi_deceitful_war_score,pos;
bool check_naomi_score;
double Naomi[1000];
double Ken[1000];
bool check_Naomi[1000];
bool check_Ken[1000];
vector<int> results[50];


int main()
{
   freopen("C:\\Users\\Hepic\\Desktop\\out.txt","r",stdin);

   scanf("%d",&T);

   while(T--)
   {
       scanf("%d",&blocks);

       for(int i=0; i<blocks; ++i)
       {
            check_Naomi[i]=true;
            check_Ken[i]=true;
       }

       for(int i=0; i<blocks; ++i)
            scanf("%lf",&Naomi[i]);

       for(int i=0; i<blocks; ++i)
            scanf("%lf",&Ken[i]);


       sort(Naomi,Naomi+blocks);
       sort(Ken,Ken+blocks);


       check_naomi_score=true;


       //Gia to War
       for(int i=0; i<blocks; ++i)
       {
           for(int j=0; j<blocks; ++j)
           {
               if(Ken[j]>Naomi[i] && check_Ken[j])
               {
                    check_naomi_score=false;
                    check_Ken[j]=false;
                    break;
               }
           }

           if(check_naomi_score)
              ++naomi_war_score;

           check_naomi_score=true;
       }


       check_naomi_score=false;


       //Gia to Deceitful War
       for(int i=0; i<blocks; ++i)
       {
           for(int j=0; j<blocks; ++j)
           {
               if(Naomi[j]>Ken[i] && check_Naomi[j])
               {
                    check_naomi_score=true;
                    check_Naomi[j]=false;
                    break;
               }
           }

           if(check_naomi_score)
              ++naomi_deceitful_war_score;

           check_naomi_score=false;
       }


       results[pos].push_back(naomi_deceitful_war_score);
       results[pos].push_back(naomi_war_score);
       ++pos;

       naomi_war_score=0;
       naomi_deceitful_war_score=0;
   }

   fclose(stdin);



   for(int i=0; i<pos; ++i)
   {
       printf("Case #%d: %d %d\n",i+1,results[i][0],results[i][1]);
   }


   return 0;
}


