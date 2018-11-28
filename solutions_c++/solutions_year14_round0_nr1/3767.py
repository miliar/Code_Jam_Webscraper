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

        int t;
        scanf("%d",&t);

        int arr1[4][4];
        int arr2[4][4];

        int cases=0;
        while(t--)
        {
            int ans1,ans2;
            scanf("%d",&ans1);
            for(int i=0;i<4;i++)
            {
                for(int j=0;j<4;j++)
                {
                    scanf("%d",&arr1[i][j]);
                }
            }

            scanf("%d",&ans2);
            for(int i=0;i<4;i++)
            {
                for(int j=0;j<4;j++)
                {
                    scanf("%d",&arr2[i][j]);
                }
            }


            int ans_arr1[4];
            int ans_arr2[4];
            for(int j=0;j<4;j++)
            {
                ans_arr1[j]=arr1[ans1-1][j];
                ans_arr2[j]=arr2[ans2-1][j];
            }

            vector<int>ans;
            ans.clear();
            for(int j=0;j<4;j++)
            {
                for(int k=0;k<4;k++)
                {
                    if(ans_arr1[j]==ans_arr2[k])
                    {
                        ans.push_back(ans_arr1[j]);
                        break;
                    }
                }
            }

            printf("Case #%d: ",++cases);
            if(ans.size()==1)
            {
                printf("%d\n",ans[0]);
            }
            else if(ans.size()>1)
            {
                printf("Bad magician!\n");
            }
            else if(ans.size()==0)
            {
                printf("Volunteer cheated!\n");
            }


        }



		return 0;
}


