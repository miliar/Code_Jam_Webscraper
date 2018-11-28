#include<bits/stdc++.h>
using namespace std;

char str[105];
int Len;

int Findlast()
{
     int i;
     for(i=Len-1; i>=0; i--){
          if(str[i]=='-')
            break;
     }
     return i;
}

int Findfirst()
{
     int i;
     for(i=0; i<Len; i++){
          if(str[i]!='+')
             break;
     }
     return i-1;
}

void flip(int k)
{
     //printf("Flipping till %d\n",k);
     int i;
     for(i=0; i<=(k/2); i++)
        swap(str[i],str[k-i]);

     for(i=0; i<=k; i++)
        str[i] = (char)(88 - str[i]);
     //puts(str);
}

int main()
{
       int T,it,i,j;
       freopen("B-large.in","r",stdin);
       freopen("B.out","w",stdout);

       scanf("%d",&T);
       for(it=1; it<=T; it++)
       {
             scanf("%s",str);
             Len=strlen(str);

             int ans=0;

             //printf("%d %d\n",Findlast(),Findfirst());

             while(true)
             {
                   int pos1 = Findlast();
                   //printf("pos1:%d\n",pos1);

                   if(pos1==-1)  break;

                   int pos2 = Findfirst();
                   //printf("pos2:%d\n",pos2);

                   if(pos2!=-1){

                        flip(pos2);
                        ans++;

                   }

                   flip(pos1);
                   ans++;
             }

             printf("Case #%d: %d\n",it, ans);
       }
       return 0;
}
