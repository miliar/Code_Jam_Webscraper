#include <iostream>
#include <stdio.h>
#include <string.h>
#include <string>
#include <vector>
#include <algorithm>
#include <iomanip>
#include <sstream>
#include <math.h>

#define fo(a, b, c) for(a = ( b ); a < ( c ); a++)
#define fr(a, b) fo(a, 0, ( b ))
#define fi(a) fr(i, ( a ))
#define fj(b) fr(j, ( b ))
#define fk(c) fr(k, ( c ))

#define ul64 uint_least64_t
#define vs vector<string>
#define vi vector<int>
#define vd vector<double>
#define vul64 vector<ul64>
#define vc vector<char>
#define pb push_back
#define ppb pop_back
#define ss stringstream

using namespace std;

bool desc(int a, int b)
{
    return (a>b);
}

void swap(double &a, double &b)
{
    double t;
    t = a;
    a = b;
    b = t;
}

int main()
{
    int i, j, k, tt, cases;
    int n;
    double t;
    vd p1, p2, temp;

    freopen("D-large.in", "r", stdin);
    freopen("d-small0.out", "w", stdout);
    cin>>tt;
    fr(cases, tt)
    {
        cin>>n;
        p1.clear();
        p2.clear();
        temp.clear();
        t = 0;
        fi(n)   {cin>>t; p1.pb(t); }
        fi(n)   {cin>>t; p2.pb(t); temp.pb(t); }

        //sort(p1.begin(), p1.end());
        fi(n) fj(n-1) if(p1[j]< p1[j+1]) swap(p1[j], p1[j+1]);
        fi(n) fj(n-1) if(temp[j]< temp[j+1]) swap(temp[j], temp[j+1]);
        //sort(p2.begin(), p2.end());

        //fi(n) cout<<p1[i]<<" "; cout<<endl;
        //fi(n) cout<<temp[i]<<" ";
        //cout<<endl<<endl;
        i = k = 0;
        while(i<n && k<n){
            //cout<<p1[i]<<" "<<temp[k]<<" "<<i<<" "<<k<<endl;
            if(temp[k] == 1) {k++; continue; }
            if(p1[i]>temp[k]) {i++; temp[k++] = 1; }
            //if(p1[i]<p2[k] && p1[i]<p2[k+1]) {i++; k++; }
            else k++;
        }
        cout<<"Case #"<<cases+1<<": "<<i<<" ";
        i = k = 0;
        sort(p2.begin(), p2.end());
        sort(p1.begin(), p1.end());
        while(k<n && i<n){
            if(p1[i]<p2[k]) {i++; k++; }
            else k++;
        }
        cout<<n-i<<endl;
    }
}
