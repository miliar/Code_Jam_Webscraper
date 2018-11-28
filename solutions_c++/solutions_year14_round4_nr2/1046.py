#include <iostream>
#include <fstream>
#include <cassert>
using namespace std;

const char * infile="B-large.in";
const char * outfile="pb-large.out";

void re_order(int b[], int n) {
    for (int i=0, j=n-1; i<j; i++, j--) 
        swap(b[i], b[j]);
}

long long getanti(int b[], int n) {
    long long res=0;
    for (int i=0; i<n; i++)
        for (int j=i+1; j<n; j++)
            if (b[i] > b[j]) res++;
    return res;
}

long long getans(int a[], int n) {
    long long ans=0;
    
    long long i=0, j=n-1;
    while (i<j) {
        int min_index = i;
        for (int k=i+1; k<=j; k++)
            if (a[k] < a[min_index])
                min_index = k;
                
        if (min_index - i < j - min_index) {
            ans += min_index - i;
            for (int k = min_index; k>i; k--) 
                swap(a[k-1], a[k]);                        
            i++;
        }
        else {
            ans += j - min_index;
            for (int k = min_index; k<j; k++)
                swap(a[k], a[k+1]);
            j--;
        }    
    }
    
    return ans;
}

int main() {
    ifstream fin(infile);
    assert(fin);
    ofstream fout(outfile);
    assert(fout);
    
    int test;
    fin >> test;

    for (int count=1; count<=test; count++){
        int n;
        fin >> n;
        int a[n];
        for (int i=0; i<n; i++)
            fin >> a[i];
        
        fout << "Case #" << count << ": " << getans(a, n) << endl;
    }
    
    
    fin.close();
    fout.close();
    return 0;
}
