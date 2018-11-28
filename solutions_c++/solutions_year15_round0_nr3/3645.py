#include "j.h"
#include <cassert>
int key[3] = {2, 3, 4};
vector<vector<int> > pro;
int multiply(int a, int b) {
    int sign = -1;
    if((a > 0 && b > 0) || (a < 0 && b < 0))
        sign = 1;
    //printf("Multiplying (%d, %d)\n", a, b);
    int val = sign*pro[abs(a)][abs(b)];
    //printf("Multiply(%d, %d) = %d\n", a, b, val);
    return val;
}
int product(int start, int end, string &s) {
    int prod = s[start]-103;
   for(int i = start+1; i <= end; i++) {
       //printf("Product now is %d\n", prod);
    prod = multiply(prod, s[i]-103);
   }
   //printf("For substring %s, product is %d\n", s.substr(start, end-start+1).c_str(), prod);
   return prod;
}
bool di(int start, string &s, int pieceid) {
    if(s.size()-start < 3-pieceid)
        return false;
    //printf("Doing piece %d starting at %d\n", pieceid, start);
    if(pieceid == 2)
        return product(start, s.size()-1, s) == 4;
    for(int i = 0; i <= s.size()-(3-pieceid); i++) {
       if(product(start, start+i, s) == key[pieceid] &&
               di(start+i+1, s, pieceid+1))
           return true;
    }
    return false;
}
vector<vector<int> > divs;
int productOf(int start, int end, string &s, vector<int> &prods) {
    if(start == end) {
        //printf("ProductOf*: %s is %d\n", s.substr(start, end-start+1).c_str(), s[start]-103);
        //return prods[start];
        return s[start]-103;
    }
    if(start == 0)
        return prods[end];

    //int p = multiply(prods[end], prods[start-1]);
    int p = multiply(prods[start-1], prods[end]);
    //printf("ProductOf: %d, %d is %d\n", s[start]-103, s[end]-103, p);
    //printf("ProductOf: %s is %d (%d, %d)\n", s.substr(start, end-start+1).c_str(), p, prods[end], prods[start-1]);
    return p; 
}

bool dijkstra(int L, int X, string &sp) {
    if(sp.size() < 2)
        return false;
    string s("");
    for(int i = 0; i < X; i++) {
        s.append(sp);
    }
    vector<int> prods(s.size(), 0);
    prods[0] = s[0]-103;
    for(int i = 1; i < s.size(); i++) {
        prods[i] = multiply(prods[i-1], s[i]-103);
        //printf("%d (%c), ", prods[i], s[i]);
    }
    if(prods[s.size()-1] != -1)
        return false;
    //printf("Prods = %d\n", prods[s.size()-1]);
    //printf("Prods = %d, %d, %d, %d\n", prods[0], prods[1], prods[8987], prods[8987]);
    //printf("%d\n", prods[s.size()-1]);
    //printv(prods);
    for(int i = 1; i < s.size()-1; i++) {
        for(int j = i+1; j <= s.size()-1; j++) {
            //printf("********* i = %d, j = %d *******\n", i, j);
            if((productOf(0, i-1, s, prods)) == 2 &&
                    (productOf(i, j-1, s, prods)) == 3 &&
                        (productOf(j, s.size()-1, s, prods)) == 4) {
                //printf("Found it at i = %d, j = %d\n", i, j);
                return true;
            }
        }
    }
    //return di(0, s, 0);
    return false;
}

int multip(int L, int X, string &sp) {
    string s;
    for(int i = 0; i < X; i++) {
        s.append(sp);
    }
    int prod = s[0]-103;
    for(int i = 1; i < s.size(); i++) {
        prod = multiply(prod, s[1]-103);
    }
    return prod;
}

int main() {
    pro.push_back(vector<int>({99, 1, 2, 3, 4}));
    pro.push_back(vector<int>({1, 1, 2, 3, 4}));
    pro.push_back(vector<int>({2, 2, -1, 4, -3}));
    pro.push_back(vector<int>({3, 3, -4, -1, 2}));
    pro.push_back(vector<int>({4, 4, 3, -2, -1}));

    int c = readSingleFromCin<int>();
    FE(ic, 1, c) {
        int L;
        int X;
        string s;
        cin >> L;
        cin >> X;
        cin >> s;
        assert(s.size() == L && "Invalid string length");
        bool ans = dijkstra(L, X, s);
        //int x = multip(L, X, s);
        //printf("Case #%d: %s (%d)\n", ic, ans ? "YES" : "NO", x);
        printf("Case #%d: %s\n", ic, ans ? "YES" : "NO");
    }
}
