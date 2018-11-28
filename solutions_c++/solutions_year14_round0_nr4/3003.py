#include <iostream>
#include <fstream>
#include <stdlib.h>

using namespace std;
int t;
int n;
double a[1200];
double b[1200];
int cmp(const void* a, const void* b) {
    double x = *((double*)a);
    double y = *((double*)b);
    if (x - y > 1e-10) {
        return 1;
    }
    if (y - x > 1e-10) {
        return -1;
    }
    return 0;
}

void process() {
    qsort(a, n, sizeof(a[0]), cmp);
    qsort(b, n, sizeof(b[0]), cmp);

    int i,j, count;
    /*
    for(i=0;i<n;i++)
        cout<<" "<<a[i];
    cout<<endl;
    for(i=0;i<n;i++)
        cout<<" "<<b[i];
    cout<<endl;
    */
    count = 0;
    int a1 = 0, b1=0, a2 = n-1, b2 = n-1;
    
    while(true) {
        if (a[a1] - b[b1] > 1e-10) {
            count ++;
            a1++;
            b1++;
        } else {
            a1++;
            b2--;
        }
        
        if (a1 >= n) {
            cout<<" "<<count;
            break;
        }
        
    }
    a1 = 0, b1 =0, count = 0;
    while(true) {
        while(b1 <n &&a[a1] - b[b1] > 1e-10) {
            b1++;
        }
        if (b1>=n) {
            cout<<" "<<(n-count);
            break;
        }
        count++;
        b1++;
        a1++;
    }
    cout<<endl;
}

int main() {
    //ifstream in("d.in");
    int i,j;
    cin>>t;
    for(i = 0;i<t;i++){
        cout<<"Case #"<<(i+1)<<":";
        cin>>n;
        for(j=0;j<n;j++)
            cin>>a[j];
        
        for(j=0;j<n;j++)
            cin>>b[j];
        process();
    }
    
    return 0;
}