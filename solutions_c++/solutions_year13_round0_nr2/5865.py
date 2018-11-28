/*
ID: ankitgu1
LANG: C++
TASK: holstein
*/
#include <iostream>
#include <fstream>
#include <cstring>
#include <string>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>

using namespace std;

FILE *in,*out;

#define MAX(a,b) ((a)>(b)?(a):(b))

typedef long long LL;
typedef long L;

int is_prime(long long num){
    for(long long t=2;t<=sqrt(num);t++){
    if(num%t==0)return 0;
    }return 1;
}
LL gcd(LL a,LL b){
    if(a%b==0)return b;
    return gcd(b,a%b);
}
int compare (const void * a, const void * b)
{
    return ( *(int*)a - *(int*)b );
}
int dec_compare (const void * a, const void * b)
{
    return ( - *(int*)a + *(int*)b );
}
//////////////////////////

int arr[110][110];
int top[110][110];
int lef[110][110];
int rig[110][110];
int down[110][110];

int main(){
    in=fopen("input.in","r");
    out=fopen("output.in","w");
    int cases;
    fscanf(in,"%d",&cases);
    for(int test=0;test<cases;test++){
        memset(top,0,sizeof(top));
        memset(rig,0,sizeof(rig));
        memset(down,0,sizeof(down));
        memset(lef,0,sizeof(lef));

        //cout<<"case no "<<test+1<<endl<<endl;

        int y,x;fscanf(in,"%d %d",&y,&x);
        for(int yy=0;yy<y;yy++)
        for(int xx=0;xx<x;xx++)
        fscanf(in,"%d",&arr[yy][xx]);
//
//        for(int yy=0;yy<y;yy++){
//        for(int xx=0;xx<x;xx++)
//        cout<<arr[yy][xx]<<" ";
//        cout<<endl;
//        }cout<<endl;

        //int test;cin>>test;
      //  getchar();

      for(int yy=1;yy<y;yy++){
        for(int xx=0;xx<x;xx++){
            top[yy][xx]=MAX(top[yy-1][xx],arr[yy-1][xx]);
        }
      }
      for(int yy=1;yy<y;yy++){
        for(int xx=0;xx<x;xx++){
            down[y-1-yy][xx]=MAX(down[y-yy][xx],arr[y-yy][xx]);
        }
      }
      for(int yy=0;yy<y;yy++){
        for(int xx=1;xx<x;xx++){
            lef[yy][xx]=MAX(lef[yy][xx-1],arr[yy][xx-1]);
        }
      }
      for(int yy=0;yy<y;yy++){
        for(int xx=1;xx<x;xx++){
            rig[yy][x-1-xx]=MAX(rig[yy][xx-1],arr[yy][xx-1]);
        }
      }
        int pos = 1;
        for(int yy=0;yy<y;yy++){
            int done=0,temp=0;
            for(int xx=0;xx<x;xx++){
//                if(yy)top=maxi[xx];
//                if(xx)left=temp;
//                if(yy<y-1)down=arr[yy+1][xx];
//                if(xx<x-1)right=arr[yy][xx+1];

               // cout<<yy<<" "<<xx<<" "<<num<<" "<<top<<" "<<right<<" "<<down<<" "<<left<<endl;
               int num=arr[yy][xx];
                if((num<rig[yy][xx] && num<top[yy][xx])||(num<top[yy][xx] && num<lef[yy][xx])||(num<lef[yy][xx] && num<down[yy][xx])||(num<down[yy][xx] && num<rig[yy][xx])){
                    done=1;pos=0;break;
                }//maxi[xx]=MAX(maxi[xx],num);
                //temp=MAX(temp,num);
            }if(done)break;
        }
        fprintf(out,"Case #%d: ",test+1);
        if(pos)fprintf(out,"YES\n");
        else fprintf(out,"NO\n");
    }
    return 0;
}
