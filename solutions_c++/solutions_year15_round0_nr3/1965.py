#include <bits/stdc++.h>
using namespace std;
struct str{
 string pr, dr;
 bool operator < (const struct str &p) const{
  if (pr < p.pr) return 1;
  if (pr == p.pr && dr < p.dr) return 1;
  return 0;
 }
}pom;

int niz[10500];
map <str, string> m;
string s, s1, s2;
int l, x, t, flag;

void Set(string s1, string s2, string s3)
{
  str ss;
  ss.pr = s1;
  ss.dr = s2;
  m[ss] = s3;
}

void make1()
{
/* 1 */
  Set("1", "1", "1");
  Set("-1", "1", "-1");
  Set("1", "-1", "-1");
  Set("-1", "-1", "1");
  Set("1", "i", "i");
  Set("-1", "i", "-i");
  Set("1", "-i", "-i");
  Set("-1", "-i", "i");
  Set("1", "j", "j");
  Set("-1", "j", "-j");
  Set("1", "-j", "-j");
  Set("-1", "-j", "j");
  Set("1", "k", "k");
  Set("-1", "k", "-k");
  Set("1", "-k", "-k");
  Set("-1", "-k", "k");
}

void make2()
{
  Set("i", "1", "i");
  Set("-i", "1", "-i");
  Set("i", "-1", "-i");
  Set("-i", "-1", "i");

  Set("i", "i", "-1");
  Set("-i", "i", "1");
  Set("i", "-i", "1");
  Set("-i", "-i", "-1");

  Set("i", "j", "k");
  Set("-i", "j", "-k");
  Set("i", "-j", "-k");
  Set("-i", "-j", "k");

  Set("i", "k", "-j");
  Set("-i", "k", "j");
  Set("i", "-k", "j");
  Set("-i", "-k", "-j");
}

void make3()
{
  Set("j", "1", "j");
  Set("-j", "1", "-j");
  Set("j", "-1", "-j");
  Set("-j", "-1", "j");

  Set("j", "i", "-k");
  Set("-j", "i", "k");
  Set("j", "-i", "k");
  Set("-j", "-i", "-k");

  Set("j", "j", "-1");
  Set("-j", "j", "1");
  Set("j", "-j", "1");
  Set("-j", "-j", "-1");

  Set("j", "k", "i");
  Set("-j", "k", "-i");
  Set("j", "-k", "-i");
  Set("-j", "-k", "i");
}

void make4()
{
  Set("k", "1", "k");
  Set("-k", "1", "-k");
  Set("k", "-1", "-k");
  Set("-k", "-1", "k");

  Set("k", "i", "j");
  Set("-k", "i", "-j");
  Set("k", "-i", "-j");
  Set("-k", "-i", "j");

  Set("k", "j", "-i");
  Set("-k", "j", "i");
  Set("k", "-j", "i");
  Set("-k", "-j", "-i");

  Set("k", "k", "-1");
  Set("-k", "k", "1");
  Set("k", "-k", "1");
  Set("-k", "-k", "-1");
}

int main()
{
 //freopen("t.in", "r", stdin);
 //freopen("t.out", "w", stdout);
 make1();
 make2();
 make3();
 make4();
 //ios_base::sync_with_stdio (false);

 scanf("%d", &t);
  int wl = 0;
 // t = 10;
  while (t--){
   wl++;
   flag = 0;
   scanf("%d%d", &l, &x);
   int ll = l;
   cin >> s;
   s1 = "";
   int i;
   for (i=1; i<=x; i++)
    s1 = s1 + s;

   l = l*x;
   int aa = 0;
   int pp = max(0, l-4*ll-1);
   memset(niz, 0, sizeof(niz));

   for (i=(l-1); i>=pp; i--)
   {
    if (i == (l-1)){
      s = s1[i];
    }
    else{
     pom.pr = s1[i];
     pom.dr = s;
     s = m[pom];
    }

    if (s == "k") {
      niz[i] = 1;
      if (aa == 0)
        aa = i+1;
    }
   // cout << niz[i];
   }

   if (aa != 0){
   pp = min(l, 4*ll+1);
   for (i=0; i<pp; i++)
   {
  //   cout << i << endl;
     if (i == 0){
       s = s1[0];
     }
     else{
      pom.pr = s;
      pom.dr = s1[i];
      s = m[pom];
     }
      int bp = 0;
      int bk = 0;

     if (s == "i")
     {
      // cout << i << endl;
       string s2 = "";
       for (int j=(i+1); j<aa; j++)
       {
         if (j == (i+1)){
           s2 = s1[j];
         }
         else{
          pom.pr = s2;
          pom.dr = s1[j];
          s2 = m[pom];
         }
         if (s2 == "j" && niz[j+1] == 1){
           flag = 1;
           break;
         }
       }
     }
     if (flag == 1) break;
   }
   }
   printf("Case #%d: ", wl);
   if (flag == 1){
    printf("YES\n");
   }
   else
    printf("NO\n");
  }
}
