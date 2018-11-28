#include <cstdio>
#include <cstdlib>
int a[200][200], mxr[200], mxc[200];
int max(int a, int b){
   return a>b?a:b;
}
int main(){
   int n, m, T, kl = 1;
   FILE *fi = fopen("sec.in", "r");
   fscanf(fi, "%d", &T);
   FILE *fo = fopen("sout.in", "w");
   while(T--){
      fscanf(fi, "%d%d", &n, &m);
      
      for (int i = 0; i!=200; i++)mxc[i] = mxr[i] = 0;
      for (int i = 0; i!=n; i++){
         for (int j = 0; j!=m; j++){
            fscanf(fi, "%d", &a[i][j]);
            mxr[i] = max(a[i][j], mxr[i]);
            mxc[j] = max(a[i][j], mxc[j]);
         }
      }
      bool found = false;
      for (int i = 0; i!=n; i++){
         for (int j = 0; j!=m; j++){
            if (a[i][j] < mxc[j] && mxr[i] > a[i][j]) found = true;
         }
      }
      if (found) fprintf(fo, "Case #%d: NO\n", kl);
      else fprintf(fo, "Case #%d: YES\n", kl);
      kl++;
   }
   system("pause");
}
   
   
