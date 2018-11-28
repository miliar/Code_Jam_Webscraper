#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <stack>
#include <queue>
#include <cstring>
#include <algorithm>
#include <vector>
#include <map>
using namespace std;

int c;
char input[101];
bool in[101];

int main()
{
        freopen ("B-small-attempt1.in","r",stdin);
        freopen ("out.txt","w",stdout);
        scanf("%d",&c);
     for(int i=0 ; i< c ;++i)
    {
        scanf("%s",&input);
        int l = strlen(input);
        memset(in,0,sizeof(in));
        for(int j =0; j<l;++j)
        {
            if(input[j]=='+')
            {
                in[j]=true;
            }
        }
        int cou=0;
        int d =0;
        int rn =l-1;

        while(d!=l)
        {
            if(in[rn])
            {
                rn--;
                d++;
            }
            else
            {
              /*  for(int j=0;j<l;j++)
                {
                    printf("%d",in[j]);
                }

                    printf("\n");
*/
                if(in[0])
                {
                    cou++;
                    int t =rn;

                   while(!in[rn])
                   {
                       rn--;
                   }
                 //  printf("swaphere");
                   for(int j=0 ; j < (rn/2)+1 ; j++ )
                   {
                       if(j!=rn-j){
                   //    printf("swap %d %d",j,rn-j);
                        swap(in[j],in[rn-j]);
                        in[j] = !in[j];
                        in[rn-j]= !in[rn-j];
                       }else
                       {
                       in[j]=!in[j];
                       }
                    }

                                       rn =t;
                }
                else
                {
                    cou++;
                    for(int j=0 ; j < (rn/2)+1 ; j++ )
                   {
                           if(j!=rn-j){
                   //    printf("swap %d %d",j,rn-j);
                        swap(in[j],in[rn-j]);
                        in[j] = !in[j];
                        in[rn-j]= !in[rn-j];
                       }else
                       {
                      //     printf("before %d ",in[j]);
                       in[j]=!in[j];

                      // printf("after %d ",in[j]);
                       }
                    }

                }
            }
        }
        printf("Case \#%d: %d\n",i+1,cou);

    }


        fclose (stdin);
        fclose (stdout);
return 0;
}
