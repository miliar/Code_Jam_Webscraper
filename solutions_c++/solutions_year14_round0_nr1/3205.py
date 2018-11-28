#include <cstdio>
#include <vector>

using namespace std;


int numbers[17];
int T,row,input_nums,pos_maxs,correct_values;
vector<int> output_res;
vector<int> all_pos_maxs;

int main()
{
   freopen("C:\\Users\\Hepic\\Desktop\\out.txt","r",stdin);

   scanf("%d",&T);

   while(T--)
   {
       for(int times=1; times<=2; ++times)
       {
           scanf("%d",&row);

           for(int i=1; i<=4; ++i)
           {
               for(int j=1; j<=4; ++j)
               {
                   scanf("%d",&input_nums);

                   if(row==i)
                     ++numbers[input_nums];
               }
           }
       }


       correct_values=0;

       for(int i=1; i<=16; ++i)
       {
           if(numbers[i]==2)
           {
                pos_maxs=i;
                ++correct_values;
           }
       }

       if(correct_values==1)
       {
           output_res.push_back(1);
           all_pos_maxs.push_back(pos_maxs);
       }

       else if(correct_values==0)
       {
           output_res.push_back(0);
           all_pos_maxs.push_back(-1);

       }

       else if(correct_values>1)
       {
           output_res.push_back(2);
           all_pos_maxs.push_back(-1);
       }

       for(int i=1; i<=16; ++i)
         numbers[i]=0;
   }


   for(int i=0; i<output_res.size(); ++i)
   {
       if(output_res[i]==1)
          printf("Case #%d: %d\n",i+1,all_pos_maxs[i]);

       else if(output_res[i]==0)
          printf("Case #%d: Volunteer cheated!\n",i+1);

       else if(output_res[i]==2)
          printf("Case #%d: Bad magician!\n",i+1);
   }

   fclose(stdin);


   return 0;
}


