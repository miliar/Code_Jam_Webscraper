#include<cstdio>

#define ll long long

ll palindrom;
ll square;
int pal[20];

bool is_ok(ll x){
     int arr[50],len;
     len=0;
     while(x>0){
         arr[len++]=x%10;
         x/=10;           
     }
     int i;
     for(i=0;i<len;i++){
         if(arr[i]!=arr[len-i-1]) break;                   
     }    
     if(i==len) return true;
     return false;
}

ll pal1(ll x){
   int arr[50],len;
   len=0;
   while(x>0){
     arr[len++]=x%10;
     x/=10;           
   }
   int i;
   for(i=len;i<2*len;i++){
     arr[i]=arr[2*len-i-1];
   }
   ll ans=0;
   for(i=0;i<2*len;i++){
     ans=ans*10+arr[i];
   }
   return ans;
}

ll pal2(ll x){
   int arr[50],len;
   len=0;
   while(x>0){
     arr[len++]=x%10;
     x/=10;           
   }
   int i;
   for(i=len-1;i<2*len-1;i++){
     arr[i]=arr[2*len-i-2];
   }
   ll ans=0;
   for(i=0;i<2*len-1;i++){
     ans=ans*10+arr[i];
   }
   return ans;
}

int main(){
    FILE *fin,*fout;
    fin = fopen("C-small-attempt1.in","r");
    fout = fopen("C-small-attempt1.out","w");
    int T,t;
    int A,B;
    int len,i,j;
    ll ans;
    
    fscanf(fin,"%d",&T);
    t=0;
    while(++t<=T){
      ans = 0;
      fscanf(fin,"%d%d",&A,&B);
      for(i=1;i<10;i++){
        palindrom = pal1(i);
        square=palindrom*palindrom;
        if(A<=square && square<=B && is_ok(square)) ans++;
        palindrom = pal2(i);
        square=palindrom*palindrom;
        if(A<=square && square<=B && is_ok(square)) ans++;
      }
      fprintf(fout,"Case #%d: %lld\n",t,ans);
                
    }
    
//    while(getchar()!='k');
    return 0;
}
    
