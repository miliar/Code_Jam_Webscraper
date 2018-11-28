#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <string>

using namespace std;

void printMat(vector< vector<int> > A) {
   for(int i = 0; i < 4; i++) {
      for(int j = 0; j < 4; j++) {
         printf("%d ", A[i][j]);
      } printf("\n");
   }
}

vector< vector<int> > ikj(vector< vector<int> > A,
         vector< vector<int> > B) {
   vector< vector<int> > C;
   C.assign(4, vector<int>());
   for(int i = 0; i < 4; i++)
      C[i].assign(4,0);;
   int i,j,k;
   for(i = 0; i < 4; i++)
      for(j = 0; j < 4; j++)
         for(C[i][j] = k = 0; k < 4; k++)
            C[i][j] += A[i][k]*B[k][j];
   return C;
}

vector< vector<int> > fast_exp(vector< vector<int> > A, long long int n) {
   vector< vector<int> > ANS;
   ANS.assign(4, vector<int>());
   for(int i = 0; i < 4; i++)
      ANS[i].assign(4,0);;
   for(int i = 0; i < 4; i++)
      for(int j = 0; j < 4; j++)
         ANS[i][j] = (i==j);
   while(n) {
      if(n & 1) ANS = ikj(ANS,A);
      A = ikj(A,A);
      n >>= 1;
   }
   return ANS;
}

vector< vector<int> > inverse(vector< vector<int> > A) {
   bool equals = true;
   for(int i = 0; i < 4; i++)
      for(int j = 0; j < 4; j++)
         if(A[i][j] != (i==j))
            equals = false;
   if(!equals) {
      vector< vector<int> > Ainv;
      Ainv.assign(4, vector<int>());
      for(int i = 0; i < 4; i++)
         Ainv[i].assign(4,0);
      for(int i = 0; i < 4; i++)
         for(int j = 0; j < 4; j++)
            Ainv[i][j] = -A[i][j];
      return Ainv;
   }
   return A;
}

int main() {
   vector< vector<int> > I, J, K, IJK, ID, ANS;

   I.assign(4, vector<int>());
   J.assign(4, vector<int>());
   K.assign(4, vector<int>());
   IJK.assign(4, vector<int>());
   ID.assign(4, vector<int>());
   ANS.assign(4, vector<int>());

   for(int i = 0; i < 4; i++) {
      I[i].assign(4,0);
      J[i].assign(4,0);
      K[i].assign(4,0);
      IJK[i].assign(4,0);
      ID[i].assign(4,0);
      ANS[i].assign(4,0);
   }

   for(int i = 0; i < 4; i++)
      for(int j = 0; j < 4; j++)
         ID[i][j] = (i==j);

   for(int i = 0; i < 4; i++)
      for(int j = 0; j < 4; j++)
         ANS[i][j] = (i==j);

   for(int i = 0; i < 4; i++)
      for(int j = 0; j < 4; j++)
         IJK[i][j] = -(i==j);

   I[0][0] = 0; I[0][1] = 1; I[0][2] = 0; I[0][3] = 0;
   I[1][0] = -1; I[1][1] = 0; I[1][2] = 0; I[1][3] = 0;
   I[2][0] = 0; I[2][1] = 0; I[2][2] = 0; I[2][3] = -1;
   I[3][0] = 0; I[3][1] = 0; I[3][2] = 1; I[3][3] = 0;
   
   J[0][0] = 0; J[0][1] = 0; J[0][2] = 1; J[0][3] = 0;
   J[1][0] = 0; J[1][1] = 0; J[1][2] = 0; J[1][3] = 1;
   J[2][0] = -1; J[2][1] = 0; J[2][2] = 0; J[2][3] = 0;
   J[3][0] = 0; J[3][1] = -1; J[3][2] = 0; J[3][3] = 0;

   K[0][0] = 0; K[0][1] = 0; K[0][2] = 0; K[0][3] = 1;
   K[1][0] = 0; K[1][1] = 0; K[1][2] = -1; K[1][3] = 0;
   K[2][0] = 0; K[2][1] = 1; K[2][2] = 0; K[2][3] = 0;
   K[3][0] = -1; K[3][1] = 0; K[3][2] = 0; K[3][3] = 0;

   map<char, vector< vector<int> > > mat;
   mat['i'] = I;
   mat['j'] = J;
   mat['k'] = K;

   int T, L, X;
   bool equals, found;
   set<char> dijkstra;
   string product, ins;
   map<int, vector< vector<int> > > hash;
   map<int, vector< vector<int> > > hash_reverse;
   vector< vector<int> > ini, med, fin;
   scanf("%d\n", &T);
for(int kase = 1; kase <= T; kase++) {
   for(int i = 0; i < 4; i++)
      for(int j = 0; j < 4; j++)
         ANS[i][j] = (i==j);
   dijkstra.clear();
   hash.clear();
   hash_reverse.clear();
   found = false;
   scanf("%d %d\n", &L, &X);
   cin >> product;
   ins = product;
   for(int i = 0; i < X-1; i++)
      product += ins;
   L = (int)product.size();
   for(int i = 0; i < L; i++) {
      ANS = ikj(ANS,mat[product[i]]);
      hash[i] = ANS;
   }
   for(int i = 0; i < (int)ins.size(); i++)
      dijkstra.insert( product[i] );
   printf("Case #%d: ", kase);
   equals = true;
   for(int i = 0; i < 4; i++)
      for(int j = 0; j < 4; j++)
         if(ANS[i][j] != IJK[i][j])
            equals = false;
   if(L < 3) equals = false;
   if(equals) {
      for(int i = 0; i < 4; i++)
         for(int j = 0; j < 4; j++)
            ANS[i][j] = (i==j);
      for(int i = L-1; i >= 0; i--) {
         ANS = ikj(mat[product[i]],ANS);
         hash_reverse[i] = ANS;
      }
      for(int i = 0; i <= L-3; i++) {
         if(found) break;
         for(int j = i+2; j <= L-1; j++) {
            // range [0,i], [i+1,j], [j+1,L-1]
            if(found) break;
            med = ikj(inverse(hash[i]),ikj(hash[L-1],inverse(hash_reverse[j])));
            if(hash[i] == I and med == J and hash_reverse[j] == K)
               found = true;
         }
      }
      if(found)
         printf("YES\n");
      else
         printf("NO\n");
   }
   else
      printf("NO\n");
}
   return 0;
}
