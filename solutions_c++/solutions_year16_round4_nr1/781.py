#include <iostream>
#include <cstdio>

using namespace std;

int t, p, r, s, pp, n, rr, ss;
string res, pe[5];
int up(int x){
  if (x == 1) {
   if (s == 0)return 0;
   s--;
   return 1;
  }
  if (x == 2) {
   if (p == 0)return 0;
   p--;
   return 1;
  }
  if (x == 3) {
   if (r == 0)return 0;
   r--;
   return 1;
  }
 
}


int rev(int x) {
 return x % 3 + 1; 
}
int check(int hod, int lev) {
 if (lev == n) {
   res += pe[hod];
   return 1;
 }  
 if (!up(hod)) return 0;
 

 if (pe[hod]>pe[rev(hod)] &&check(rev(hod), lev + 1) && check(hod, lev + 1)) return 1; else 
 if (pe[hod]<pe[rev(hod)] &&check(hod, lev + 1) && check(rev(hod), lev + 1)) return 1;
 
 return 0;
}
string back(int hod, int lev) {
 	if (lev == n) {
 		return pe[hod];
	}
	up(hod);
	string p1 = back(rev(hod), lev + 1);
	string p2 = back(hod, lev + 1);
	if (p1 > p2) swap(p1, p2);
	string ref = p1;
	ref += p2;
	return ref; //p1 + p2;
	
}
int main(){
 
 cin >> t;
 pe[1] = "R";
 pe[2] = "S";
 pe[3] = "P";
int qq = 1;
 while (t--) {
   cout << "Case #"<< qq<<": ";
        qq++;
	cin >> n >> r >> p >> s;
   rr = r, pp = p, ss = s;
   p--;
   res= "";
   if (p >= 0 && check(3, 0)) {
     r = rr, p = pp, s = ss;
     cout << back(3, 0) << endl;

     continue;
   }     

   res= "";
   r = rr, p = pp, s = ss;
   r--;
   if (r >= 0 && check(1, 0)) {
     r = rr, p = pp, s = ss;
     cout << back(1,0) << endl;	

     continue;
   }
   res = "";
   
   r = rr, p = pp, s = ss;
   s--;
   if (s >= 0 && check(2, 0)) {
        r = rr, p = pp, s = ss;
   	cout << back(2, 0) << endl;

	continue;
   }
   res= "";

   cout << "IMPOSSIBLE" << endl;
   
  
 }
 return 0;
}