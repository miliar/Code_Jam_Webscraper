#include <bits/stdc++.h>
using namespace std;

int t, n, p[]={2, 3, 5, 7, 11, 13, 17, 19,
               23, 29, 31, 37, 41, 43, 47,
               53, 59, 61, 67, 71, 73, 79,
               83, 89, 97, 101, 103, 107, 109,
               113, 127, 131, 137, 139, 149, 151,
               157, 163, 167, 173, 179, 181, 191, 193, 197, 199};
int mod[100], sv[100];

int power(int a, int b, int c){
  int r=1;
  while (b){
    if (b%2) r*=a;
    a*=a;
    r%=c;
    a%=c;
    b>>=1;
  }
  return r;
}

int main(){
  n=32;
  int all=500;
  //cin >> n;
  n-=2;

  int sz = sizeof(p)/sizeof(int);
  puts("Case #1:");
  for (int mask=1,col; mask<(1<<n); mask++){

     if (!all) break;
     col=0;
     for (int num=2; num<=10; num++) {
         memset(mod, 0, sizeof mod);
         for (int k=0; k<sz; k++){
         mod[k]+=1;
         mod[k]+=power(num, n+1, p[k]);
        // cout << "mod " << mod[k] << " " << p[k] << endl;
         mod[k]%=p[k];
           int sn = num%p[k];
           for (int j=0; j<n; j++)
            {
             if (mask&(1<<j)) mod[k]=(mod[k]+sn)%p[k];
             sn*=num;
             sn%=p[k];
            }
         }
         bool fake=false;
         for (int k=0; k<sz; k++) if (mod[k]==0) fake=true, sv[num]=p[k], k=sz+1;
         if (fake) col++;
       //  cout << num << " " << fake << endl;
     }
     if (col==9){
        cout << 1;
        for (int j=n-1; j>=0; j--) cout << (mask&(1<<j) ? 1 : 0);
        cout << "1 ";
        for (int i=2; i<=9; i++) cout << sv[i] << " ";
        cout << sv[10] << endl;
        all--;
     }
     //break;

  }

}
