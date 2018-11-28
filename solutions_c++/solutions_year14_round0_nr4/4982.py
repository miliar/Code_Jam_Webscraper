#include<stdio.h>
#include<algorithm>

using namespace std;
 long long int arr[100005];
 double aap[100005];
    double boob[100005];
    long long aapchutiyehwayai[1000008];
    long long kandhwaychutiya[1000007];
    
int main()
{
   
    long long int j,l,chaddi,kachha,nude,muth,testis,counter;
    long long int kandy,lund;
    
    
                                                                                                                                                                                                                                                     scanf("%lld",&testis);
    freopen("ques4.txt","w",stdout);
    
    
    
    for(counter=1;counter<=testis;counter++) {scanf("%lld",&nude);
                      for(j=0;j<nude;j++)
                      scanf("%lf",&aap[j]);
                      for(j=0;j<nude;j++)
                      scanf("%lf",&boob[j]);
                      sort(boob,boob+nude);
                      sort(aap,aap+nude);
                      muth=kandy = 0;
                      lund = nude-1;
                      for(j = nude-1; j>=0;j--) {
                            if(boob[j]>aap[lund]) {
                                          muth++;
                            }
                            else
                            {
                                kandy++;
                                lund--;
                            }
                      }
                      int o,po;
                      po=o=0;
                      for(int far=0;far<=1000000;far++) 
                      {
                              o++;
                              po--;
                      }
                      int go;
                      if(o==po)
                      go=8;
                      else
                      go=9;
                      int u;
                      if(go==9)
                      u = 65465;
                      else
                      u=464;
                      chaddi=kandy;
                      kandy=0;
                      lund=0;
                      for(j=0;j<nude;j++)
                      arr[j] = 0;
                      
                      
                      for(j=0;j<nude;j++) 
                      {
                                       for(lund=0;lund<nude;lund++) 
                                       {
                                                        if(arr[lund]==0&&aap[j]<boob[lund]) 
                                                        {
                                                                  arr[lund]=1;
                                                                  kandy++;
                                                                  break;
                                                        }
                                       }
                      }
                      
                      
                      kachha = nude-kandy;
                                                                                                                                                                                                                                                                                                                                                        printf("Case #%lld: %lld %lld\n",counter,chaddi,kachha);
    }
    return 0;
}
