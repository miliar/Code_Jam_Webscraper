#include<cstdio>
#include<string>
#include<iostream>

using namespace std;
char a[10][10];
int b[10][10],c[10][10],n;

int main(){
    
    freopen( "A-small-attempt1.in", "r", stdin );
    freopen(  "output.txt", "w", stdout );
   
   scanf("%d", &n);
   for(int k=0; k<n;  k++) {
           
           for(int i=0; i<4; i++)
           for(int j=0; j<4; j++){
                   b[i][j]=0;
                   c[i][j]=0;
                   }
    
    
  for(int i=0; i<4; i++)
          scanf("%s", a[i]);
    
    int d1=0,d2=0,s=0,dd1=0,dd2=0;
    
    for(int i=0; i<4; i++)
    for(int j=0; j<4; j++){
            if(a[i][j]=='X' || a[i][j]=='T') {b[i][0]++; b[j][1]++;}
             if(a[i][j]=='O' || a[i][j]=='T' ) {c[i][0]++; c[j][1]++;}
             if(i==j && (a[i][j]=='X' || a[i][j]=='T')) d1++;
             if(i+j==3 && (a[i][j]=='X' || a[i][j]=='T')) dd1++;
              if(i+j==3 && (a[i][j]=='O' || a[i][j]=='T')) dd2++; 
             if(i==j && (a[i][j]=='O' || a[i][j]=='O')) d2++; 
             if(a[i][j]!='.') s++;}
    
 
      
      int z1=0, z2=0;      
    for(int i=0; i<4; i++)
    for(int j=0; j<2; j++){
            if(b[i][j]==4) z1=1;
            if(c[i][j]==4) z2=1;
            if(d1==4) z1=1;
            if (d2==4) z2=1;
            if(dd1==4) z1=1;
            if (dd2==4) z2=1;
}        
     
       if(z1==1) printf("Case #%d: X won\n",k+1);
      else if(z2==1) printf("Case #%d: O won\n",k+1);
      else if(s==16) printf("Case #%d: Draw\n",k+1);
      else printf("Case #%d: Game has not completed\n",k+1);
          
}            
       
    return 0;
    
}
            
