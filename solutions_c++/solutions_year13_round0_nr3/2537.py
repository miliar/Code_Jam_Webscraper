#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cassert>
#include <climits>
#include <ctime>
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <algorithm>
#include <vector>
#include <deque>
#include <list>
#include <queue>
#include <set>
#include <map>
#include <limits>
#include <cstring>
using namespace std;
long long rev(unsigned long long int x)
{
     unsigned long long int r=0,d;
     while(x>0)
     {
               d=x%10;
               r=r*10+d;
               x=x/10;
     }
     return r;
}

bool pal(unsigned long long int x)
{
     long long y=rev(x);
     if(x==y)
     return 1;
     return 0;
}
int main()
{

     int t,k=0,cases=0,c1,c2;
     unsigned long long int j,ar[100],a,b;//C-large-1.in
     ifstream ifs;
     ofstream ofs;
     ifs.open("C-large-1(1).in");
     ofs.open("ou.txt");
     //freopen("C-small-attempt0","r",stdin);
     //freopen("c.txt","w",stdout);//100000000000001
 /*   for(unsigned long long int i=1;i<100000000000001;i++)
     {
             if(pal(i))
             {

                                j=i*i;
                                if(pal(j))
                                ar[k++]=j;

             }
     }
     */

     unsigned long long int temp[]={1,
                                        4,
                                        9,
                                        121,
                                        484,
                                        676,
                                        10201,
                                        12321,
                                        14641,
                                        40804,
                                        44944,
                                        69696,
                                        94249,
                                        698896,
                                        1002001,
                                        1234321,
                                        4008004,
                                        5221225,
                                        6948496,
                                        100020001,
                                        102030201,
                                        104060401,
                                        121242121,
                                        123454321,
                                        125686521,
                                        400080004,
                                        404090404,
                                        522808225,
                                        617323716,
                                        942060249,
                                        10000200001,
                                        10221412201,
                                        12102420121,
                                        12345654321,
                                        40000800004,
                                        637832238736,
                                        1000002000001,
                                        1002003002001,
                                        1004006004001,
                                        1020304030201,
                                        1022325232201,
                                        1024348434201,
                                        1086078706801,
                                        1210024200121,
                                        1212225222121,
                                        1214428244121,
                                        1230127210321,
                                        1232346432321,
                                        1234567654321,
                                        1615108015161,
                                        4000008000004,
                                        4004009004004,
                                        4051154511504,
                                        5265533355625,
                                        9420645460249,
                                        100000020000001,
                                        100220141022001,
                                        102012040210201,
                                        102234363432201,
                                        121000242000121,
                                        121242363242121,
                                        123212464212321,
                                        123456787654321,
                                        123862676268321,
                                        144678292876441,
                                        165551171155561,
                                        400000080000004,
                                        900075181570009};

   // printf("%llu\n\n",temp[67]+1);

    for(unsigned long long int i=0;i<68;i++)
     {
                                j=sqrt(temp[i]);
                                if(pal(j))
                                {


                                ar[k++]=j*j;
                                        //ar[i]=temp[i];
                                        //printf("%llu\n",ar[k-1]);
                                }



     }
    //printf("%d\n\n",k);
    ifs>>t;
     //scanf("%d",&t);
     while(t--)
     {
               cases++;
               ofs<<"Case #"<<cases<<": ";
               ifs>>a>>b;
               //printf("Case #%d: ",cases);
               //scanf("%llu%llu",&a,&b);
              // if(a>ar[k-1])
               //{printf("0\n");continue;}
               //if(b>ar[k-1])
              // b=ar[k-1];
               int cnt=0;
               for(int i=0;i<k;i++)
               {
                       if(ar[i]>=a&&ar[i]<=b)
                       cnt++;
                       if(ar[i]>b)
                       break;
               }
               ofs<<cnt<<endl;

     }
}
