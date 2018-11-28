#include<bits/stdc++.h>
using namespace std;
char str[50];

void test(int base)
{
      int div = base+1;
      int i,rem=0;
      int mult=1;

      for(i=0; i<32; i++){
             if(str[i]=='1'){
                rem = (rem+mult)%div;
             }
             mult = (mult*base)%div;
      }
      if(rem!=0){
          puts("ERROR!");
      }
}

void doit(vector<int>pos)
{
      int i,j;
      for(i=0; i<32; i++)  str[i]='0';
      str[32]='\0';
      str[0]=str[31]='1';
      for(i=0; i<pos.size(); i++)
          str[pos[i]]='1';

//      if(pos.size()>4){
//      printf("%s\n",str);
//      for(i=2; i<=10; i++)
//          test(i);
//      }
      printf("%s",str);
      for(i=2; i<=10; i++)  printf(" %d",i+1);
      puts("");
}


int main()
{
      int i,j,cnt2=0, cnt4=0,cnt8=0;
      int T,J,N;
      freopen("C-large.in","r",stdin);
      freopen("write.out","w",stdout);

      scanf("%d",&T);
      scanf("%d%d",&N,&J);

      printf("Case #1:\n");

      for(i=1; i<=30; i++){
          for(j=i+1; j<=30; j+=2){
            //   printf("i:%d j:%d\n",i,j);
               vector<int>V;
               V.push_back(i);V.push_back(j);
               doit(V);
               cnt2++;
               J--;
               if(J==0) return 0;
          }
      }
    //  printf("cnt2:%d\n",cnt2);

      for(i=1; i<=30; i++){

           for(j=i+2; j<=29; j+=2){
               //  printf("i:%d j:%d\n",i,j);
                 vector<int>V;
                 V.push_back(i);V.push_back(i+1);
                 V.push_back(j);V.push_back(j+1);
                 doit(V);
                 cnt4++;
                 J--;
                 if(J==0) return 0;
           }
      }

   //   printf("cnt4:%d\n",cnt4);

      for(i=1; i<=30; i++){

           for(j=i+3; j<=28; j+=2){

                   //printf("i:%d j:%d\n",i,j);
                   vector<int>V;
                   V.push_back(i);V.push_back(i+1);V.push_back(i+2);
                   V.push_back(j);V.push_back(j+1);V.push_back(j+2);
                   doit(V);
                   cnt8++;
                   J--;
                   if(J==0) return 0;
           }
      }

      //printf("cnt8:%d\n",cnt8);

      return 0;
}
