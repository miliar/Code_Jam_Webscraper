 #include <bits/stdc++.h>
 using namespace std;
 
 map<string, int> computed;
 
 int tryit(vector<int> nplates);
 int trylow(vector<int> nplates);
 int trydivide(vector<int> nplates, int pos);
 
 string vet2string (vector<int> vet) {
     string str;
     for (int i = 0; i < vet.size(); i++) {
         while (vet[i] != 0) {
             str.push_back((char)(vet[i]%10+'0'));
             vet[i] /= 10;
         }
         str.push_back(',');
     }
     return str;
 }
 int main(int argc, char** argv) {
     int tests;
     cin >> tests;
     for (int test = 1; test <= tests; test++) {
         int dinners;
         vector<int> nplates;
         cin >> dinners;
         for (int i = 0; i < dinners; i++) {
             int in;
             cin >> in;
             nplates.push_back(in);
         }
         
         cout << "Case #" << test << ": " << tryit(nplates) << endl;
     }
     return 0;
 }
 
 int tryit(vector<int> nplates) {
     sort(nplates.begin(), nplates.end());
     string str = vet2string(nplates);
     if (computed[str] != 0) return computed[str];
     int pos = 0;
     for (int i = 1; i < nplates.size(); i++)
         if (nplates[i] > nplates[pos])
             pos = i;
     if (nplates[pos] == 1) {
         computed[str] = 1;
     } else {
         computed[str] = min(trydivide(nplates,pos), trylow(nplates));
     }
     return computed[str];
 }
 
 int trylow(vector<int> nplates) {
     for (int i = 0; i < nplates.size(); i++) 
         nplates[i]--;
     return 1+tryit(nplates);
 }
 
 int trydiff(vector<int> nplates, int pos, int diff) {
     int tmp = nplates[pos];
     nplates[pos] = nplates[pos] - diff;
     nplates.push_back(tmp - nplates[pos]);
     return 1+tryit(nplates);
 }
 
 int trydivide(vector<int> nplates, int pos) {
    int minimo = 10000;
    for (int i = 2; i < nplates[pos]; i++)
        minimo = min(minimo, trydiff(nplates, pos, i));
    return minimo;
 }