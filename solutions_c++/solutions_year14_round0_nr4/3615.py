#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string.h>
using namespace std;


int main() 
{

        freopen ("input.txt","r",stdin);
        freopen ("output.txt","w",stdout);


        int t,cases=0;
        scanf("%d",&t);

        while(t--)
        {
            int N;
            scanf("%d",&N);

            long double arr1[1009];
            long double arr2[1009];

            for(int i=0;i<N;i++)
                scanf("%Lf",&arr1[i]);

            for(int i=0;i<N;i++)
                scanf("%Lf",&arr2[i]);
            
            int flag1[1009];
            int flag2[1009];

            for(int i=0;i<N;i++)
            {
                flag1[i]=1;
                flag2[i]=1;
            }

            sort(arr1,arr1+N);
            sort(arr2,arr2+N);
            
            int ans2=0;
            int count=0;
            for(int i=0;i<N;i++)
            {
                if(flag1[i] != 0)
                {
                    for(int j=0;j<N;j++)
                    {
                        if(flag2[j] != 0)
                        {
                            if(arr2[j]>arr1[i])
                            {
                                flag1[i]=flag2[j]=0;
                                ++count;
                                break;
                            }
                        }
                    }
                }
            }


            ans2=N-count;

            
            int ans1=0;
            for(int i=0;i<N;i++)
            {
                flag1[i]=1;
                flag2[i]=1;
            }
            

            
            while(1)
            {
                count=0;
                for(int i=0;i<N;i++)
                {
                    if(flag2[i] == 1) ++count;
                }

                if(count == 1) break;
                int count2=0;

                int to_be_removed=0;
                int index=-1;
                for(int i=0;i<N;i++)
                {
                    count2=0;
                    for(int j=0;j<N;j++)
                    {
                        if(arr1[i] < arr2[j]&& flag2[j] ==1 && flag1[i] == 1) ++count2;
                    }
                    if(count2==count && count != 0)
                    {
                        to_be_removed=1;
                        index=i;
                        break;

                    }
                }

                if(index == -1) break;


                if(index != -1)
                {
                    
                       int found=0;
                       for(int j=N-1;j>=0;j--)
                       {
                           if(flag2[j] == 1 && arr2[j] > arr1[index])
                           {
                                for(int k=0;k<N;k++)
                                {
                                    if(flag1[k] == 1 && arr1[k] > arr1[index])
                                    {
                                        
                                        found=1;
                                        flag2[j]=0;
                                        flag1[index]=0;
                                        break;
                                    }
                                }

                                if(found) break;
                           }
                       }

                }
            }


            /*
            for(int i=0;i<N;i++)
            {
               printf("arr1 %Lf flag1 = %d arr2 %Lf flag2 = %d\n", arr1[i], flag1[i], arr2[i],flag2[i]);
            }
            */

            
            for(int i=N-1;i>=0;i--)
            {
                if(flag1[i] == 1)
                {
                    for(int j=N-1;j>=0;j--)
                    {
                        if(flag2[j]==1 && arr1[i] > arr2[j])
                        {
                            flag1[i]=0;
                            flag2[j]=0;
                            ++ans1;
                            break;
                        }
                    }
                }
            }




            printf("Case #%d: %d %d\n",++cases,ans1,ans2);
        }




		return 0;
}


