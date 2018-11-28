#include <iostream>
#include <fstream>
#include <iomanip>
using namespace std;

ofstream fout ("D-small.out");
ifstream fin ("D-large.in");

void exchange(double &a, double &b);

void q_sort(int l, int r, double *p){
        double e = p[(l+r) /2];
        int i = l, j=r;
        do{
                while(i<=j && p[i]<e) i++;
                while(i<=j && p[j]>e) j--;
                if( i<=j ) {
                        exchange(p[i], p[j]);
                        i++;
                        j--;
                }
        }
        while(i<=j);
        if(i<r) q_sort(i, r , p);
        if(j>l) q_sort(l, j , p);
}

void exchange(double &a, double &b){
        double temp;
        temp = b;
        b = a;
        a = temp;

}

int main()
{
        int t; fin>>t;
        int n;

        for(int k=0; k<t;k++){
                 bool flag=0;
                 bool f=0;
                    int ans1=0,ans2=0;
                fin>>n;
                double g[n+1] , b[n+1], g_ori[n+1],  b_ori[n+1];
                for(int i=1; i<=n; i++) {fin>>g[i] ; g_ori[i] = g[i];}
                for(int i=1; i<=n; i++) {fin>>b[i];  b_ori[i] = b[i];}
                q_sort(1,n,g); q_sort(1,n,b);


                for(int i=n; i>0; i--){
                        if( b[i] >= g[i] ) {
                                ans2++;
                                b[i] = g[i] = 2;

                        }
                        if( b[i] < g[i]){
                                b[1] = 2;
                                g[i] = 2;
                        }
                        q_sort(1,n,b);
                        q_sort(1,n,g);
                }

                for(int i=1; i<=n; i++) { g[i] = g_ori[i];}
               for(int i=1; i<=n; i++) { b[i] = b_ori[i];}
                        q_sort(1,n,g); q_sort(1,n,b);
                  for(int i=n; i>0; i--){
                        if( g[i] >= b[i] ) {
                                ans1++;
                                b[i] = g[i] = 2;

                        }
                        if( g[i] < b[i]){
                                g[1] = 2;
                                b[i] = 2;
                        }
                        q_sort(1,n,b);
                        q_sort(1,n,g);
                }

                fout<<"Case #"<<k+1<<": " <<ans1<<" "<<n-ans2<<endl;
        }
    return 0;
}
