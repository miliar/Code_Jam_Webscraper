#include <iostream>
#include <fstream>
#include <cassert>
#include <algorithm>
using namespace std;

const char *infile = "D-large.in";
const char *outfile = "pd-large.out";

int getAns1(double a[], double b[], int n) {
    int j=0;
    int ans1=0;
    for (int i=0; i<n; i++) {
        if (a[i] > b[j]) {
            ans1++;
            j++;
        }
    }
    return ans1;
}

int getAns2(double a[], double b[], int n) {
    int ans2=0;
    int i=n-1;
    int m=n;
    int k=n;
    while (i>=0) {
        while (k>0 && a[i] < b[k-1]) 
            k--;
        
        int j=i-1;
        while (j>=0 && (k==0 || a[j]>b[k-1])) 
            j--;
        
        if (i-j > m-k) {
            ans2 += (i-j) - (m-k);
            m = k;
        }
        else {
            m -= i-j;
        }
        
        i=j;
    }
    
    return ans2;
}

int main() {
    ifstream fin(infile);
    assert(fin);
    ofstream fout(outfile);
    assert(fout);
    
    int test;
    fin >> test;
    for (int count=1; count<=test; count++) {
        int n;
        fin >> n;
        double a[n], b[n];
        for (int i=0; i<n; i++) 
            fin >> a[i];
        for (int i=0; i<n; i++) 
            fin >> b[i];
        sort(a, a+n);
        sort(b, b+n);
        int ans1 = getAns1(a, b, n);
        int ans2 = getAns2(a, b, n);
        fout << "Case #" << count << ": " << ans1 << " " << ans2 << endl;
    }
    
    fin.close();
    fout.close();
    return 0;
}
