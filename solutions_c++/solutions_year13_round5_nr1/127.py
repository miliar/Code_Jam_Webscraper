#include<cstdio>
#include<iostream>
#include<sstream>
#include<cmath>
#include<algorithm>
#include<map>
#include<set>
#include<list>
#include<vector>
#include<stack>
#include<queue>
#include<string>
#include<iomanip>
#include<fstream>
#include<ctime>
using namespace std;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef pair <int,int> ii;
typedef long long LL;
#define pb push_back
const int INF = 2147483647;
const LL INFF = 1000000000000000LL;

int z,q,n,i;
LL tab[40],bat[40],b;
double res;

double policz () {
       LL minn = INFF;
       int i, f=0;
       double res = 0.0;
       for (i=0;i<37;i++) minn = min(minn, tab[i]+bat[i]);
       for (i=0;i<37;i++) if (tab[i]+bat[i]==minn) f++;
       for (i=0;i<37;i++) if (tab[i]+bat[i] == minn) res += (35.0/f) * bat[i] - (f-1)*1.0/f * bat[i];
       else res -= bat[i];
       return res;
}

double probuj (int a) {
       //printf("%d\n",a);
       LL pot = 0, d;
       double res = 0.0;
       int i,j;
       for (i=0;i<37;i++) {
           if (i<a) bat[i] = tab[a-1] - tab[i];
           else if (i>=a) {
                if (tab[i] == tab[a-1]) bat[i]=1; else bat[i]=0;
           }
           pot += bat[i];
       }
       j=a-1;
       for (i=a;i<37;i++) if (bat[i]>0) j=i;
       //if (a==33) cout << pot << endl;
       while (j<37) {
           if (tab[j+1] == tab[j] + bat[j]) {j++; continue;}
           if (pot > b) {j++; continue;}
           //if (a==33) printf(" %d\n",j);
           res = max(res, policz());
           d = (b - pot) / (j + 1);
           d = min(d, tab[j+1] - (tab[j]+bat[j]) - 1);
           //if (a==33) cout << d << " " << pot << endl;
           for (i=0;i<=j;i++) bat[i]+=d;
           pot += d * (j+1);
           res = max(res, policz());
           if (j!=36) {
              for (i=0;i<=j;i++) bat[i]++;
              pot += (j+1);
              while (tab[j+1] == tab[a-1]+bat[a-1]) {
                    j++;
                    bat[j]++;
                    pot++;
              }
           }
           else j++;
       }
       /*while (pot <= b) {
             res = max(res, policz());
             //cout << pot << " ";
             //printf("%.3lf\n",res);
             for (i=0;i<a;i++) {
                 bat[i]++;
                 pot++;
             }
             for (i=a;i<37;i++) if (tab[i]+bat[i]==tab[a-1]+bat[a-1]) {
                 bat[i]++;
                 pot++;
             }
       }*/
       //printf("%d %.3lf\n",a,res);
       return res;
}

int main() {
scanf("%d",&z);
for (q=1;q<=z;q++) {
    cin >> b >> n;
    for (i=0;i<n;i++) cin >> tab[i];
    for (i=n;i<37;i++) tab[i]=0;
    tab[37] = INFF;
    sort(tab,tab+37);
    res = 0.0;
    for (i=1;i<=37;i++) {
        res = max(res, probuj(i));
        //return 0;
    }
    printf("Case #%d: %.11lf\n",q,res);    
}
return 0;
}
